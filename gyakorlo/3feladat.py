#Írj egy Python programot, amely bekér egy dolgozat pontszámot (x) a felhasználótól és kiír egy
#érdemjegyet az alábbiak szerint! 1: x<50; 2: 50<=x<60; 3: 60<=x<70; 4: 70<=x<85; 5: x>=85.

print("A dolgozat pontszáma")
x = int(input())

if x < 50:
    print(1)
if 50 <= x < 60:
    print(2)
if 60 <= x < 70:
    print(3)
if 70 <= x < 85:
    print(4)
if x > 85:
    print(5)