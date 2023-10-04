#include <cs50.h>
#include <math.h>
#include <stdio.h>

bool valid(long number);
void which_bank(long number);

int main(void)
{
    long number = 0;

    do
    {
        number = get_long("Number: ");
    }
    while (number <= 0);

    if (valid(number))
    {
        which_bank(number);
    }
    else
    {
        printf("INVALID\n");
    }
}

bool valid(long number)
{
    int nDigits = floor(log10(number)) + 1;
    long number_add = 0;
    long number_second = 0;
    long sum = 0;

    for (int i = 1; i <= nDigits; i++)
    {
        number_add = number % (long) pow(10, i);
        number_second = number_add / pow(10, i - 1);

        if (i % 2 == 0)
        {
            number_second *= 2;

            if (number_second >= 10)
            {
                sum += (number_second / 10 + number_second % 10);
            }
            else
            {
                sum += number_second;
            }
        }
        else
        {
            sum += number_second;
        }
    }

    if (sum % 10 == 0)
        return true;
    else
        return 0;
}

void which_bank(long number)
{
    int nDigits = floor(log10(number)) + 1;
    int two_fd = number / (long) pow(10, nDigits - 2);
    int first_d = number / (long) pow(10, nDigits - 1);

    if (nDigits == 15 && (two_fd == 34 || two_fd == 37))
    {
        printf("AMEX\n");
    }
    else if (nDigits == 16 && (two_fd == 51 || two_fd == 52 || two_fd == 53 || two_fd == 54 || two_fd == 55))
    {
        printf("MASTERCARD\n");
    }
    else if ((nDigits == 13 || nDigits == 16) && first_d == 4)
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
    }
}