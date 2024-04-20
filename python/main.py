class TreeNode:
    def __init__(self, label, children):
        self.label = label
        self.children = children
        self.rank = len(children)


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


print(stairs(3))
