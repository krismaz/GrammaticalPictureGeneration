using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GrammarLib
{
    public class Segment
    {
        public Point P1 { get; set; }
        public Point P2 { get; set; }
        public override string ToString()
        {
            return string.Format("({0} -> {1})", P1, P2);
        }

    }
}
