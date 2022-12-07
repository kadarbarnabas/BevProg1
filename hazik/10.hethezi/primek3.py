from primek import is_prime as p

i = 2
index = 0
while i <= 200:
    if p(i):
        index += i
    i += 1
    
print(index)