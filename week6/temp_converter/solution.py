# Kullanıcıdan Celsius değerini al
celsius = float(input("Celsius: "))

# Fahrenheit hesapla: (C * 9/5) + 32
fahrenheit = (celsius * 9/5) + 32

# f-string kullanarak ekrana yazdır
print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
