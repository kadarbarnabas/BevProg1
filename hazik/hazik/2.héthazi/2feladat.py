from cmath import pi
import math

def main():
    
    befogoA = int(input("Adja meg a derékszögű háromszög 'A' befogóját: "))
    befogoB = int(input("Adja meg a derékszögű hárömszög 'B' befogóját: "))
    
    atfogo = math.sqrt(befogoA*befogoA + befogoB*befogoB)
    
    print(f"Az átfogó átmérője {round(atfogo, 2)}")
    
    print()
    
    a = input("Ezzel a két befogóval akar tovább haladni (Igen/Nem): ")
    print()
    if a == "Igen":
        Aszög = math.acos(befogoB/atfogo) * (180 / pi)
        print(f"Az alfa szög nagysága {round(Aszög, 2)} fok")
        
        Bszög = math.acos(befogoA/atfogo) * (180 / pi)     
        print(f"A béta szög nagységa {round(Bszög, 2)} fok")
        
    elif a == "Nem":
        befogoA = int(input("Adja meg az új derékszögű háromszög 'A' befogóját: "))
        befogoB = int(input("Adja meg az új derékszögű háromszög 'B' befogóját: "))
        
        atfogo = math.sqrt(befogoA*befogoA + befogoB*befogoB)
        
        Aszög = math.acos(befogoB/atfogo) * (180 / pi)
        print(f"Az alfa szög nagysága {round(Aszög, 2)} fok")
        
        Bszög = math.acos(befogoA/atfogo) * (180 / pi)     
        print(f"A béta szög nagységa {round(Bszög, 2)} fok")
    
    else:
        print()
        print("Nem sikerült beírni hogy igen vagy nem ezért indísd újra a programot") 
        
    print()
    
    print("Adja meg a másodfokú megoldó képlet tagjait (ax^2 + bx + c = 0)")
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    
    D = b*b - 4 * a * c
    print(D)
    if D  < 0:
        print("Az egyenlet üres halmazt ad")
    else:
        c1 = (-b + math.sqrt(D)) / (2*a)
        c2 = (-b - math.sqrt(D)) / (2*a)
        
        print(f"Az első megoldás {round(c1, 2)}")
        print(f"A második megoldás {round(c2, 2)}")
        
    
if __name__ == "__main__":
    main()