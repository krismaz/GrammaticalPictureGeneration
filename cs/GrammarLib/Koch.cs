using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GrammarLib
{
    public class Koch
    {
        public static IEnumerable<Drawing> Generate()
        {
            Drawing d = new Drawing(Line.Right);
            while (true)
            {
                yield return d;
                d = d + d * Transformation.ClockWise90 + d + d * Transformation.ClockWise270 + d*Transformation.ClockWise270 + d + d * Transformation.ClockWise90 + d;
            }
        }
    }
}
