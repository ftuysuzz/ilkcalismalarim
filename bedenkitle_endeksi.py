import time
print("Beden Kitle Endeksi Bulma Programına Hoşgeldiniz")

boy = float(input("Boyunuzu Giriniz (m)"))
kilo = int(input("Kilonuzu Giriniz"))

print("Hesaplanıyor......")

time.sleep(2)

print("Vücüt Kitle Endeksiniz : {}".format((kilo) / (boy * boy)))
