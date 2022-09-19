import pytest


@pytest.mark.parametrize("x,expected",[(80,"Normal"),(50,"Borderline Low"),(20,"Low")])

def test_check_HDL(x,expected):
    from blood_calculator import check_HDL
    answer = check_HDL(x)
    assert answer == expected





"""
def test_check_HDL_BL():
    from blood_calculator import check_HDL
    answer_BL = check_HDL(50)
    expected_BL = "Borderline Low"
    assert answer_BL == expected_BL

def test_check_HDL_L():
    from blood_calculator import check_HDL
    answer_L = check_HDL(20)
    expected_L = "Low"
    assert answer_L == expected_L
"""
