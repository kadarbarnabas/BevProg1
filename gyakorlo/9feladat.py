#Írj egy Python programot, amely bekér két pozitív egész számot a felhasználótól és kiírja a
#képernyőre azokat a páros számokat, amelyek a két adott érték közötti zárt intervallumban
#találhatóak!

print("Adja meg az első számot")
a = int(input())
print("Adja meg a második számot")
b = int(input())

for i in range(a + 1, b, 1):
    if i % 2 == 0:
        print(i)
