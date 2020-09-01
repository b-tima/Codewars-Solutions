using System;
using System.Linq;

class WhichAreIn
{
    public static string[] inArray(string[] array1, string[] array2) => array1.Where(x => array2.Any(y => y.Contains(x))).Distinct().OrderBy(x => x).ToArray();
}