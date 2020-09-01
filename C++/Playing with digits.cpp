#include <cmath>

class DigPow
{
public:
  static int digPow(int n, int p);
};

int DigPow::digPow(int n, int p)
{
  int sum = 0;
  std::string n_to_string = std::to_string(n);

  for(auto i = n_to_string.begin(); i != n_to_string.end(); ++i)
  {
    sum += std::pow((*i - '0'), p);
    ++p;
  }

  return sum % n == 0 ? sum / n : -1;
}