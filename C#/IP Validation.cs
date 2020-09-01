using System;
using System.Linq;

namespace Solution
  {
  class Kata
    {
    public static bool is_valid_IP(string IpAddres)
    {
      string[] splitted = IpAddres.Split('.');
      if (splitted.Length != 4) return false;
      foreach (string str in splitted)
        if (str.Any(x => !char.IsNumber(x)) || str[0] == '0') return false;
      return true;
    }
    }
  }