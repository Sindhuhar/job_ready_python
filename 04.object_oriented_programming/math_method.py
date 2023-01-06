# Working with ststic methods.

class MathFormula:
    def pow(self,x,y):
        return x**y;

m = MathFormula()
print(m.pow(3,3))

#A Static Math Method
class MathFormula:
    @staticmethod
    def pow(x, y):
        return x ** y;


print(MathFormula.pow(3, 3))