#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Kullanıcıdan isim istiyoruz
    string name = get_string("What is your name? ");
    
    // İsmi ekrana selam vererek yazdırıyoruz
    printf("hello, %s\n", name);
}