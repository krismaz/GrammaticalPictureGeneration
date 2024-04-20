using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GrammarLib
{
    public class DragonCurve
    {
        public static IEnumerable<Drawing> Generate()
        {
            Drawing d = new Drawing(Line.Up);
            while (true)
            {
                yield return d;
                d = d + ((-d)*Transformation.ClockWise90);
            }
        }
    }
}
