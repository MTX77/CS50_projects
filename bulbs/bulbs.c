#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    string message = get_string("Message: ");

    const int n = strlen(message);
    const int by_size = 8 * n;
    int pom_dec = 0;
    int count = 0;
    int count_print = 7;

    int bin_num[by_size];

    // Letter to dec to bin
    for (int i = 1; i <= n; i++)
    {
        pom_dec = (int) message[i - 1];

        for (int z = 0; z < 8; z++)
        {
            bin_num[count] = pom_dec % 2;
            pom_dec /= 2;
            count++;
        }

        count_print = (8 * i) - 1;

        // Printing
        for (int j = 0; j < 8; j++)
        {
            print_bulb(bin_num[count_print]);
            count_print--;
        }
        printf("\n");
    }
}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}
