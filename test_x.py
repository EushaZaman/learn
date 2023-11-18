


def addup(a, b):
    return a + b


def test_addup():
    assert addup(3, 5) == 8

def subtract(a, b):
    return a - b

def test_subtract():
    assert subtract(2, 1) == 1

def calculate(x, y, z):
    return x/y*z

def test_calculate():
    assert calculate(10, 2, 4) == 20

def complex_number(x,y,z):
    a = addup(x,y)
    b = subtract(x,z)
    return calculate(a,b,y)



print(complex_number(20,10,30))

