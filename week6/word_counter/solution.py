text = input("Bir cümle yazın: ").lower()
words = text.split()

# Kelime frekanslarını tutmak için sözlük (dictionary)
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Sonuçları yazdır
for word, count in word_count.items():
    print(f"{word}: {count}")
