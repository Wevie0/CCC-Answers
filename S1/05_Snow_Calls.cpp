#include <iostream>
#include <string>
#include <vector>

char convert(char x)
{
    if (x == 'A' || x == 'B' || x == 'C')
    {
        return '2';
    }
    else if (x == 'D' || x == 'E' || x == 'F')
    {
        return '3';
    }
    else if (x == 'G' || x == 'H' || x == 'I')
    {
        return '4';
    }
    else if (x == 'J' || x == 'K' || x == 'L')
    {
        return '5';
    }
    else if (x == 'M' || x == 'N' || x == 'O')
    {
        return '6';
    }
    else if (x == 'P' || x == 'Q' || x == 'R' || x == 'S')
    {
        return '7';
    }
    else if (x == 'T' || x == 'U' || x == 'V')
    {
        return '8';
    }
    else if (x == 'W' || x == 'X' || x == 'Y' || x == 'Z')
    {
        return '9';
    }
    return x;
}

int main()
{
    std::cin.sync_with_stdio(0);
    std::cin.tie(0);

    int t;
    std::string number;
    std::cin >> t;
    
    std::string output = "";

    for (int j = 0; j < t; j++)
    {
        std::cin >> number;
        output = "";
        for (int i = 0; i < number.length(); i++)
        {
            if (output.length() >= 10)
            {
                break;
            }
            if (number[i] == '-')
            {
                continue;
            }
            output += (convert(number[i]));
        }
        output.insert(3, "-");
        output.insert(7, "-");
        std::cout << output << '\n';
    }
    return 0;
}