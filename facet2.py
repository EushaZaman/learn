#2
'''
import sys
print(sys.version)
'''

#3
'''
import datetime
print(datetime.datetime.today())'''
#4
'''
def area(radius):
    return (3.14 * radius) ** 2

print(area(25))'''
#5
'''
first1 = input("What is your first name?")
last1 = input("What is your last name?")
def printy(first, last):
    name = first + " " + last
    return name[::-1]
print(printy(first1, last1))
'''
#6
'''
numlist = []

for what in range(5):
    numlist.append(input("type in a random number"))
print(numlist)
print(tuple(numlist))'''
#8
'''
color_list = ["Red","Green","White" ,"Black"]
print(color_list[0] + color_list[-1])'''
#10
'''
def multithree(iny):
    return iny + (iny **2) + (iny **3)
print(multithree(2))'''
#15
'''
def spherevolume(radius):
    return (4/3 * 3.14 * radius) ** 3
print(spherevolume(6))'''
#16
'''
def randy(number):
    if number > 17:
        return (abs(number) - 17) * 2
    else:
        return number - 17
print(randy(16))
'''
#17
'''
number = int(input("insert a number"))
if 900<=number<=1000 or 1000<=number<=1100 or 1900<=number<=2000 or 2000<=number<=2100:
    print("within")
else:
    print("not in range")'''
#18
'''
num1 = int(input("Give me a number"))
num2 = int(input("Give me a number"))
num3 = int(input("Give me a number"))
if num2 and num3 and num1 == num3 and num2 and num1:
    print(str(num1 ** 3))
else:
    print(str(num1 + num2 + num3))
'''
#21
'''
number = int(input("give me a number"))
if number % 2 == 1:
    print("Number is odd")
if number % 2 == 0:
    print("Number is even")'''
#24
'''
vowels = ["a", "e", "i", "o", "u", "y"]
def vowelcheck(letter):
    if letter in vowels:
        return "letter is a vowel"
    else:
       return "letter is a consenent"
print(vowelcheck("a"))
'''
#25
'''
list1 = range(10)
list2 = range(11,20)
def listcheck(number):
    if number in list1:
        return "number is in list 1"
    if number in list2:
        return "number is in list 2"
    else:
        return "number is not in any of the lists"
print(listcheck(1))'''
#27#Go over this
'''
list = ["I"," ","h","a","v","e"," ","2"," ","d","o","g","s","."]
theword = ""
for letter in list:
    theword += letter
print(theword)
#28'''
'''
numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958,743, 527
    ]
for number in numbers:
    if number == 412:
        break
    elif number % 2 == 0:
        print(f"{number}")
    else:
        pass'''
#2
'''
import sys
print(sys.version)

class Person:
    def __init__(self, name):
        self.name = name
    def say(self):
        print("hello")


fred = Person("Fred")
print(fred.name)
print(fred.say())'''
#3
'''
import datetime
print(datetime.datetime.now())
'''
#7
'''
filename = input("enter file name")
dot_position = filename.rfind(".")
if dot_position == -1:
    print("This file name has no exstention")
print(filename[dot_position + 1:])'''
#11
'''
def addup(a, b):
    """
    adds up
    """
    pass
print(addup.__doc__)'''
#19
'''
thestring = input("Insert a string here")
if "ls" == thestring[0:2]:
     print(thestring)
else:
    print(f"ls{thestring} ls has been added")
'''
#29
'''
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
for color in color_list_1:
    if color not in color_list_2:
        print(color)
    else:
        pass'''
#30
'''
def triangle_area(base,height):
    
    #finds the area of a triangle when the user inputs a base and height.
    
    return (base * height)/2
print(triangle_area(1,2))
print(triangle_area.__doc__)'''
#33

'''def intsum(list):

    #Adds up any amount of integers but if there more than one of the same integer the value will return to 0

    value = 0
    for number in list:
        if list.count(number) > 1 :
            return 0
        else:
            value += number
    return value
harvey = [1,1,1]
print(intsum(harvey))
print(intsum.__doc__)'''
#34
'''
def return20sum(a,b):
    value = a + b
    if 15<=value<=20:
        return 20
    else:
        return value
print(return20sum(1,2))
print(return20sum(6,110))'''
#36
'''
def addintsonly(a,b):
    if type(a) and type(b) is int:
        return a + b
    else:
        return "can only add integers"
print(addintsonly(1,2))
print(addintsonly(1,"hello"))'''
#37
'''
name = "Eusha"
age = "15"
address = "2 thingy road"
print(f"{name}\n{age}\n{address}")'''
#38
'''
def addmultiply(x,y):
    return (x+y)**2
print(addmultiply(4,3))'''
#39
'''
def interest(amount, int,years):
    return amount +((amount/(int/100))*years)
    
    takes a amount a rate of interest and a amount of years and calcualtes the final amount.
    
print(interest(10000,3.50,7))'''
#40
'''
import math
p1 = [4, 0]
p2 = [6, 6]
distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )


print(distance)'''
#49
'''
import blank
print(blank.printdirectory())'''
#48
'''
n = "246.2458"
n = float(n)
print(n)
n = int(n)
print(n)'''
'''
numbers = "12,12.3,1456,1234.5,687.12,523.7"
numbers = numbers.split(",")
for number in numbers:
    if "." in number:
        number = float(number)
        print(number)
    else:
        number = int(number)
        print(number)
        '''
#45
'''
import os
import sys
print(sys.version)
print(sys.getwindowsversion())
print(dir(os))
#directory = os.system("")
#print(directory)
'''
#60
'''
import math
def hypotenuse(a,b):
    return math.sqrt((a**2)+(b**2))
print(hypotenuse(2,8))'''
#61
'''
def converting(feetamt):
    return feetamt*12
print(converting(12))'''
#62
'''
minute = 60
hour = 3600
day = 86400
week = 604800
month = 2.628e+6
def time_convert(what,amt):
    return what * amt
print(time_convert(month,250))'''
#65
'''
minute = 60
hour = 3600
day = 86400
week = 604800
month = 2.628e+6
def secondstosomthing(what,amt):
    return amt/what
print(secondstosomthing(day,604800))'''
#68
'''
def digitaddup(number):
    number = str(number)
    number1 = 0
    for num in number:
        number1 += int(num)
    return number1
print(digitaddup(1234))'''
#69
'''
list = {1,2,3,5,4,1,2,3}
print(sorted(list))'''
#72
'''
import math
print(dir(math))'''
#78
'''
print(dir(__builtins__))'''
#82
'''
list1 = [1,2,3,4,15]
def sumoflist(list):
    value = 0
    for number in list:
        value += number
    return value
print(sumoflist(list1))'''
#83
'''
def valueoverlist(list, valueover):
    listreturn = []
    for number in list:
        if number > valueover:
            listreturn.append(number)
        else:
            None
    return listreturn
list1 = [1,2,3,4,15]
print(valueoverlist(list1,1))'''
#84
'''
string = "I have three dogs and they are very big and I fed them alot of beef today because they need to get strong"
def charocur(string,character):
    occurance = string.count(character)
    return occurance
print(charocur(string,"d"))'''
#86
'''
print(ord("a"))'''
#88
'''
x = 30
y = 20
print(f"{x}+{y}=50")'''
#89
'''
value = 1
notvalue = 2
if value == 1:
    print("First day of the month!")
else:
    print("not equal to one")'''
#91
'''
ankle = 1
leg = 2
print(leg)
print(ankle)
leg = ankle
ankle = leg+1
print(leg)
print(ankle)'''
#92
'''
print(f"!@(*)#&*%_)#&*_)%(*_#(%*_@()$&!@%_)(!@*$_()*!@)_(%&!_@)%*!@)_$*_)(!#*%_)(!@*%_)!(@%")
'''
#93
'''
thingy = "what is the word"
print(str(type(thingy)) + thingy)'''
#110
'''
num_list = [45, 55, 60, 37, 100, 105, 220]
result = list(filter(lambda x: (x % 15 == 0), num_list))
print("Numbers divisible by 15 are",result)'''
#112
'''
list = [1,2,3,4,5,6,7,8,9]
list.pop(0)
print(list)'''
#113
'''
class NotNumber(BaseException):
    pass
number = 1
number2 = "fifteen"
def numcheck(number):
    try:
        number
        if type(number) != int:
            raise NotNumber
    except NotNumber:
        print( "It is not a number")
    finally:
        return number
print(numcheck(number))
print(numcheck(number2))'''
#114
'''
def positivefiler(list):
    for number in list:
        if number <0:
            list.remove(number)
        else:
            pass
        return list
list1 = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
print(positivefiler(list1))'''
'''
print = "abc"
assert print == "abc"'''
'''
from os.path import exists
file_exists = exists("facet")
print(file_exists)

from pathlib import Path
path = Path("facet2.py")
print(path.is_file())

'''
'''
stringlist = ["dog","cat","camel","goat"]

print(" ".join(stringlist) + ".".capitalize())

if "dog" in stringlist:
    print("true")
else:
    print("false")
stringjoin = ""
for item in stringlist:
    stringjoin += item + " "
#stringjoin = stringjoin.upper[0]
stringjoin.join(".",-1)
print(stringjoin)'''
'''
from pathlib import Path
size = Path("facet2.py").stat().st_size/ 1024
print(f"{size}k")'''
'''
def factorial(number):
    if number == 1:
        return number
    return number * factorial(number-1)
print(factorial(5))'''
