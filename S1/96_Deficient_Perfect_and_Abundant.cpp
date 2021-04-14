#include <iostream>
#include <string>
#include <vector>
#include <cmath>

std::vector <int> divisors(int x)
{
    std::vector <int> output;
    for (int i = 1; i < x; i++)
    {
        if (x % i == 0)
        {
            output.push_back(i);
        }
    }
    return output;
}

int main()
{
    std::cin.sync_with_stdio(0);
    std::cin.tie(0);
    
    int nums;
    int n;
    int sum;
    std::vector <int> divs;
    
    std::cin >> nums;

    for (int i = 0; i < nums; i++)
    {
        std::cin >> n;
        divs = divisors(n);
        for (int i = 0; i < divs.size(); i++)
        {
            sum += divs[i];
        }
        
        if (sum < n)
        {
            std::cout << n << " is a deficient number.\n";
        }
        else if (sum == n)
        {
            std::cout << n << " is a perfect number.\n";
        }
        else 
        {
            std::cout << n << " is an abundant number.\n";
        }
        sum = 0;
    }
    
    return 0;
}