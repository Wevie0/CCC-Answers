#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

int main()
{
    std::string one;
    std::string two;

    std::cin >> one;
    std::cin >> two;

    int num_wilds = std::count(two.begin(), two.end(), '*');
    short difference;
    std::vector<char> ignore;

    for (int i = 0; i < one.length(); i++)
    {

        if (std::count(one.begin(), one.end(), one[i]) < std::count(two.begin(), two.end(), one[i]))
        {
            std::cout << "N\n";
            return 0;
        }
        else if (std::count(one.begin(), one.end(), one[i]) > std::count(two.begin(), two.end(), one[i]) &&
         !(std::find(ignore.begin(), ignore.end(), one[i]) != ignore.end()))
        {
            ignore.push_back(one[i]);
            num_wilds -= (std::count(one.begin(), one.end(), one[i]) - std::count(two.begin(), two.end(), one[i]));
        }

        if (num_wilds < 0)
        {
            std::cout << "N\n";
            return 0;
        }
    }
    std::cout << "A\n";
    return 0;
}