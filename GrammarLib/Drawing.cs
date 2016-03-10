using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GrammarLib
{
    public class Drawing
    {
        private List<Line> _lines = new List<Line> { };
        private Point _origin { get; set; } = new Point();
        public IEnumerable<Point> Points { get { return _lines.Scan(_origin, (point, line) => point + line); } }
        public IEnumerable<Segment> Segments { get { return Points.Zip(Points.Skip(1), (p1, p2) => new Segment { P1 = p1, P2 = p2 }); } }
        public Point End { get { return Points.Last(); } } 

        public static Drawing operator+(Drawing d1, Drawing d2)
        {
            return new Drawing { _lines = d1._lines.Concat(d2._lines).ToList(), _origin = d1._origin };
        }

        public static Drawing operator-(Drawing d)
        {
            return new Drawing { _lines = d._lines.Select(l => -l).Reverse().ToList(), _origin = d.End};
        }

        public static Drawing operator*(Drawing d, Transformation t)
        {
            return new Drawing { _lines = d._lines.Select(l => l*t).ToList(), _origin = d._origin };
        }

        public Drawing()
        {
        }

        public Drawing(Line line)
        {
            _lines.Add(line);
        }

        public override string ToString()
        {
            return string.Join(" -> ", Points);
        }
    }
}
