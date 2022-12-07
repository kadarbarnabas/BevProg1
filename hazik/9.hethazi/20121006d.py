def main():
    file = open("string1.py", 'r', encoding='UTF-8')
    file2 = open("string1_clean.py", 'w')
    txt = file.readlines()
    for i in range(len(txt)):
        if txt[i][0] != "#" and txt[i] != "\n" and txt[i][0] != '\t#':
                print(txt[i], file=file2, end="")
        
    file.close
    file2.close
        

if __name__ == "__main__":
    main()