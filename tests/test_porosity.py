import unittest
import pytest

from pypetrophysics import porosity


porosity_den_params = [
    (2.65, 1, 2.45, 0.1379),
    (2.71, 0.99, 2.68, 0.017),
]

@pytest.mark.parametrize('rhomatrix, rhofluid, rhobulk, expected', porosity_den_params)
def test_porosity_density(rhomatrix, rhofluid, rhobulk, expected):
    result = porosity.porosity_density(rhomatrix, rhofluid, rhobulk)
    assert result == pytest.approx(expected, abs=0.001)


porosity_den_params_limits = [
    (2.65, 1, 2.45, 0.15, 0.6, 0.15),
    (2.71, 0.99, 2.08, 0, 0.1, 0.1),
]

@pytest.mark.parametrize('rhomatrix, rhofluid, rhobulk, lowlimit, highlimit, expected', porosity_den_params_limits)
def test_porosity_density_limits(rhomatrix, rhofluid, rhobulk, lowlimit, highlimit, expected):
    assert porosity.porosity_density(rhomatrix, rhofluid, rhobulk, limit_result=True, low_limit=lowlimit, high_limit=highlimit) == expected
    # assert result == expected
