using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GrammarLib
{
    public struct Transformation
    {
        public double XX { get; set; }
        public double XY { get; set; }
        public double YX { get; set; }
        public double YY { get; set; }

        public static Transformation Unit = new Transformation { XX = 1, XY = 0, YY = 1, YX = 0 };
        public static Transformation ClockWise90 = new Transformation { XX = 0, XY = -1, YY = 0, YX = 1 };
        public static Transformation ClockWise180 = new Transformation { XX = -1, XY = 0, YY = -1, YX = 0 };
        public static Transformation ClockWise270 = new Transformation { XX = 0, XY = 1, YY = 0, YX = -1 };


    }
}
