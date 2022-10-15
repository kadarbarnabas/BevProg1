from audioop import reverse
from math import floor


def main():
    decimalisszam = int(input("Adjon meg egy tetszőleges számot: "))
    
    binarisszam = []
    while decimalisszam != 0:
        
        #Azért floor mert ezáltal lefele kerekítek és vannak olyan esetek 
        #hogy ha felfele kerekítenék akkor azt az egy maradékot kikéne vonnom az eredményből
        #és ügye abba az estbe ha 0 lenne maradék viszont nem vonhatom ki a maradékot
        #az eredményből
        
        binarisszam.append(decimalisszam % 2)
        decimalisszam = floor(decimalisszam / 2)
      
    for i in range(len(binarisszam) - 1, -1, -1):
        print(binarisszam[i], end="")
    
    
if __name__ == "__main__":
    main()