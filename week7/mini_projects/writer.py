import csv

name = input("Name: ")
home = input("Home: ")

# 'a' (append) modu ile dosyanın sonuna ekleme yapıyoruz
with open("names.csv", "a", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    # Eğer dosya boşsa başlık eklemek gerekebilir (isteğe bağlı)
    writer.writerow({"name": name, "home": home})

print("Başarıyla kaydedildi.")
