# Not listesi
grades = [85, 92, 78, 90, 88]

# Ortalama hesapla
total = sum(grades)
average = total / len(grades)

# Harf notu belirle
if average >= 90:
    letter = 'A'
elif average >= 80:
    letter = 'B'
elif average >= 70:
    letter = 'C'
else:
    letter = 'F'

print(f"Ortalama: {average}, Harf Notu: {letter}")
