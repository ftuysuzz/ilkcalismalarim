import time
"""
İkinci Dereceden ax^2 + bx + c denkleminin kök bulma programıdır.
"""

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

print("Delta Hesaplanıyor.....")

delta = b ** 2 - 4 * a * c

x1 = (-b - delta ** 0.5) / (2 * a)
x2 = (-b + delta ** 0.5) / (2 * a)
time.sleep(2)

print("Birinci Kök : {}\nİkinci Kök : {}".format(x1,x2))