namespace myjinxin
{
    using System;
    using System.Linq;
    
    public class Kata
    {
    public bool InviteMoreWomen(int[] L)
    {
      return L.Count(x => x == -1) < L.Count(x => x == 1);
    }
    }
}