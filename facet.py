class LengthError(BaseException):
    pass
def display_length(scentence):
    try:
        scentencelegth = len(scentence)
        if scentencelegth == 0:
            raise LengthError
    except LengthError:
        print("Length must not be 0")
    else:
        print("Sucsefully read length of scentence")
    finally:
        return scentencelegth
print(display_length(""))
