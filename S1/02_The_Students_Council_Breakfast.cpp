#include <iostream>
#include <string>
#include <vector>

int main()
{
    std::cin.sync_with_stdio(0);
    std::cin.tie(0);

    int p;
    int g;
    int r;
    int o;
    int c;

    short comb = 0;
    short min = 999;

    std::cin >> p >> g >> r >> o >> c;

    for (int i = 0; i <= (c / p); i++)
    {
        for (int j = 0; j <= (c / g); j++)
        {
            // std::cout << c / g << '\n';
            for (int k = 0; k <= (c / r); k++)
            {
                // std::cout << i << '\t' << j << '\t' << k << '\t' << '\n';
                for (int l = 0; l <= (c / o); l++)
                {
                    if (i * p + j * g + k * r + l * o == c)
                    {
                        std::cout << "# of PINK is " << i << " # of GREEN is "<< j
                         << " # of RED is " << k << " # of ORANGE is " << l << '\n';
                        comb++;
                        if (i + j + k + l < min)
                        {
                            min = i + j + k + l;
                        }
                    }
                }
            }
        }
    }
    std::cout << "Total combinations is " << comb << ".\n";
    std::cout << "Minimum number of tickets to print is " << min << ".\n";
    return 0;
}