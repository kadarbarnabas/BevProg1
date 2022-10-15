def main():
    eletkor = int(input("Adjon meg egy életkort: "))
    
    print("Fogyaszthat-e legálisan alkoholt Amerikában?")
    if eletkor >= 21:
        print("Igen fogyaszthat")
    else:
        print("Nem fogyaszthat")
    print()
    
    print("Vásárolhat-e dohányterméket Magyarországon?")
    if eletkor >= 18:
        print("Igen vásárolhat")
    else:
        print("Nem vásárolhat")
    print()
    
    print("Szerezhet-e jogosítványt?")
    if eletkor >= 16:
        print("Igen szerezhet")
    else:
        print("Nem szerezhet")
    print()
    
    print("Megnézheti-e egyedül a Shrek 2-t")
    if eletkor >= 12:
        print("Igen megnézheti")
    else:
        print("Nem nemnézheti(godnolom)")
    print()
    
    
if __name__ == "__main__":
    main()