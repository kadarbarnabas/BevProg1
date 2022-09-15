#Írj egy Python programot, amely bekér három számot a felhasználótól és kiírja a képernyőre a
#legnagyobb értéket ezek közül!

a = []

for i in range(3):
    print(f"{i + 1}. szám")
    b = int(input())
    a.append(b)

#a.sort()
#print(f"{a[len(a) - 1]} a legnagyobb szám")

index = 0
legnagyobb = a[0]
for i in range(3):
    b = a[i]
    if legnagyobb < b:
        index = b
        legnagyobb = index


print(f"{legnagyobb} a legnagyobb szám")