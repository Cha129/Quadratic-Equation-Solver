#Quadratic Equations solver
import math
a=int(input("Enter the coefficient of x^2:"))
b=int(input("Enter the coefficient of x:"))
c=int(input("Enter the constant:"))
print("The of Quadratic Equation {}x^2+{}x+{}".format(a,b,c))
def Quadratic_Equation_Solver(a,b,c):
    discriminant=b**2 - (4)*a*c
    if discriminant>0:
        print("The roots of the Quadratic Equation is real")
        root_1=(-b+math.sqrt(discriminant))/((2)*a)
        root_2=(-b-math.sqrt(discriminant))/((2)*a)
        print("The of Quadratic Equation {}x^2+{}x+{} is {} and {}".format(a,b,c,root_1,root_2))
    elif discriminant==0:
        print("The roots of the Quadratic Equation are real and also equal")
        roots=(-b+math.sqrt(discriminant))/((2)*a)
        print("The of Quadratic Equation {}x^2+{}x+{} is {}".format(a,b,c,roots))
    elif discriminant<0:
        print("The roots of quadratic equations are imaginary since the discriminant is {} which is negative".format(discriminant))

Quadratic_Equation_Solver(a,b,c)










        


        

