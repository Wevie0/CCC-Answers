#include <iostream>
#include <string>
#include <vector>

int main()
{
    std::cin.sync_with_stdio(0);
    std::cin.tie(0);

    short current = 1;
    short input;

    while (true)
    {
        std::cin >> input;
        if (input == 0)
        {
            std::cout << "You Quit!\n";
            break;
        }
        current += input;

        if (current == 9)
        {
            current = 34;
        }
        else if (current == 40)
        {
            current = 64;
        }
        else if (current == 67)
        {
            current = 86;
        }

        else if (current == 54)
        {
            current = 19;
        }
        else if (current == 90)
        {
            current = 48;
        }
        else if (current == 99)
        {
            current = 77;
        }
        if (current > 100)
        {
            current -= input;
        }

        std::cout << "You are now on square " << current << '\n';
        if (current >= 100)
        {
            std::cout << "You Win!\n";
            break;
        }
    }

    return 0;
}