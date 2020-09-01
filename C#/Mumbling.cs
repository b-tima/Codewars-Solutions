using System;

public class Accumul 
{
    public static string Accum(string s)
    {
      string returnValue = "";
      for(int i = 0; i < s.Length; i++)
      {
        for(int j = 1; j <= i+1; j++)
        {
          if (j == 1)
            returnValue += char.ToUpper(s[i]);
          else
            returnValue += char.ToLower(s[i]);
        }
        if (i != s.Length-1)
          returnValue += '-';
      }
      return returnValue;
    }
}