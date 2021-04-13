#include <iostream>
#include <string>
#include <vector>

int main()
{
    std::cin.sync_with_stdio(0);
    std::cin.tie(0);

    short quarters;
    short m1, m2, m3;
    unsigned short counter = 0;

    std::cin >> quarters >> m1 >> m2 >> m3;
    m1 = 35 - m1;
    m2 = 100 - m2;
    m3 = 10 - m3;

    while (true)
    {
        if (quarters == 0)
        {
            break;
        }

        m1 -= 1;
        quarters -= 1;
        counter++;
        if (m1 == 0)
        {
            quarters += 30;
            m1 = 35;
        }

        if (quarters == 0)
        {
            break;
        }

        m2 -= 1;
        quarters -= 1;
        counter++;
        if (m2 == 0)
        {
            quarters += 60;
            m2 = 100;
        }

        if (quarters == 0)
        {
            break;
        }

        m3 -= 1;
        quarters -= 1;
        counter++;
        if (m3 == 0)
        {
            quarters += 9;
            m3 += 10;
        }
    }
    std::cout << "Martha plays " << counter << " times before going broke.\n";
    return 0;
}