import pytest


@pytest.mark.parametrize("x,expected",[(200,"very high"),(170,"high"),(140,"borderline high"),(100,"normal")])

def test_check_LDL(x,expected):
    from LDL import check_LDL
    answer = check_LDL(x)
    assert answer == expected


