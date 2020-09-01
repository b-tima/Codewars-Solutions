public class Triangle
{
    public static bool IsTriangle(int a, int b, int c)
    {
      return (a * b) / 2 > 0 && (a * c) / 2 > 0 && (c * b) / 2 > 0 &&
        a < b + c && a > b - c && a > c - b;
    }
}