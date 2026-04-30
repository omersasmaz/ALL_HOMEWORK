import csv

# Örnek bir CSV okuma işlemi (Örn: isimler.csv)
counts = {}

try:
    with open("names.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # 'home' sütunundaki verileri sayalım
            home = row["home"]
            if home in counts:
                counts[home] += 1
            else:
                counts[home] = 1

    for home in sorted(counts):
        print(f"{home}: {counts[home]}")
except FileNotFoundError:
    print("Hata: names.csv dosyası bulunamadı.")
