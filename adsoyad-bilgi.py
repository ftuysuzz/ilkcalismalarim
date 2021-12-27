#Ad Soyad Bilgi Formu
import time

print("Bilgi Formuna Hoşgeldiniz..")

a = input("Adınızı Giriniz")
b = input("Soyadınızı Giriniz")
c = int(input("Numaranızı Giriniz"))

print("Bilgiler Yazdırılıyor...")

time.sleep(1)

print("Adınız: {}\nSoyadınız: {}\nNumaranız: {}".format(a,b,c))