#include <stdio.h>
#include <stdlib.h>

void put(char *signal, const char ch, int *length)
{
    signal[*length] = ch;
    *length += 1;
}

int isIn(char *signal, int length, char ch)
{
    for (int i = 0; i < length; i++)
    {
        if (signal[i] == ch)
            return i;
    }

    return -1;
}

void deleteFirst(char *signal, int *length, int count)
{
    for (int i = 0; i < *length - 1; i++)
        signal[i] = signal[i + count];
    *length -= count;
}

void printArray(char *array, int length)
{
    for (int i = 0; i < length; i++)
        printf("%c ", array[i]);
}

int firstMarker(FILE *file, char *signal, int len)
{
    int ch, length = 0, count = 0;

    while ((ch = fgetc(file)) != EOF && length < len)
    {
        count++;
        int index = isIn(signal, length, ch);
        if (index >= 0)
        {
            deleteFirst(signal, &length, index + 1);
            put(signal, ch, &length);
        }
        else
        {
            put(signal, ch, &length);
        }
    }

    return count;
}

int firstMarkerPacket(FILE *file)
{
    char *signal = (char *)malloc(4 * sizeof(char));
    return firstMarker(file, signal, 4);
}

int firstMarkerMessage(FILE *file)
{
    char *signal = (char *)malloc(14 * sizeof(char));
    return firstMarker(file, signal, 14);
}

int main()
{
    FILE *file = fopen("./input.txt", "r");
    printf("%d\n", firstMarkerPacket(file));
    fclose(file);

    file = fopen("./input.txt", "r");
    printf("%d\n", firstMarkerMessage(file));
    fclose(file);
    return 0;
}
