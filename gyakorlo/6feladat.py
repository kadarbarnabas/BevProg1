#Írj egy Python programot, amely bekér három egész számot a felhasználótól és kiírja a
#képernyőre, hogy mind a három páros szám-e (igen/nem)!

a = []

for i in range(3):
    print(f"Adja meg a {i + 1}. számot")
    b = int(input())
    if b % 2 == 0:
        a.append(0)
    else:
        a.append(1)

b = True
for i in range(len(a)):
    if a[i] != 0:
        b = False
        break

c = True
for i in range(len(a)):
    if a[i] != 1:
        c = False
        break


if c:
    print("Mind háromn szám páratlan")
else:
    if b:
        print("Mind három szám páros")
    else:
        for i in range(len(a)):
            if a[i] == 1:
                print(f"A {i + 1}. szám páratlan")
            else:
                print(f"A {i + 1}. szám páros")


