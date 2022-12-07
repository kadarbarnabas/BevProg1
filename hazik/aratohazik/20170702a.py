import random

def main():
    r = random.randint(1, 100)
    print(r)
    
    while True:
        tipp = int(input("your guess> "))
        
        if tipp < r:
            print("my number is larger")
        if tipp > r:
            print("my number is smaller")
        if tipp == r:
            print("Good job! That's it!")
            break
    
if __name__ == "__main__":
    main()