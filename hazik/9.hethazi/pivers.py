def main():
    txt = open("pi.txt", 'r')
    lyrics = txt.readlines()
    txt.close
    
    txt = open("pi2.txt", 'w')
    print(lyrics[0], file=txt)
    txt.close
    
if __name__ == "__main__":
    main()