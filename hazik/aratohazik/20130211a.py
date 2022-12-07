def main():
    word1 = input("Adjon meg egy szót: ")
    word2 = input("Adja meg a második szót: ")
    
    word1l = []
    word2r = []
    for i in range(len(word2)):
        if word1[i] != " " or word2[i] != " ":
            word1l.append(word1[i].lower())
            word2r.append(word2[i].lower())
        
    word2r.reverse()
    
    anagramma = True
    
    if word1l != word2r:
        anagramma = False
    
    if anagramma:
        print("Ez anagramma")
    else:
        print("Ez nem anagramma")
    
    
    
if __name__ == "__main__":
    main()