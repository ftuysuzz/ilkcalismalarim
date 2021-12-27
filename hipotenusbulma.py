import time
print("Hipotenüs Bulma Aracına Hoşgeldiniz")

a = int(input("Birinci Kenar Uzunluğunu Giriniz"))
b = int(input("İkinci Kenar Uzunluğunu Giriniz"))

print("Hesaplanıyor...")
time.sleep(1)

print("Hipotenüs : {}".format((a ** 2 + b ** 2) ** 0.5))