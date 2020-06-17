"""
Saturation Calculations
"""

from pypetrophysics import miscfuncs

def sw_archie(phi, rw, rt, arch_a, arch_m, arch_n, limit_result=False, low_limit=0, high_limit=1):
    """
    Archie Water Saturation

    Parameters
    ----------
    phi : float
        Porosity (decimal)
    rw : float
        Water resistivity
    rt : float
        True formation resistivity
    arch_a : float
        Archie Tortuosity Factor (a)
    arch_m : float
        Archie Cementation Exponent (m)
    arch_n : float
        Archie Saturation Exponent (n)
    limit_result : bool, optional
        Apply limits to the result value.
        By default False
    low_limit : int, optional
        Low limit. If value falls below this limit it will be set to this value. 
        By default 0
    high_limit : float, optional
        High limit. If value falls above this limit it will be set to this value.
        By default: 1
    Returns
    -------
    float
        Returns water saturation computed using the Archie equation in decimal units.
    """
    sw = ((arch_a / phi ** arch_m) * (rw/rt))**(1/arch_n)
    
    if limit_result is True:
        return miscfuncs.limit_vals(sw, low_limit, high_limit)
    else:
        return sw

    return sw