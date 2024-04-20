using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GrammarLib
{
    public struct Line
    {
        public double X { get; set; }
        public double Y { get; set; }

        public override string ToString()
        {
            return string.Format("({}, {})", X, Y);
        }

        public static Line operator-(Line l)
        {
            return new Line { X = -l.X, Y = -l.Y };
        }

        public static Line operator*(Line l, Transformation t)
        {
            return new Line { X = l.X * t.XX + l.Y * t.YX, Y = l.Y * t.YY + l.X * t.XY };
        }

        public static Line Up = new Line { X = 0, Y = 1 };
        public static Line Down = new Line { X = 0, Y = -1 };
        public static Line Right = new Line { X = 1, Y = 0 };
        public static Line Left = new Line { X = -1, Y = 0 };

    }
}
