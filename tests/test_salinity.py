import pytest
from pypetrophysics import salinity

def test_rw_at_form_temp():
    result = salinity.rw_at_form_temp(0.05, 75, "f", 112)
    assert result == pytest.approx(0.0345, abs=0.001)

def test_chlorides_to_NaCl():
    result = salinity.chlorides_to_NaCl(13000)
    assert result == 21385

def test_NaCl_to_chlorides():
    result = salinity.NaCl_to_chlorides(21385)
    assert result == 13000