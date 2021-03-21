void wave(const char *y, char **target)
{
    int whitespaces = 0;
    for (int i = 0; y[i] != '\0'; i++)
    {
        if (y[i] == ' ')
        {
            whitespaces++;
            continue;
        }
        for (int j = 0; y[j] != '\0'; j++)
        {
            target[i - whitespaces][j] = i == j ? y[j] + ('A' - 'a') : y[j];
        }
    }
}