import random

# 1 ile 100 arasında rastgele bir sayı tut
number = random.randint(1, 100)
guess = 0

print("1 ile 100 arasında bir sayı tuttum. Tahmin et!")

# Doğru tahmin edene kadar dön
while guess != number:
    guess = int(input("Tahminin: "))
    
    if guess < number:
        print("Daha yüksek!")
    elif guess > number:
        print("Daha düşük!")
    else:
        print(f"Tebrikler! Doğru sayı {number} idi.")
