#include <iostream>
#include <string>
#include <vector>

std::vector<int> remove(std::vector<int> list, int m)
{
    std::vector<int> output;
    for (int i = 0; i < list.size(); i++)
    {
        if ((i + 1) % m != 0 || i == 0)
        {
            output.push_back(list[i]);
        }
    }

    return output;
}

int main()
{
    int k;
    int m;
    int multiple;
    std::vector<int> people;

    std::cin >> k;
    std::cin >> m;

    for (int i = 1; i <= k; i++)
    {
        people.push_back(i);
    }

    for (int i = 0; i < m; i++)
    {
        std::cin >> multiple;
        people = remove(people, multiple);
    }

    for (int i : people)
    {
        std::cout << i << '\n';
    }

    return 0;
}