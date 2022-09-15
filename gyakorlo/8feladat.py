#Írj egy Python programot, amely bekér egy pozitív egész számot a felhasználótól és kiírja a
#képernyőre azokat a pozitív hárommal osztható számokat, amelyek kisebbek az adott számnál!

print("Adjon meg egy pozitív egész számot")
a = int(input())

for i in range(a, 0, -1):
    if i % 3 == 0:
        print(i)