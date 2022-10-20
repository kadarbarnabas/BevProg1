class devs:
    def __init__(self, name, rank, years, pay) -> None:
        
        self.name = name
        self.rank = "Junior"
        self.years  = 0
        self.pay = pay
        
    def UpRisePay(self):
        
        i = True
        while i:
            b = input(f"\nAlapértelemezetten vagy az ön által kiszabott mennyiséggel akarja-e növelni {self.name} fizetését? (Alap/Kiszab): ")
            if b == "Alap":
                self.pay += 10000
                i = False
            elif b == "Kiszab":
                amount = int(input(f"\nMennyivel kívánja növelni {self.name} fizetését: "))
                self.pay += amount
                i = False
            else:
                print("\nHibás bevitel!")
    
    def YearS(self):
        self.years += 1
        
    def DevRank(self):
        if self.years == 0:
            self.rank = "Intern"
            
        if 1 <= self.years <= 2:
            self.rank = "Junior"
        
        if 2 <= self.years <= 5:
            self.rank = "Medior"
        
        if self.years > 5:
            self.rank = "Senior"
            
    def devdata(self):
        print(f"\nNév: {self.name}\nRang: {self.rank}\nÉvek: {self.years}\nFizetés: {self.pay}\n" )
            
def main():
    a1 = devs(name="Kádár Barnabás", rank="", years= 0, pay= 0)
    
    a1.UpRisePay()
    a1.YearS()
    a1.YearS()
    a1.YearS()
    a1.DevRank()
    
    a1.devdata()
    
if __name__ == "__main__":
     main()