#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

int main()
{
    std::vector <std::string> cities;
    std::vector <signed short> temps;

    while (true)
    {
        std::string c;
        short t;
        std::cin >> c >> t;
        cities.push_back(c);
        temps.push_back(t);
        if (c == "Waterloo")
        {
            break;
        }
    }

    short min_index = std::min_element(temps.begin(),temps.end()) - temps.begin();

    std::cout << cities[min_index] << '\n';

    return 0;
}