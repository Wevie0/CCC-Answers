#include <iostream>
#include <string>
#include <vector>

int main()
{
    std::vector <std::string> text;
    int n;
    int s = 0;
    int t = 0;

    std::cin >> n;

    for (int i = 0; i <= n; i++)
    {
        std::string line;
        std::getline(std::cin, line);
        text.push_back(line);
    }

    for (int i = 0; i < text.size(); i++)
    {
        for (int j = 0; j < text[i].size(); j++)
        {
            if (text[i][j] == 't' || text[i][j] == 'T')
            {
                t++;
            }
            else if (text[i][j] == 's' || text[i][j] == 'S')
            {
                s++;
            }
        }
    }

    if (t > s)
    {
        std::cout << "English\n";
    }
    else
    {
        std::cout << "French\n";
    }
    
    return 0;
}