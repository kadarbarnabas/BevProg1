def main():
    Na = int(input("Nátrium: "))
    Cl = int(input("Klór: "))
    
    NaCl = 0
    maradekNA = 0
    maradekCL = 0
    
    if Na == Cl*2:
        NaCl = Cl*2
    
    elif Na > Cl*2:
        maradekNA = Na - Cl*2
        NaCl = Cl*2
        
    elif Na < Cl*2:
        maradekCL = Cl*2 - Na
        NaCl = Na
        
    print(f"Létrejött konyhasó: {NaCl}\nmaradék klóratom: {maradekCL}\nmaradék nátriumatom: {maradekNA}")
    
if __name__ == "__main__":
    main()