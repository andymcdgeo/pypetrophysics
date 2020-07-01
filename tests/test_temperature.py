import pytest
from pypetrophysics import temperature

def test_temp_gradient():
    result = temperature.temp_gradient(150, 60, 8000)
    assert result == pytest.approx(0.01125, abs=0.01)

def test_formation_temperature():
    result = temperature.formation_temperature(60, 0.01125, 8000)
    assert result == 150