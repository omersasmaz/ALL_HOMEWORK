import csv

students = []

try:
    with open("students.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({"name": row["name"], "house": row["house"]})

    # İsimlere göre alfabetik sıralama (Lambda kullanarak)
    for student in sorted(students, key=lambda student: student["name"]):
        print(f"{student['name']} is in {student['house']}")
except FileNotFoundError:
    print("Hata: students.csv bulunamadı.")
