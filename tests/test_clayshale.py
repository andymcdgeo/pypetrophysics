import pytest
from pypetrophysics import clayshale

# Testing basic clay vol
# min, max, input, expected
clayshalevol_params = [
    (10, 120, 50, "linear", 0.3630),
    (10, 120, 30, "linear", 0.1818),
    (10, 120, 50, "larionov-young", 0.1280),
    (10, 120, 50, "larionov-old", 0.2180),
    (10, 120, 50, "steiber", 0.160),
    (10, 120, 50, "clavier", 0.20),
]

@pytest.mark.parametrize('minval, maxval, inputval, method, expected', clayshalevol_params)
def test_gr_clay_shale_vol(minval, maxval, inputval, method, expected):
    result = clayshale.gr_clay_shale_vol(minval, maxval, inputval, method)
    assert result == pytest.approx(expected, 0.01)

#Testing exception raised when method not recognised
def test_gr_clay_shale_vol_exception():
    with pytest.raises(Exception):
        clayshale.gr_clay_shale_vol(0, 60, 42, "meaningoflife")

#Testing limits work as expected
clayshalevol_limits_params = [
    (10, 30, 120, 0, 1, 1),
    (10, 50, 5, 0, 0.5, 0),
    (10, 130, 120, 0.8, 1, 0.9166),
    ]
@pytest.mark.parametrize('minval, maxval, inputval, lowval, highval, expected', clayshalevol_limits_params)
def test_gr_clay_shale_vol_limits(minval, maxval, inputval, lowval, highval, expected):
    result = clayshale.gr_clay_shale_vol(minvalue=minval, maxvalue=maxval, inputvalue=inputval, limit_result=True, low_limit=lowval, high_limit=highval)
    assert result == pytest.approx(expected, 0.01)