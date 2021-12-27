import time

print("Yol Ücreti Programına Hoşgeldiniz")

a = float(input("KM'de kaç yaktığını yazınız."))
b = int(input("Kaç KM yol gittiğinizi yazınız."))

print("Hesaplanıyor....")

time.sleep(2)

print("Ödemeniz Gereken Miktar: {}".format(a * b))