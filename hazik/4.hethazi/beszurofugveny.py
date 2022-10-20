def beszur(szoveg, prameter, plusztxt):
    
    szöveg2 = []
    txt = szoveg.split(' ')
    
    for i in range(len(txt)):
        if txt[i] == prameter:
            szöveg2.append(plusztxt)
            szöveg2.append(prameter)
            
        else:
            szöveg2.append(txt[i])
    
    return szöveg2


def main():
    
    txt = input("Adjon meg egy kívánt szöveget: ")
    para = input("Adja meg azt a szót ami elé szót kíván beszúrni: ")
    ptxt = input("Beszurni kívánt szó: ")

    print(*beszur(txt, para, ptxt))

if __name__ == "__main__":
    main()