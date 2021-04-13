#include <iostream>
#include <string>
#include <vector>

int main()
{
    std::cin.sync_with_stdio(0);
    std::cin.tie(0);

    std::string genotype_f;
    std::string genotype_m;
    short x;
    std::string phenotype;

    std::cin >> genotype_f;
    std::cin >> genotype_m;
    std::cin >> x;

    for (int i = 0; i < x; i++)
    {
        std::string output = "Possible baby.";
        std::cin >> phenotype;
        for (int letter = 0; letter < phenotype.length(); letter++)
        {
            if (islower(phenotype[letter]))
            {
                if ((isupper(genotype_f[letter * 2]) && isupper(genotype_f[letter * 2 + 1])) ||
                    (isupper(genotype_m[letter * 2]) && isupper(genotype_m[letter * 2 + 1])))
                {
                    output = "Not their baby!";
                }
            }

            if (isupper(phenotype[letter]))
            {
                if (islower(genotype_f[letter * 2]) && islower(genotype_f[letter * 2 + 1]) &&
                    islower(genotype_m[letter * 2]) && islower(genotype_m[letter * 2 + 1]))
                {
                    output = "Not their baby!";
                }
            }
        }
        std::cout << output << '\n';
    }

    return 0;
}