unsigned long int McCarthy(int x)
{
    if (x > 100)
    {
        return (x - 10);
    }
    else
    {
        return McCarthy(McCarthy(x + 11));
    }
}