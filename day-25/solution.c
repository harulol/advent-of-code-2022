#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void reverse(char *string)
{
    int left = 0;
    int right = strlen(string) - 1;
    while (left < right)
    {
        char temp = string[left];
        string[left] = string[right];
        string[right] = temp;

        left++;
        right--;
    }
}

int value(char snafu)
{
    switch (snafu)
    {
    case '1':
        return 1;
    case '2':
        return 2;
    case '0':
        return 0;
    case '-':
        return -1;
    case '=':
        return -2;
    }

    return 0;
}

long long int to_decimal(const char *snafu)
{
    long long int power = 1;
    long long int total = 0;

    for (int i = strlen(snafu) - 1; i >= 0; i--)
    {
        total += value(snafu[i]) * power;
        power *= 5;
    }

    printf("Converted %s to %d.\n", snafu, total);
    return total;
}

char *to_snafu(long long int decimal)
{
    char *snafu = (char *)malloc(100 * sizeof(char));
    strcpy(snafu, "");

    while (decimal != 0)
    {
        int remainder = decimal % 5;
        decimal /= 5;

        char num[10];
        switch (remainder)
        {
        case 0:
        case 1:
        case 2:
            itoa(remainder, num, 10);
            strcat(snafu, num);
            break;
        case 3:
            strcat(snafu, "=");
            decimal++;
            break;
        case 4:
            strcat(snafu, "-");
            decimal++;
            break;
        }
    }

    reverse(snafu);
    return snafu;
}

void solve_part_one()
{
    FILE *fp = fopen("./input.txt", "r");
    char line[256];

    long long int total = 0;

    while (fgets(line, 256, fp) != NULL)
    {
        line[strcspn(line, "\n")] = 0;
        total += to_decimal(line);
    }

    fclose(fp);
    printf("%llu\n", total);

    char *snafu = to_snafu(total);
    printf("%s\n", snafu);
}

int main()
{
    solve_part_one();
    return 0;
}
