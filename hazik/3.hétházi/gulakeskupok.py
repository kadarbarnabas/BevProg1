from cmath import pi

def teglalapT(a,b):
    
    teglalapTer = a * b
    
    return teglalapTer

def körT(r):
    
    körTer = r * pi * pi
    
    return  körTer


def main():   
    
    a = float(input("Adja meg a téglalap A oldalát: "))
    b = float(input("Adja meg a téglalap B oldalát: "))   
    print(f"{teglalapT(a, b)} egységnyi a téglalap területe")
    
    r = float(input("Adja meg a kör sugarát: "))
    print(f"{round(körT(r), 2)} egységnyi a kör terüle")
    
    m = float(input("Adjon meg egy magasságot: "))
    gV = (teglalapT(a, b) * m) / float(3)
    
    kV = (körT(r) * m) / float(3)
    
    print(f"A(z) {m} egységnyi magas gúlának {round(gV, 2)} egysényi a térfogata")
    print(f"A(z) {m} egységnyi magas kúpnak {round(kV, 2)} egysényi a térfogata")
if __name__ == '__main__':
    main()