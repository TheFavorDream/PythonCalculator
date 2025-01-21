class Compiler:
    def __init__(self):
        self.NumberBase = 10
        self.__String = ""

    def GrammerCheck(self):
        Num = 0
        for i in self.__String:
            if i == "(" or i == ")":
                Num += 1
        if Num % 2 != 0:
            print("Wrong Equation")
            return False
        return True
    
    def SetString(self, String):
        self.__String = String
        return
    
    def Calculate(self, Display):
        self.__String += "t"

        Nums = []
        Tmp = ""
        IsFloat = False
        for i in self.__String:
            if i == "+" or i == "-" or i == "x" or i == "/" or i == "t":
                if IsFloat:
                    Nums.append(float(Tmp))
                else:
                    Nums.append(int(Tmp))
                Tmp = ""
                IsFloat = False

            else:
                if i == ".":
                    IsFloat = True
                Tmp += i
        print(Nums)

    
        
        
    
if __name__ == "__main__":
    print("You Cannot Run this File!. Run Calculator.py instead.")