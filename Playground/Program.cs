using GrammarLib;
using System;
using System.Linq;

namespace Playground
{
    class Program
    {
        static void Main(string[] args)
        {
            foreach(Drawing d in DragonCurve.Generate().Take(10))
            {
                Console.WriteLine(d);
                Console.WriteLine(string.Join("\n", d.Segments.Select(s => string.Format("<line x1 = \"{0}\" y1 = \"{1}\" x2 = \"{2}\" y2 = \"{3}\" stroke = \"blue\" stroke-width = \"4\" />",s.P1.X*10, s.P1.Y * 10, s.P2.X * 10, s.P2.Y * 10))));
            }
            Console.ReadKey();

        }
    }
}
