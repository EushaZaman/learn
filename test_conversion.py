import conversion
from conversion import CONVERSIONS as cc


def test_feetinch_to_inches():
    assert conversion.feetinch(1,1) == 12

def test_feetinch_to_feet():
    print(cc)
    assert conversion.feetinch(2,12) == 1

def test_convert():
    assert conversion.convert("mile", "inch", 1) == 63360


