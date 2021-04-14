#include <iostream>
#include <string>
#include <vector>

std::vector<std::string> cards;

bool no_high_card(int start, int stop)
{
    for (int i = start + 1; i <= start + stop; i++)
    {
        if (cards[i] == "ace" || cards[i] == "king" || cards[i] == "queen" || cards[i] == "jack")
        {
            return false;
        }
    }
    return true;
}

int main()
{
    std::cin.sync_with_stdio(0);
    std::cin.tie(0);

    std::string card;

    short a_points = 0;
    short b_points = 0;
    bool turn = true;

    for (int i = 0; i < 52; i++)
    {
        std::cin >> card;
        cards.push_back(card);
    }

    for (int i = 0; i < 52; i++)
    {
        if (cards[i] == "ace" && no_high_card(i, 4) && i < 48)
        {
            if (turn)
            {
                a_points += 4;
                std::cout << "Player A scores 4 point(s).\n";
            }
            else
            {
                b_points += 4;
                std::cout << "Player B scores 4 point(s).\n";
            }
        }
        if (cards[i] == "king" && no_high_card(i, 3) && i < 49)
        {
            if (turn)
            {
                a_points += 3;
                std::cout << "Player A scores 3 point(s).\n";
            }
            else
            {
                b_points += 3;
                std::cout << "Player B scores 3 point(s).\n";
            }
        }
        if (cards[i] == "queen" && no_high_card(i, 2) && i < 50)
        {
            if (turn)
            {
                a_points += 2;
                std::cout << "Player A scores 2 point(s).\n";
            }
            else
            {
                b_points += 2;
                std::cout << "Player B scores 2 point(s).\n";
            }
        }
        if (cards[i] == "jack" && no_high_card(i, 1) && i < 51)
        {
            if (turn)
            {
                a_points += 1;
                std::cout << "Player A scores 1 point(s).\n";
            }
            else
            {
                b_points += 1;
                std::cout << "Player B scores 1 point(s).\n";
            }
        }
        turn = !turn;
    }

    std::cout << "Player A: " << a_points << " point(s).\n";
    std::cout << "Player B: " << b_points << " point(s).\n";

    return 0;
}