#include <iostream>
#include <string>
#include <vector>

int main()
{
    std::cin.sync_with_stdio(0);
    std::cin.tie(0);

    int n;
    int n_subjects;
    int n_verbs;
    int n_objects;

    std::vector<std::string> subjects;
    std::vector<std::string> verbs;
    std::vector<std::string> objects;

    std::cin >> n;

    std::string input;
    for (int i = 0; i < n; i++)
    {
        subjects.clear();
        verbs.clear();
        objects.clear();
        std::cin >> n_subjects;
        std::cin >> n_verbs;
        std::cin >> n_objects;
        std::cin.ignore();
        for (int j = 0; j < n_subjects; j++)
        {
            std::getline(std::cin, input);
            subjects.push_back(input);
        }
        for (int j = 0; j < n_verbs; j++)
        {
            std::getline(std::cin, input);
            verbs.push_back(input);
        }
        for (int j = 0; j < n_objects; j++)
        {
            std::getline(std::cin, input);
            objects.push_back(input);
        }
        for (int j = 0; j < subjects.size(); j++)
        {
           // std::cout << subjects[j] << '\n';
            for (int k = 0; k < verbs.size(); k++)
            {
                for (int l = 0; l < objects.size(); l++)
                {
                    std::cout << subjects[j] << " " << verbs[k] << " " << objects[l] << ".\n";
                }
            }
        }
    }
    return 0;
}