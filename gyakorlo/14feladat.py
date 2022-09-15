#Írj egy Python programot, amely először bekér egy kisebb majd egy nagyobb pozitív valós
#számot a felhasználótól és kiírja a képernyőre azokat az egész számokat, amelyek a megadott
#értékek között helyezkednek el!
import math

print("Adjon meg az 1. valós számot")
a = float(input())
print("Adja meg a 2. valós számot")
b = float(input())

a1 = math.floor(a)
b1 = math.floor(b)

for i in range(a1, b1 + 1, 1):
    print(i)