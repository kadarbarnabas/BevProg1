def valid(text, chars="0123456789"):

    a = []
    for i in range(len(text)):
        
        for t in range(len(chars)):
            
            if text[i] == chars[t]:
                
                a.append(text[i])
                
    return a
        
    
                
def main():
    text = input("Adjon meg valamit: ")
    
    for i in range(len(valid(text))):
        print(valid(text)[i], end="")
    
if __name__ == "__main__":
    main()