#include <iostream>
#include <string>
#include <vector>

int main()
{
    std::cin.sync_with_stdio(0);
    std::cin.tie(0);
    
    unsigned short n;
    unsigned short y;
    unsigned short m;
    unsigned short d;

    // 1989 2 27

    std::cin >> n;

    for (int i = 0; i < n; i++)
    {
        std::cin >> y >> m >> d;
        if (y - 1989 < 0)
        {
            std::cout << "Yes\n";
            continue;
        }
        if (y - 1989 == 0 && m - 2 < 0)
        {
            std::cout << "Yes\n";
            continue;
        }
        if (y - 1989 == 0 && m - 2 == 0 && d - 27 <= 0)
        {
            std::cout << "Yes\n";
            continue;
        }
        std::cout << "No\n";
    }
    
    return 0;
}