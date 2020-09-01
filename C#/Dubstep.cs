using System;
using System.Linq;

public class Dubstep
    {
    public static string SongDecoder(string input)
    {
      return string.Join(" ", input.Replace("WUB", " ").Split().Where(x => !string.IsNullOrEmpty(x))).ToUpper();
    }
    }