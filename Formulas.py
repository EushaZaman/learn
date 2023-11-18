'''
The porpouse of the Formulas module is to provide formulas for common and every day occurrences and mathematical procedures
'''
class ImaginaryNumError(BaseException):
    pass
import math


def quadratic(a=0,b=0,c=0):
    '''
   This functions returns the one or more answers that the quadratic formula could possibly have for your variables
   (a,b,c) and inserts them into the quadratic formula which would be 0=-b(+,-) the square of ((b^2)-(4*a*c))/(2*a)
   NOTE:In the case that an imaginary coeficient is square rooted, it will print the actual square root in the long form
   (I.E sqrt of 7 would be printed as 2.6457513110645907); The default values of the funtction will always equal to 0 and
    the function will remind you of it
    '''
    BOT = 2*a
    INT = (b**2)-(4*a*c)
    if a ==0 and b==0 and c== 0:
        return "All values are equal to 0 or are not set and therefore defeults to default value 0"
    if BOT == 0:
        return 0
    if INT < 0:
        INT = math.sqrt(math.fabs(float((b**2)-(4*a*c))))
        INK1 = -b/BOT
        INK2 = INT/BOT
        return f"{INK1}±i{INK2}"
    else:
        INT = math.sqrt((b**2)-(4*a*c))
        return (f"{(((-b)+(INT))/BOT)},{(((-b)-(INT))/BOT)}")





    #This preforms the quadratic formula
def pythagorean(a=0,b=0):
    '''
    This function does the pythagorean theorum for you
    '''
    insqrt = (a ** 2) + (b ** 2)
    try:
        insqrt
        if insqrt < 0:
            raise ImaginaryNumError
            insqrt *= -1
    except ImaginaryNumError:
        print(f"a squared({a**2}) and b squared({b**2}) added together makes a negative number({insqrt}) and thus cannot be square rooted")
    finally:
        return f"The hypotenuse(c) is {math.sqrt(insqrt)}"

'''
print(pythagorean(2,2))
print(pythagorean.__doc__)
print(quadratic(1,2,3))
print(quadratic.__doc__)

'''
#print(quadratic(1,4,5))

