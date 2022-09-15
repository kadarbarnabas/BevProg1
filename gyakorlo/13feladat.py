#Írj egy Python programot, amely bekér egy pozitív egész számot a felhasználótól és kiírja a
#képernyőre felváltva a 0 és 1 számjegyeket úgy, hogy a számjegyek együttes darabszáma
#pontosan a megadott szám legyen!

print("Adjon meg egy pozitív egész számot")
a = int(input())

for i in range(a):
    if i % 2 == 0:
        print("0", end="")
    else:
        print("1", end="")