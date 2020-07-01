import pytest
from pypetrophysics import saturation

def test_sw_archie():
    result = saturation.sw_archie(0.23, 0.9, 40, 0.62, 2.15, 2)
    assert result == pytest.approx(0.573, abs=0.001)

sw_archie_params_limits = [
    (0.23, 0.9, 40, 0.62, 2.15, 2, 0, 0.5, 0.5),
    (0.23, 0.9, 40, 0.62, 2.15, 2, 0.6, 1, 0.6),
]
@pytest.mark.parametrize('phi, rw, rt, arch_a, arch_m, arch_n, low_limit, high_limit, expected', sw_archie_params_limits)
def test_sw_archie_limits(phi, rw, rt, arch_a, arch_m, arch_n, low_limit, high_limit, expected):
    assert saturation.sw_archie(phi, rw, rt, arch_a, arch_m, arch_n, limit_result=True, low_limit=low_limit, high_limit=high_limit) == expected

def test_formation_factor():
    result = saturation.formation_factor(1, 0.12, 2)
    assert result == pytest.approx(69.444, abs=0.01)

def test_ro():
    result = saturation.ro(69.444, 0.02)
    assert result == pytest.approx(1.3888, abs=0.01)

def test_resistivity_index():
    result = saturation.resistivity_index(100, 10)
    assert result == pytest.approx(10, abs=0.01)

def test_resistivity_index_2():
    result = saturation.resistivity_index(123, 3)
    assert result == pytest.approx(41, abs=0.01)