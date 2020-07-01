import pytest

from pypetrophysics import convert

def test_ft_to_m():
    result = convert.ft_to_m(10)
    assert result == pytest.approx(3.048, abs=0.01)

def test_m_to_ft():
    result = convert.m_to_ft(10)
    assert result == pytest.approx(32.8084, abs=0.01)