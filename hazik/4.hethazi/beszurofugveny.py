from dataclasses import replace


def beszur(beszo, hely, txt):
    
    for i in range(len(txt)):
        if hely == txt[i]:
            return hely
    

def main():
    
    txt = "Az egy bögre"
    print(txt)
    
    beszo = input("Adja meg a beszúrni kívánt szavat: ")
    hely = input("Adja meg azt a szavat, ami elé kívánja beszurni a szavát: ")
    
    print(beszur(beszo, hely, txt))
    
    pass
    
if __name__ == "__main__":
    main()