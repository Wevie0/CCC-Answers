#include <iostream>
#include <string>
#include <vector>

int main()
{
    int n;
    int out;

    std::cin >> n;
    n -= 1;

    
    out = (n * (n-1) * (n-2))/6;
    
    std::cout << out << '\n';
    return 0;
}