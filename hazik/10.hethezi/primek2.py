from primek import is_prime as p

i = 2
while i <= 100:
    if p(i):
        print(i)
    i += 1