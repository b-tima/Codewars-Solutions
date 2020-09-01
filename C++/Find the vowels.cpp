std::vector<int> vowelIndices(std::string word)
{
  std::string vowels = "AEIOUY";
  std::vector<int> res;

  for (auto i = word.begin(); i != word.end(); ++i)
    for (auto j = vowels.begin(); j != vowels.end(); ++j)
      if (toupper(*i) == *j)
        res.push_back(std::distance(word.begin(), i) + 1);

  return res;
}