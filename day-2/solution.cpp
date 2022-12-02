#include <fstream>
#include <iostream>
#include <string>

int get_score_part_one(char opponent, char player)
{
    // Opponent: Rock A, Paper B, Scissors C
    // Us: Rock X, Paper Y, Scissors Z

    int points = 0;

    switch (player)
    {
    case 'X':
        points = 1;
        break;
    case 'Y':
        points = 2;
        break;
    case 'Z':
        points = 3;
        break;
    }

    if ((opponent == 'A' && player == 'X') || (opponent == 'B' && player == 'Y') || (opponent == 'C' && player == 'Z'))
        points += 3;
    else if ((opponent == 'A' && player == 'Y') || (opponent == 'B' && player == 'Z') || (opponent == 'C' && player == 'X'))
        points += 6;

    return points;
}

int get_score_part_two(char opponent, char player)
{
    // Opponent: Rock A, Paper B, Scissors C
    // Us: X lose, Y draw, Z win.

    int points = 0;

    switch (player)
    {
    case 'X':
        points = 0;

        if (opponent == 'A')
            points += 3;
        else if (opponent == 'B')
            points += 1;
        else
            points += 2;

        break;
    case 'Y':
        points = 3;

        if (opponent == 'A')
            points += 1;
        else if (opponent == 'B')
            points += 2;
        else
            points += 3;

        break;
    case 'Z':
        points = 6;

        if (opponent == 'A')
            points += 2;
        else if (opponent == 'B')
            points += 3;
        else
            points += 1;

        break;
    }

    return points;
}

void solve_part_one()
{
    std::string line;
    std::fstream file;
    int total1 = 0, total2 = 0;
    file.open("input.txt");

    while (std::getline(file, line))
    {
        char opponent = line.at(0), me = line.at(2);
        total1 += get_score_part_one(opponent, me);
        total2 += get_score_part_two(opponent, me);
    }

    std::cout << total1 << std::endl;
    std::cout << total2 << std::endl;

    file.close();
}

int main()
{
    solve_part_one();
    return 0;
}
