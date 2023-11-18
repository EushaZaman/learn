def feetinch(option, val):
    if option == 1:
        return val * 12
    elif option == 2:
        return val / 12


'''        

while True:
    print("1. Convert feet to inches")
    print("2. Convert inches to feet")
    print("3.Convert yards to feet")
    print("4.Convert feet to yards")
    print("99. Quit")
    option = int(input("Enter a number of your choice"))
    if option == 99:
        break
    if option not in (1,2):
        print("INVLID OPTION")
        continue
    feetinch(option, int(input("insert value here")))
    '''
'''
if option == 1:
         val = int(input("Put number of feet here"))
         print(val * 12)
     if option == 2:
         val = int(input("Put number on inches here"))
         print(val / 12)'''
''''''
CONVERSIONS = {
    "millimeter": 0.0393701,
    "centimeter": 0.393701,
    "inch": 1,
    "feet": 12,
    "yard": 36,
    "mile": 63360
}
print(dir(dict))


def conversion(option1, option2, val1):
    return round((CONVERSIONS.get(option1) * val1) / (CONVERSIONS.get(option2)), 4)


def convert(convert_from, convert_to, convert_amount):
    if convert_from not in (CONVERSIONS.keys()):
        return 0.0
    if convert_to not in (CONVERSIONS.keys()):
        return 0.0
    return float(conversion(convert_from, convert_to, convert_amount))

if __name__ == "__main__":
    while True:
        convert_from = input("insert what you want to convert: ")
        convert_to = input("insert what you want to convert to: ")
        convert_amount = int(input("insert the amount that you want to convert: "))

        sucsess = convert(convert_from, convert_to, convert_amount)
        if not sucsess:
            print("You have or more misspelled values")
            continue
        wanto = input("want to continue?: ").lower()
        if wanto == "yes":
            continue
        break





