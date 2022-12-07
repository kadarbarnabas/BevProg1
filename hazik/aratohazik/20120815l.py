def fordito():
    txt = open("szoveg.txt", 'r')
    szoveg = txt.readlines()
    print(szoveg)
    
    li = []
    for i in range(len(szoveg)):
        for n in range(len(szoveg[i])):
            if 88 >= ord(szoveg[i][n]) >= 65 or 120 >= ord(szoveg[i][n]) >= 97:
                ascii = ord(szoveg[i][n])
                ascii2 = ascii + 2
                li.append(chr(ascii2))
            
            if ord(szoveg[i][n]) == 90:
                ascii = 65
                ascii2 = ascii + 1
                li.append(chr(ascii2))
                
            if ord(szoveg[i][n]) == 89:
                ascii = 65
                ascii2 = ascii + 0
                li.append(chr(ascii2))
            
            if ord(szoveg[i][n]) == 122:
                ascii = 97
                ascii2 = ascii + 1
                li.append(chr(ascii2))
                
            if ord(szoveg[i][n]) == 121:
                ascii = 97
                ascii2 = ascii + 0
                li.append(chr(ascii2))
            
            if szoveg[i][n] == '\n':
                li.append('\n')
            
            if szoveg[i][n] == ' ':
                li.append(' ')
                
    txt.close
    print(*li, sep='')
    
fordito()