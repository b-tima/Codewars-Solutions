using System;

public class BuyCar {

    public static int[] nbMonths(int startPriceOld, int startPriceNew, int savingperMonth, double percentLossByMonth)
    {
      if (startPriceOld >= startPriceNew)
        return new int[] { 0, startPriceOld - startPriceNew };
      int months = 0;
      double percentage = percentLossByMonth;
      double currentCarPrice = startPriceOld;
      double currentPrice = startPriceNew;
      double currentBank = 0;
      while (true)
      {
        months++;
        if (months % 2 == 0)
          percentage += 0.5;
        currentPrice *= 1 - (percentage / 100);
        currentCarPrice *= 1 - (percentage / 100);
        currentBank = currentCarPrice + months * savingperMonth;
        if (currentBank >= currentPrice)
          return new int[] { months, Convert.ToInt32(currentBank - currentPrice) };
      }
    }
}