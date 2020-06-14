import pytest
from pypetrophysics import clayshale

# Testing basic clay vol
# min, max, input, expected
clayshalevol_params = [
    (10, 150, 20, "linear", 0.0714),
    (10, 150, 20, "larionov-young", 0.01673),
    (10, 150, 20, "larionov-old", 0.03434),
    (10, 150, 20, "steiber", 0.02499),
    (10, 150, 20, "clavier", 0.03119),
]

@pytest.mark.parametrize('minval, maxval, inputval, method, expected', clayshalevol_params)
def test_gr_clay_shale_vol(minval, maxval, inputval, method, expected):
    result = clayshale.gr_clay_shale_vol(minval, maxval, inputval, method)
    assert result == pytest.approx(expected, 0.01)