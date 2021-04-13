#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

bool distinct(int year)
{
    std::string year_s = std::to_string(year);
    for (unsigned int i = 0; i < year_s.length(); i++)
    {
        if (std::count(year_s.begin(), year_s.end(), year_s[i]) > 1)
        {
            return false;
        }
    }
    return true;
}

int main()
{
    int y;
    std::cin >> y;
    while (true)
    {
        y++;
        if (distinct(y))
        {
            std::cout << y << '\n';
            return 0;
        }

    }
    
    return 0;
}