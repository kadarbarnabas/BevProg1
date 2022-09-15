#Írj egy Python programot, amely bekér egy egész számot a felhasználótól és kiírja a képernyőre,
#hogy osztható-e (igen/nem) a szám 3-mal vagy 5-tel!
print("Adjon meg egy számot")
beszam = int(input())

b = beszam % 3
c = beszam % 5

if b == 0 and c == 0:
    print("A szám 3-al és 5-el is osztható")
else:
    if b == 0:
        print("A szám 3-al osztható")
    else:
        if c == 0:
            print("A szám 5-el osztható")
        else:
            print("A szám se 3-al se 5-el nem oszható")