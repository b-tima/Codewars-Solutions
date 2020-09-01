using System.Linq;

public class Kata
{
    public static int[] SortArray(int[] array)
    {
      if (array.Length == 0) return array;
      var odds = array.Where(x => x % 2 != 0 && x > 0).OrderBy(x => x).GetEnumerator();
      for (int i = 0; i < array.Length; i++)
        if (array[i] % 2 != 0 && array[i] > 0)
        {
          odds.MoveNext();
          array[i] = odds.Current;
        }

      odds = null;
      return array;
    }
}