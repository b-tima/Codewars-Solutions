long long thirt(long long n)
{
    int pattern[6] ={ 1, 10, 9, 12, 3, 4 };
    long long lastSum = 0;
    while (n != lastSum) {
        lastSum = n;
        long long patternSum = 0;
        int i = 0;
        while(n > 0){
            patternSum += (n % 10) * pattern[i++%6];
            n /= 10;
        }
        n = patternSum;
    }
    return n;
}