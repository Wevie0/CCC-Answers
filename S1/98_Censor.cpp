#include <iostream>
#include <string>
#include <vector>
#include <sstream>

int n;
std::string x, input;

void solve()
{
    std::vector<std::string> words;
    std::getline(std::cin, x);
    std::stringstream strstr(x);
    while (std::getline(strstr, input, ' '))
    {
        words.push_back(input);
    }
    for (std::string word : words)
    {
        if (word.length() != 4)
        {
            std::cout << word << " ";
        }
        else
        {
            std::cout << "**** ";
        }
    }
}

int main()
{
    std::cin.sync_with_stdio(0);
    std::cin.tie(0);
    std::cin >> n;
    for (int i = 0; i <= n; ++i)
    {
        solve();
        if (i != 0)
            std::cout << "\n";
    }
    return 0;
}
