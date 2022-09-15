#Írj egy Python programot, amely bekér egy pozitív egész számot a felhasználótól és kiírja a
#képernyőre azt a számot, amely az ennél a számnál nem nagyobb pozitív egész számok
#összege!

print("Adjon meg egy pozitív egész számot")
a = int(input())

szamlalo = 0

for i in range (a + 1):
    szamlalo = szamlalo + i

print(szamlalo)