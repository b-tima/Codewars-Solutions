std::string get_middle(std::string input)
{
  int len = std::strlen(input.c_str());
  int middle = len / 2;
  if (len % 2 == 1)
    return std::string(1, *(input.begin() + middle));
  else
    return std::string(1, *(input.begin() + middle - 1)) + std::string(1, *(input.begin() + middle));
}