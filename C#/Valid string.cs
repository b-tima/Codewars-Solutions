using System;
using System.Collections.Generic;
using System.Linq;

public class Kata
{
    public static bool ValidateString(string[] dictionary, string word)
    {
      List<char> currentWord = new List<char>();
      foreach (char c in string.Join(string.Empty, word.Split()))
      {
        currentWord.Add(c);
        if (!dictionary.Any(x => x.Contains(string.Join(string.Empty, currentWord)))) return false;
        if (dictionary.Any(x => x == string.Join(string.Empty, currentWord))) currentWord.Clear();
      }
      return currentWord.Count < 1;
    }
}