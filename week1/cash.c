#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int cents;
    // Negatif değer girmesini engelle
    do
    {
        cents = get_int("Change owed: ");
    }
    while (cents < 0);

    int coins = 0;

    // 25 kuruşluklar
    while (cents >= 25)
    {
        cents -= 25;
        coins++;
    }

    // 10 kuruşluklar
    while (cents >= 10)
    {
        cents -= 10;
        coins++;
    }

    // 5 kuruşluklar
    while (cents >= 5)
    {
        cents -= 5;
        coins++;
    }

    // 1 kuruşluklar
    while (cents >= 1)
    {
        cents -= 1;
        coins++;
    }

    // Toplam madeni para sayısını yazdır
    printf("%i\n", coins);
}