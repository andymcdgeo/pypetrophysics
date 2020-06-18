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