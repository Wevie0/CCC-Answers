#include <iostream>

int main()
{
    short n;
    std::cin >> n;
    short heights[n + 1];
    short widths[n];

    for (int i = 0; i < n + 1; i++)
    {
        std::cin >> heights[i];
    }

    for (int i = 0; i < n; i++)
    {
        std::cin >> widths[i];
    }

    short left;
    short right;
    double total;

    for (int i = 0; i < n; i++)
    {
        left = heights[i];
        right = heights[i + 1];
        if (left == right)
        {
            total += left * widths[i];
        }
        else if (left > right)
        {
            total += right * widths[i];
            total += ((left - right) * widths[i]) / 2.0;
        }
        else
        {
            total += left * widths[i];
            total += ((right - left) * widths[i]) / 2.0;
        }
    }

    std::cout << std::fixed << total << '\n';
    return 0;
}