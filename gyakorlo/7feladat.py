#Írj egy Python programot, amely bekér két szót (sztringet) a felhasználótól és ABC sorrendben
#kiírja őket a képernyőre!

a = []

for i in range(2):
    print(f"Adja meg a {i + 1}. szót")
    a.append(input())

a.sort()
for i in range(len(a)):
    print(a[i])