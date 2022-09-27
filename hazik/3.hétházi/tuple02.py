import math


def distance(p1, p2):
    
    tav = math.sqrt(pow(p2[0] - p1[0], 2) + pow(p2[1] - p1[1], 2))
    
    return tav


def main():
    p1 = (1, 2)
    p2 = (6, 5)
    print('A ket pont kozti tavolsag:', distance(p1, p2))

#############################################################################

if __name__ == "__main__":
    main()