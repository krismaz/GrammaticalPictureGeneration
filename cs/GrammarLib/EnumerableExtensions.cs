using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GrammarLib
{
    static class EnumerableExtensions
    {

        //http://stackoverflow.com/questions/3224935/in-scala-how-do-i-fold-a-list-and-return-the-intermediate-results
        public static IEnumerable<TResult> Scan<TSource, TResult>(
                        this IEnumerable<TSource> source,
                        TResult seed,
                        Func<TResult, TSource, TResult> func)
        {
            TResult current = seed;
            yield return current;
            foreach (TSource item in source)
            {
                current = func(current, item);
                yield return current;
            }
        }
    }   
}
