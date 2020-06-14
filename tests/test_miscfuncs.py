import pytest
from pypetrophysics.miscfuncs import dec_perc_convert
from pypetrophysics.miscfuncs import limit_vals

# Testing prosity unit conversion
perc_dec_input = [
    (55, "percent", 0.55), 
    (0.42, "decimal", 42),
    (0.21, "decimal", 21),
    ]

@pytest.mark.parametrize('inputval, units, expected', perc_dec_input)
def test_dec_percent_convert(inputval, units, expected):
    assert dec_perc_convert(inputval, units) == expected

def test_dec_perc_exception():
    with pytest.raises(Exception):
        dec_perc_convert(42, "solongandthanksforthefish")

# Testing the limit_vals function
def test_limit_vals_high():
    assert limit_vals(50, 20, 40) == 40

def test_limit_vals_low():
    assert limit_vals(50, 60, 100) == 60

def test_limit_vals_in():
    assert limit_vals(50, 20, 100) == 50