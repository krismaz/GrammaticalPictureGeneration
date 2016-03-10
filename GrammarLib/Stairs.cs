using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GrammarLib
{
    public class Stairs
    {
        public static IEnumerable<Drawing> Generate()
        {
            Drawing d1 = new Drawing(Line.Up);
            Drawing d2 = new Drawing(Line.Right);
            Drawing next = d1 + d2;
            while(true)
            {
                yield return next;
                next = next + next;

            }
        }
    }
}
