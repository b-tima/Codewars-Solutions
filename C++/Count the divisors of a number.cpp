int divisors(long long n)
{
  long long divs = 1;

  for (long long i = 1; i <= n / 2; i++)
    if (n % i == 0) divs++;

  return divs;
}