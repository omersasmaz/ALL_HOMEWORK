#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height;
    // 1 ile 8 arasında geçerli bir sayı alana kadar sor
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);

    // Her satır için bir döngü
    for (int i = 0; i < height; i++)
    {
        // Boşlukları yazdır (Hizalama için)
        for (int j = 0; j < height - i - 1; j++)
        {
            printf(" ");
        }
        // Diyezleri (#) yazdır
        for (int k = 0; k < i + 1; k++)
        {
            printf("#");
        }
        // Bir alt satıra geç
        printf("\n");
    }
}