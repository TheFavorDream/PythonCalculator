
class ComputeEngine:
    def __init__(self):
        self.OperatorOrder = ["^", "/", "x"]

    #Checks if the Equation is valid or not. True if Valid and False if not.
    def CheckGrammer(self, Equation:str):
        
        Parantesis = 0
        for i in Equation:
            if i == "(" or i == ")":
                Parantesis += 1

        if Parantesis % 2 != 0:
            print("Incorrect Number of Parantesis")
            return False
        
        return [Parantesis//2]


    def AddPlusSign(self, Text:str):
        
        Equation = ""

        for i in Text:
            if i == "-":
                Equation += "+-"
            else:
                Equation += i

        return Equation

    def RemoveAll(self, OperatorList:list, Item:str):
        for i in OperatorList:
            if i == Item:
                OperatorList.remove(i)
        return OperatorList

    def ComputeTerm(self, Term:str):

        Sum = 0
        Content = self.__Extract(Term)
        x = 0
        for i in self.OperatorOrder:
            for j in range(0, len(Content[1])):
                if i == Content[1][j-x]:
                    Num1 = Content[0][j-x]
                    Num2 = Content[0][j+1-x]

                    if i == "^":
                        Sum = Num1 ** Num2
                    elif i == "/":
                        Sum = Num1 / Num2
                    elif i == "x":
                        Sum = Num1 * Num2

                    Content[0][j-x] = Sum
                    Content[0].remove(Num2)
                    x += 1
            Content[1] = self.RemoveAll(Content[1], i)
                    
                    

        return Content[0][0]

    #Extarcts the Equation Into Terms
    def __Extract(self, SubEquation:str):
        
        SubEquation += "t"

        Nums = []
        Operators = []
        IsFloat = False
        Digit = ""

        for i in SubEquation:
            if i == "^" or i == "x" or i == "/" or i == "t":
                if IsFloat:
                    Nums.append(float(Digit))
                else:
                    Nums.append(int(Digit))
                Operators.append(i)
                Digit = ""
                IsFloat = False
            else:
                if i == ".":
                    IsFloat = True
                Digit += i

        Operators.pop()

        return [Nums, Operators]

    def SumUp(self, List):
        Sum = 0
        for i in List:
            Sum+=i
        return Sum


    def Calculate(self, Equation:str):

        Terms = self.AddPlusSign(Equation).split("+")

        Values = []
        for i in Terms:
            Values.append(self.ComputeTerm(i))

        return  str(self.SumUp(Values))
                






        



    

if __name__ == "__main__":
    print ("ComputerEngine.py is not executable.")
