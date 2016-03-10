namespace GrammarLib
{
    public struct Point
    {
        public double X { get; set; }
        public double Y { get; set; }

        public static Point operator+(Point p, Line l)
        {
            return new Point { X = p.X + l.X, Y = p.Y + l.Y };
        }

        public override string ToString()
        {
            return string.Format("({0}, {1})", X, Y);
        }

    }
}