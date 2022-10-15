def tukorszamvizsgalat(szam):
    
    szamjegyek0 = []
    szamjegyek1 = []
    
    for i in range(len(szam)):
        szamjegyek0.append(szam[i])
        szamjegyek1.append(szam[i])
        
    szamjegyek1.reverse()
    
    a = True
    szamlalo = 0
    
    while szamjegyek0[szamlalo] == szamjegyek1[szamlalo] and szamlalo == len(szam):
        a = True
        szamlalo += 1
        
    else:
        a = False
    
    return a

def main():
    szam = input("Adjon meg egy számot: ")
    
    if tukorszamvizsgalat(szam):
        print("A megadott szám tükörszám")
    else:
        print("A megadott szám nem tükörszám")
             
if __name__ == "__main__":
    main()