#Írj egy Python programot, amely bekér egy 20-nál nem nagyobb pozitív egész számot a
#felhasználótól és kiírja a képernyőre a START szót úgy, hogy előtte annyi szóköz legyen amennyi
#a megadott szám értéke!

print("Adjon meg egy 20-nál kisebb számot")
x = int(input())

while(x > 20):
    print("Próbáld meg ujra")
    print("Adj meg egy 20-nál kisebb számot!")
    x = int(input())

for i in range(x):
    print(" ", end="")
    if i == x - 1:
        print("START")