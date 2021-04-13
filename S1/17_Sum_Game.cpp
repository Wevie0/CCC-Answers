#include <iostream>

int main()
{

    int n;
    int score;
    int r = 0;
    int output = 0;

    std::cin >> n;

    int swifts[n];
    int semaphores[n];

    for (int i = 0; i < n; i++)
    {
        std::cin >> score;
        r += score;
        swifts[i] = r;
    }
    r = 0;
    for (int i = 0; i < n; i++)
    {
        std::cin >> score;
        r += score;
        semaphores[i] = r;
    }

    for (int i = 0; i < n; i++)
    {
        if (swifts[i] == semaphores[i])
        {
            output = i + 1;
        }
    }

    std::cout << output << '\n';
    return 0;
}