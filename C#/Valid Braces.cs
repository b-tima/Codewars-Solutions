using System;
using System.Linq;
using System.Collections.Generic;

public class Brace {

    public static readonly char[] openedBraces = { '(', '[', '{' };
    public static readonly char[] closedBraces = { ')', ']', '}' };
    public static bool validBraces(string braces)
    {
      string str = string.Join(string.Empty, braces.Where(x => openedBraces.Contains(x) || closedBraces.Contains(x)));
      Stack<int> order = new Stack<int>();
      foreach(char c in str)
      {
        switch (c)
        {
          case '(':
          case '[':
          case '{':
            order.Push(openedBraces.ToList().IndexOf(c));
            continue;
          default:
            if (order.Count < 1 ||
              order.Pop() != closedBraces.ToList().IndexOf(c))
              return false;
            continue;
        }
      }
      return order.Count < 1;
    }
}