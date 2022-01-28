#include <iostream>
using namespace std;

unsigned long int silnia(int x)
{
    if (x == 0)
    {
        return 1;
    }
    else
    {
        return x * silnia(x - 1);
    }
}
unsigned long int fibonacci(int x)
{
    if (x < 2)
    {
        return x;
    }
    else
    {
        return fibonacci(x - 1) + fibonacci(x - 2);
    }
}
int main()
{
    cout << silnia(5) << endl;
    cout << fibonacci(100) << endl;
}