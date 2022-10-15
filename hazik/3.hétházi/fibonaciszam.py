def main():
    
    nszam = int(input("Adja meg a Fibonaci sorozat n-edik tagját: "))
    fibo = [1, 1]
    
    i = 0
    while i != nszam - 2:
        index = fibo[i] + fibo[i + 1]
        fibo.append(index)
        i += 1
        
    print(f"A Fibonaci szám sorozat n-edik tagja : {fibo[-1]}")

if __name__ == "__main__":
    main()