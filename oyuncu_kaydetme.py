import time

print("Oyuncu Kaydetme Programına Hoşgeldiniz")
time.sleep(2)
ad = input("Oyuncunun Adı")
soyad = input("Oyuncunun Soyadı")
takım = input("Oyuncunun Takımı")

bilgiler = [ad,soyad,takım]


print("Bilgiler Kaydediliyor.....")
time.sleep(2)
print("Oyuncu Adı : {}\nOyuncu Soyadı : {}\nOyuncu Takımı: {}".format(bilgiler[0],bilgiler[1],bilgiler[2]))

print("Bilgiler Kaydedildi....")