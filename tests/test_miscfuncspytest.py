import pytest
from pypetrophysics.miscfuncs import dec_perc_convert

# @pytest.mark.parametrize("porosity_val", [("100", "50")])
# @pytest.mark.parametrize("units", [("percent", "decimal")])
# @pytest.mark.parametrize("expected", [("1", "500")])
# def test_porosity_unit_convert(porosity_val, units, expected_result):
#     #assert dec_perc_convert(porosity_val, units) == expected_result
#     pass

# def test_porosity_unit_convert2():
#     assert dec_perc_convert(1, "decimal") == 100

the_iterable = [
    (55, "percent", 0.55), 
    (55, "decimal", 0.55),
    (44, "decimal", 0.54),
    ]

    
@pytest.mark.parametrize('arg1, arg2, arg3', the_iterable)
def test_sonic_porosity(arg1, arg2, arg3):
    assert dec_perc_convert(arg1, arg2) == arg3

