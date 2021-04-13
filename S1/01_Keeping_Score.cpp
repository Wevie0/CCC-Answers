#include <iostream>
#include <string>
#include <vector>

int main()
{
    std::cin.sync_with_stdio(0);
    std::cin.tie(0);

    std::string input;
    std::cin >> input;
    std::string output;

    std::vector<char> cards;
    short points = 0;
    short point_tot = 0;
    char current_suit = 'C';

    std::cout << "Cards Dealt \t \t Points\n";

    for (int i = 0; i < input.length(); i++)
    {
        if (input[i] == 'C')
        {
            continue;
        }

        if (input[i] == 'D')
        {
            if (cards.size() == 0)
            {
                points += 3;
            }

            else if (cards.size() == 1)
            {
                points += 2;
            }

            else if (cards.size() == 2)
            {
                points++;
            }

            output = "Clubs ";
            for (int i = 0; i < cards.size(); i++)
            {
                output += cards[i];
                output += ' ';
            }

            std::cout << output << "\t      " << points << '\n';
            point_tot += points;
            points = 0;
            cards.clear();
            continue;
        }

        else if (input[i] == 'H')
        {
            if (cards.size() == 0)
            {
                points += 3;
            }

            else if (cards.size() == 1)
            {
                points += 2;
            }

            else if (cards.size() == 2)
            {
                points++;
            }

            output = "Diamonds ";
            for (int i = 0; i < cards.size(); i++)
            {
                output += cards[i];
                output += ' ';
            }

            std::cout << output << "\t      " << points << '\n';
            point_tot += points;
            points = 0;
            cards.clear();
            continue;
        }
        else if (input[i] == 'S')
        {
            if (cards.size() == 0)
            {
                points += 3;
            }

            else if (cards.size() == 1)
            {
                points += 2;
            }

            else if (cards.size() == 2)
            {
                points++;
            }

            output = "Hearts ";
            for (int i = 0; i < cards.size(); i++)
            {
                output += cards[i];
                output += ' ';
            }

            std::cout << output << "\t      " << points << '\n';
            point_tot += points;
            points = 0;
            cards.clear();
            continue;
        }

        if (input[i] == 'A')
        {
            points += 4;
        }
        else if (input[i] == 'K')
        {
            points += 3;
        }
        else if (input[i] == 'Q')
        {
            points += 2;
        }
        else if (input[i] == 'J')
        {
            points += 1;
        }

        cards.push_back(input[i]);
    }
    if (cards.size() == 0)
    {
        points += 3;
    }

    else if (cards.size() == 1)
    {
        points += 2;
    }

    else if (cards.size() == 2)
    {
        points++;
    }

    output = "Spades ";
    for (int i = 0; i < cards.size(); i++)
    {
        output += cards[i];
        output += ' ';
    }

    std::cout << output << "\t      " << points << '\n';
    point_tot += points;

    std::cout << "Total " << point_tot;

    return 0;
}