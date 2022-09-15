#Írj egy Python programot, amely bekér három számot a felhasználótól és kiírja a képernyőre,
#hogy a számok közül bármelyik kettőnek az összege egyenlő-e a harmadik számmal!

a = []

for i in range(3):
    print(f"Adja meg a {i + 1}. számot")
    a.append(int(input()))

if a[0] + a[1] == a[2]:
    print("Az 1. és a 2. szám összege egyenlő a 3. számmal")
else:
    if a[0] + a[2] == a[1]:
        print("Az 1. és a 3. szám összege egyenlő a 2. számmal")
    else:
        if a[1] + a[2] == a[0]:
            print("Az 2. és a 3. szám összege egyenlő az 1. számmal")
        else:
            print("Két bármely szám összege nem egyenlő a maradék számmal")