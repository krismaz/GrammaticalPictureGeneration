using GrammarLib;
using System;
using System.Linq;
using System.IO;
namespace Playground
{
    class Program
    {
        static void Main(string[] args)
        {
            foreach(Drawing d in Koch.Generate().Take(1))
            {
                Console.WriteLine(d);
                Console.WriteLine(string.Join("\n", d.Segments.Select(s => string.Format("<line x1 = \"{0}\" y1 = \"{1}\" x2 = \"{2}\" y2 = \"{3}\" stroke = \"blue\" stroke-width = \"4\" />",s.P1.X*10, s.P1.Y * 10, s.P2.X * 10, s.P2.Y * 10))));
            }
            var dd = Koch.Generate().Skip(6).First();
            //Console.WriteLine(dd);
            File.WriteAllText("dd.svg", "<svg xmlns=\"http://www.w3.org/2000/svg\" version=\"1.1\" > ");
            File.AppendAllText("dd.svg",string.Join("\n", dd.Segments.Select(s => string.Format("<line x1 = \"{0}\" y1 = \"{1}\" x2 = \"{2}\" y2 = \"{3}\" stroke = \"blue\" />", s.P1.X, s.P1.Y, s.P2.X, s.P2.Y))));
            File.AppendAllText("dd.svg", "</svg> ");
            Console.ReadKey();

        }

        static Drawing DragonRecursive(int i, int j = 0)
        {
            if(i == 0)
            {
                switch(j)
                {
                    case 0:
                        return new Drawing(Line.Up);
                    case 1:
                        return new Drawing(Line.Left);
                    case 2:
                        return new Drawing(Line.Down);
                    case 3:
                        return new Drawing(Line.Right);
                }
            }
            switch (j)
            {
                case 0:
                     return DragonRecursive(i - 1, 0) + DragonRecursive(i - 1, 1);
                case 1:
                    return DragonRecursive(i - 1, 2) + DragonRecursive(i - 1, 1);
                case 2:
                    return DragonRecursive(i - 1, 2) + DragonRecursive(i - 1, 3);
                case 3:
                    return DragonRecursive(i - 1, 0) + DragonRecursive(i - 1, 3);
            }
            return null;
        }
    }
}
