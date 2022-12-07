def main():
    pages = input("Adja meg az oldalakat: ")
    
    x = pages.split(",")
    li = []
    for i in range(len(x)):
        x2 = x[i].split("-")
        
        if len(x2) == 2:
            for k in range(int(x2[0]), int(x2[1]) + 1):
                li.append(k)
        else:
            li.append(int(x2[0]))
    
    li.sort()               
    print(li)
    
if __name__ == "__main__":
    main()