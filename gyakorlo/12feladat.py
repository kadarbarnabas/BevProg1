#Írj egy Python programot, amely bekér egy szót (sztringet) a felhasználótól és kiírja a
#képernyőre a szó betűit, úgy, hogy minden betű egy új sorba kerüljön!

print("Adjon meg egy szót")
a = input()

for i in range(len(a)):
    print(a[i])
