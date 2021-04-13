#include <iostream>
#include <string>
#include <vector>
#include <cmath>

int main()
{
    long long a;
    long long b;
    long long six;
    int out = 0;

    std::cin >> a;
    std::cin >> b;

    for (long long i = 1; i <= b; i++)
    {
        six = std::pow(i, 6);
        if (six > b)
        {
            break;
        }
        if (a <= six && six <= b)
        {
            out++;
        }
 
    }
    std::cout << out << '\n';
    return 0;
}