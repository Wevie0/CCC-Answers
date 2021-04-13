#include <iostream>
#include <string>
#include <vector>

int main()
{
    std::vector <long long> nums;
    long long k;
    long long n;
    long long out = 0;

    std::cin >> k;

    for (long long i = 0; i < k; i++)
    {
        std::cin >> n;
        if (n != 0)
        {
            nums.push_back(n);
        }
        else
        {
            nums.pop_back();
        }
    }

    for (long long num : nums)
    {
        out += num;
    }
    std::cout << out << '\n';

    return 0;
}