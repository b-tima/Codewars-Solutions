using System;
using System.Linq;

public class Printer 
{
    public static string PrinterError(string s)
    {
      string acceptedValues = "abcdefghijklm";
      return $"{s.Count(c => !acceptedValues.Contains(c))}/{s.Length}";
    }
}