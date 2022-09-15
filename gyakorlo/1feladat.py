#Írj egy Python programot, amely bekér három számot a felhasználótól és kiírja a képernyőre a
#legkisebb értéket ezek közül!

a = []

for i in range(3):
    print(f"{i + 1}. szám")
    b = int(input())
    a.append(b)

#a.sort()
#print(f"{a[0]} a legkisebb szám")

index = 0
legkisebb = a[0]
for i in range(3):
    b = a[i]
    if legkisebb > b:
        index = b
        legkisebb = index


print(f"{legkisebb} a legkisebb szám")