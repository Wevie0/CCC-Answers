#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

int main()
{
    int n;

    std::cin >> n;
    if (n == 0)
    {
        return 0;
    }

    std::string names[n];
    int scores[n];
    int r;
    int s;
    int d;

    for (int i = 0; i < n; i++)
    {
        std::cin >> names[i] >> r >> s >> d;
        scores[i] = 2 * r + 3 * s + d;
    }

    int best = 0;
    int sec = 0;
    std::string best_n = "";
    std::string sec_n = "";

    for (int i = 0; i < n; i++)
    {
        if (scores[i] > best || (scores[i] == best && std::string(names[i]) < std::string (best_n)))
        {
            sec = best;
            sec_n = best_n;
            best = scores[i];
            best_n = names[i];
        }
        else if (scores[i] > sec || (scores[i] == sec && std::string(names[i]) < std::string (sec_n)))
        {
            sec = scores[i];
            sec_n = names[i];
        }
    }
    std::cout << best_n << '\n' << sec_n << '\n';
    return 0;
}