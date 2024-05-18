import cairo
import os
import time
import random
from math import sin, cos, pi


class TreeNode:
    def __init__(self, label, children=[]):
        self.label = label
        self.children = children
        self.rank = len(children)

    def Copy(self):
        return TreeNode(self.label, [c.Copy() for c in self.children])

    def Search(self, q) -> bool:
        if self.label == q:
            return True
        return any(c.Search(q) for c in self.children)

    def Tranform(self, rules):
        if self.label in rules:
            return random.choice(rules[self.label]).Copy()
        return TreeNode(self.label, [c.Tranform(rules) for c in self.children])

    def __str__(self) -> str:
        return f"{self.label}[{', '.join(str(c) for c in self.children)}]"


class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def Translate(self, x, y):
        return Line(self.x1+x, self.y1 + y, self.x2+x, self.y2 + y)

    def __str__(self) -> str:
        return f"({self.x1}, {self.y1}) -> ({self.x2}, {self.y2})"


class LineDrawing:
    def __init__(self, lines, ex, ey):
        self.lines = lines
        self.ex = ex
        self.ey = ey

    def Union(self, other):
        return LineDrawing(self.lines + other.lines, other.ex, other.ey)

    def Translate(self, x, y):
        return LineDrawing([l.Translate(x, y) for l in self.lines], self.ex + x, self.ey + y)

    def Concatenate(self, other):
        return self.Union(other.Translate(self.ex, self.ey))

    def __str__(self) -> str:
        return f"[{', '.join([str(l) for l in self.lines])}] -- {self.ex, self.ey} "

    def Show(self):
        filename = f"output/{time.time()}.svg"
        minx = min(min(l.x1, l.x2) for l in self.lines)
        maxx = max(max(l.x1, l.x2) for l in self.lines)
        miny = min(min(l.y1, l.y2) for l in self.lines)
        maxy = max(max(l.y1, l.y2) for l in self.lines)
        maxmax = max(maxx, maxy)

        if minx != 1 or miny != 1:
            self.Translate(-minx + 1, -miny + 1).Show()
            return

        with cairo.SVGSurface(filename, 500, 500) as surface:
            context = cairo.Context(surface)
            context.transform(cairo.Matrix(1, 0, 0, -1, 0, 500))

            context.set_line_width((maxmax)/200)

            context.scale(500/(maxmax+1), 500/(maxmax+1))
            for line in self.lines:
                context.move_to(line.x1, line.y1)
                context.line_to(line.x2, line.y2)

            context.stroke()

        os.startfile(os.path.abspath(filename))


LineDrawing.Empty = LineDrawing([], 0, 0)
LineDrawing.Left = LineDrawing([Line(0, 0, -1, 0)], -1, 0)
LineDrawing.Right = LineDrawing([Line(0, 0, 1, 0)], 1, 0)
LineDrawing.Up = LineDrawing([Line(0, 0, 0, 1)], 0, 1)
LineDrawing.Down = LineDrawing([Line(0, 0, 0, -1)], 0, -1)


def stairs(n):
    if not n:
        return LineDrawing.Empty

    if n == 1:
        return LineDrawing.Up.Concatenate(LineDrawing.Right)

    return stairs(n-1).Concatenate(stairs(n-1))


def dragon(n, m) -> LineDrawing:
    if n == 0 and m == 0:
        return LineDrawing.Up
    if n == 1 and m == 0:
        return LineDrawing.Left
    if n == 2 and m == 0:
        return LineDrawing.Down
    if n == 3 and m == 0:
        return LineDrawing.Right
    if n == 0:
        return dragon(0, m-1).Concatenate(dragon(1, m-1))
    if n == 1:
        return dragon(2, m-1).Concatenate(dragon(1, m-1))
    if n == 2:
        return dragon(2, m-1).Concatenate(dragon(3, m-1))
    if n == 3:
        return dragon(0, m-1).Concatenate(dragon(3, m-1))


def koch(n, m) -> LineDrawing:
    if n == 0 and m == 0:
        return LineDrawing.Right
    if n == 1 and m == 0:
        return LineDrawing.Down
    if n == 2 and m == 0:
        return LineDrawing.Left
    if n == 3 and m == 0:
        return LineDrawing.Up
    if n == 0:
        return koch(0, m-1).Concatenate(koch(1, m-1)).Concatenate(koch(0, m-1)).Concatenate(koch(3, m-1)).Concatenate(koch(3, m-1)).Concatenate(koch(0, m-1)).Concatenate(koch(1, m-1)).Concatenate(koch(0, m-1))
    if n == 1:
        return koch(1, m-1).Concatenate(koch(2, m-1)).Concatenate(koch(1, m-1)).Concatenate(koch(0, m-1)).Concatenate(koch(0, m-1)).Concatenate(koch(1, m-1)).Concatenate(koch(2, m-1)).Concatenate(koch(1, m-1))
    if n == 2:
        return koch(2, m-1).Concatenate(koch(3, m-1)).Concatenate(koch(2, m-1)).Concatenate(koch(1, m-1)).Concatenate(koch(1, m-1)).Concatenate(koch(2, m-1)).Concatenate(koch(3, m-1)).Concatenate(koch(2, m-1))
    if n == 3:
        return koch(3, m-1).Concatenate(koch(0, m-1)).Concatenate(koch(3, m-1)).Concatenate(koch(2, m-1)).Concatenate(koch(2, m-1)).Concatenate(koch(3, m-1)).Concatenate(koch(0, m-1)).Concatenate(koch(3, m-1))


def koch_island(m) -> LineDrawing:
    return koch(0, m).Concatenate(koch(1, m)).Concatenate(koch(2, m)).Concatenate(koch(3, m))


skylineRule = {
    "SL": [
        TreeNode("BL"),
        TreeNode("*",
                 [
                     TreeNode("*",
                              [
                                  TreeNode("SL"),
                                  TreeNode("r")
                              ]),
                     TreeNode("SL")
                 ])
    ],
    "BL": [
        TreeNode("*",
                 [
                     TreeNode("r"),
                     TreeNode("BL")
                 ]),
        TreeNode("*",
                 [
                     TreeNode("BL"),
                     TreeNode("r")
                 ]),
        TreeNode("*",
                 [
                     TreeNode("*",
                              [
                                  TreeNode("u"),
                                  TreeNode("BL")
                              ]),

                     TreeNode("d")
                 ]),
        TreeNode("r")
    ]
}


def concat_help(strings):
    if len(strings) == 1:
        return TreeNode(strings[0])
    return TreeNode("*", [TreeNode(strings[0]), concat_help(strings[1:])])


def concat_help_string(string):
    return concat_help([str(c) for c in string])


def concat_help_nodes(nodes):
    if len(nodes) == 1:
        return nodes[0]
    return TreeNode("*", [nodes[0], concat_help_nodes(nodes[1:])])


kochRule = {
    "r": [concat_help(["r", "u", "r", "d", "r"])],
    "u": [concat_help(["u", "l", "u", "r", "u"])],
    "d": [concat_help(["d", "r", "d", "l", "d"])],
    "l": [concat_help(["l", "d", "l", "u", "l"])]
}

hilbertRule = {
    "A": [concat_help_string("BuArAdC")],
    "B": [concat_help_string("ArBuBlD")],
    "C": [concat_help_string("DlCdCrA")],
    "D": [concat_help_string("CdDlDuB")]
}

sierpinskiBaseRule = {
    "AB": [concat_help(["AC", "AB", "CB"])],
    "AC": [concat_help(["AB", "AC", "BC"])],
    "BA": [concat_help(["BC", "BA", "CA"])],
    "BC": [concat_help(["BA", "BC", "AC"])],
    "CA": [concat_help(["CB", "CA", "BA"])],
    "CB": [concat_help(["CA", "CB", "AB"])],
}

sierpinskiGasketRule = {
    "AB": [TreeNode("r")],
    "AC": [TreeNode("u")],
    "BA": [TreeNode("l")],
    "BC": [concat_help_string("lu")],
    "CA": [TreeNode("d")],
    "CB": [concat_help_string("dr")],
}

sierpinskiAltRule = {
    "AB": [concat_help_string("rrrr")],
    "AC": [concat_help_string("rruuu")],
    "BA": [concat_help_string("llll")],
    "BC": [concat_help_string("lluuu")],
    "CA": [concat_help_string("dddll")],
    "CB": [concat_help_string("dddrr")],
}

turtleKochRule = {
    "F": [concat_help_nodes([TreeNode("F"), TreeNode("+", [TreeNode("F")]), TreeNode("-", [TreeNode("F")]), TreeNode("F")])]
}

turtleTreeRule = {
    "F": [concat_help_nodes([TreeNode("F"),
                             TreeNode("F"),
                             TreeNode("enc",
                                      [TreeNode("+",
                                                [concat_help_nodes([TreeNode("F"), TreeNode("F")])])]),
                             TreeNode("enc",
                                      [TreeNode("-",
                                                [concat_help_nodes([TreeNode("F"), TreeNode("+", [TreeNode("F")])])])])
                             ])]

}


def paint(node) -> LineDrawing:
    match node.label:
        case "*":
            return paint(node.children[0]).Concatenate(paint(node.children[1]))
        case 'u':
            return LineDrawing.Up
        case 'd':
            return LineDrawing.Down
        case 'l':
            return LineDrawing.Left
        case 'r':
            return LineDrawing.Right
        case _:
            return LineDrawing.Empty


def turtlepaint(node, angle, turn0=0, a0=0) -> LineDrawing:
    match node.label:
        case "*":
            return turtlepaint(node.children[0], angle, turn0, a0).Concatenate(turtlepaint(node.children[1], angle, turn0, a0))
        case 'F':
            x, y = cos(turn0*angle + a0), sin(turn0*angle + a0)
            return LineDrawing([Line(0, 0, x, y)], x, y)
        case '+':
            return turtlepaint(node.children[0], angle, turn0+1, a0)
        case '-':
            return turtlepaint(node.children[0], angle, turn0-1, a0)
        case 'enc':
            branch = turtlepaint(node.children[0], angle, turn0, a0)
            branch.ex = branch.ey = 0
            return branch
        case 'hide':
            branch = turtlepaint(node.children[0], angle, turn0, a0)
            branch.lines = []
            return branch
        case _:
            return LineDrawing.Empty


root = TreeNode("F")

for i in range(5):
    root = root.Tranform(turtleTreeRule)
    turtlepaint(root, pi/9, 0, pi/2).Show()
