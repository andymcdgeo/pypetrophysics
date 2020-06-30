"""
Saturation Calculations
"""

from pypetrophysics import miscfuncs

def formation_factor(arch_a, phi, arch_m):
    """
    Computes Archie Formation Factor (F)

    Parameters
    ----------
    arch_a : float
        Archie Tortuosity Factor - a
    phi : [type]
        Porosity (decimal)
    arch_m : float
        Archie Cementation Exponent - m

    Returns
    -------
    float
        Returns Archie Formation Factor
    """
    return arch_a / phi ** arch_m

def ro(formation_factor, rw):
    """
    Archie Ro - Resistivity of water saturation formation (ohm.m)

    Parameters
    ----------
    formation_factor : float
        Archie Formation Factor
    rw : float
        Resistivity of formation water (ohm.m)

    Returns
    -------
    float
        Returns resistivity of water saturation formation (ohm.m)
    """
    return formation_factor * rw

def resistivity_index(rt, ro):
    """
    Archie Resistivity Index (I)

    Parameters
    ----------
    rt : float
        True formation resistivity (ohm.m)
    ro : float
        Resistivity of water saturated formation (ohm.m)

    Returns
    -------
    float
        Returns Archie resistivity index (I)
    """
    return rt/ro

def sw_archie(phi, rw, rt, arch_a, arch_m, arch_n, limit_result=False, low_limit=0, high_limit=1):
    """
    Archie Water Saturation

    Parameters
    ----------
    phi : float
        Porosity (decimal)
    rw : float
        Water resistivity (ohmm.m)
    rt : float
        True formation resistivity (ohmm.m)
    arch_a : float
        a - Archie Tortuosity Factor
    arch_m : float
        m - Archie Cementation Exponent
    arch_n : float
        n - Archie Saturation Exponent
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

def sw_simandoux():
    # TODO
    pass


def sw_indonesian(rw, rt, rshale, vclay, phi, archie_m, archie_n):
    """
    Calculates water saturation using Poupon-Leveaux (1971) - Indonesian.

    The indonesian equation is designed for determining water saturation in shaly sands.

    Parameters
    ----------
    rw : float
        Water resistivity (ohm.m)
    rt : float
        Formation resistivity (ohm.m)
    rshale : float
        Shale resistivity (ohm.m)
    vclay : float
        Volume of clay (decimal)
    phi : float
        Porosity (decimal)
    archie_m : float
        m - Archie cementation exponent
    archie_n : float
        n - Archie saturation exponent

    Returns
    -------
    float
        Returns water saturation computed using the Poupon-Leveaux (Indonesian) equation.

      References
    ----------
    Poupon, A. and Leveaux, J. (1971) ‘Evaluation Of Water Saturation In Shaly Formations’, 
    The Log Analyst, vol. 12, no. 4, pp. 3–8.

    PetroWiki (2020), Water Saturation Determination, https://petrowiki.org/Water_saturation_determination
    """
    part_a = ((vclay**(2-vclay))/rshale)**0.5
    part_b = (phi**archie_m / rw)**0.5
    part_c = (part_a + part_b)**2 * rt
    result = part_c**(-1/archie_n)
    
    return result

def sw_waxsmit(rw, rt, b, qv, a, phit, m_star, n_star):
    """
    Calculates Water Saturation using Waxman-Smits (1968).

    W-S equation is designed for determining water saturation in shaly sand.
    To solve the equation a number of iterations need to be executed.

    Parameters
    ----------
    rw : float
        Water resistivity (ohm.m)
    rt : float
        Formation resistivity (ohm.m)
    b : float
        Equivalent Conductivity of Exchange Cations
    qv : float
        Cation Exchange Capacity Per Unit Pore Volume (meq-ml-1)
    a : float
        a - Archie Tortuosity Factor
    phit : float
        Total Porosity (decimal)
    m_star : float
        m-star - Shaly sand cementation exponent
    n_star : float
        n-star - Shaley sand saturation exponent

    Returns
    -------
    float
        Returns water saturation computed using the Waxman-Smits equation in decimal units.
            
    References
    ----------
    Waxman, M. H. and Smits, L. J. M. (1968) ‘Electrical Conductivities in Oil-Bearing Shaly Sands’, 
    Society of Petroleum Engineers Journal, vol. 8, no. 2 [Online]. DOI: https://doi.org/10.2118/1863-A.

    Freedman, R., Formation, F. and Consultants, E. (1985) ‘THE WAXMAN-SMITS EQUATION FOR SHALY SANDS : I . SIMPLE METHODS OF SOLUTION ; 
    11 . ERROR ANALYSIS’, no. March 1985.
    """
    swt = sw_archie(a, m_star, n_star, phit, rw, rt)
    difference = 0.001
    x = True
    count = 0
    while x:
        swt_prev = swt
        part_a = rt * (1 + rw * b * qv / swt)
        part_b = a * phit**(-m_star) * rw
        swt = (part_a / part_b) ** (-1 / n_star)
        if abs(swt - swt_prev) <= difference:
            x = False
        count += 1
        #print(count, swt)
    
    return swt


def excess_cond_bqv(b, qv):
    return b * qv

def qv_cec(density_dry_clay, phit, cec):
    return ((cec * density_dry_clay * (1 - phit))) / (100 * phit)

def equiv_cond_echange_cations_B(temp, rw):
    """
    Calculates Equivalent Conductivity of Exchange Cations, (B)

    Parameters
    ----------
    temp : float
        Temperature (deg C)
    rw : float
        Water Resistivity (ohmm.m)

    Returns
    -------
    float
        B - Equivalent Conductivity of Exchange Cations
    """
    part_a = (-1.28 + 0.225 * temp - 0.0004059 * temp**2)
    part_b = (1 + rw ** 1.23 * (0.045 * temp - 0.27)) 

    return part_a / part_b

def qv_hsk():
    pass

def swb(porosity_wet_clay, clay_vol, phit):
    return (porosity_wet_clay * clay_vol) / phit

def qv_juhasz(vclay_dry, density_dry_clay, cec_dry_clay, phit):
    """[summary]

    Parameters
    ----------
    vclay_dry : float
        Volume of dry clay (decimal)
    density_dry_clay : float
        Density of dry clay (g/cc)
    cec_dry_clay : float
        Cation Exchange Capacity of the average clay minerals present (meq/g)
    phit : float
        Total porosity

    Returns
    -------
    float
        Returns Qv - Cation Exchange Capacity per unit total pore volume.
    
    References
    ----------
    Juhasz, I. (1979) ‘The Central Role of Qv and Formation-Water Salinity in the Evaluation of Shaly Formations’,
    The Log Analyst, vol. 20, no. 4, pp. 1–11.

    Juhasz, I. (1981) ‘Normalised Qv--the key to shaly sand evaluation using the Waxman-Smits equation in the absence of core data’, 
    Society of Professional Well Log Analysts 22nd Annual Logging Symposium Transactions, no. Paper Z, p. 36.
    """
    return (vclay_dry * density_dry_clay * cec_dry_clay)/phit

def vol_dry_clay(phi_n, phi_d, HI_dry_clay):
    """
    Calculates volume of dry clay content

    Parameters
    ----------
    phi_n : float
        Neutron porosity (decimal)
    phi_d : float
        Density porosity (decimal)
    HI_dry_clay : float
        Hydrogen Index of the average dry clay-mineral mixture within the formation (decimal)

    Returns
    -------
    float
        Returns volume of dry clay (decimal)
    
    References
    ----------
    Juhasz, I. (1979) ‘The Central Role of Qv and Formation-Water Salinity in the Evaluation of Shaly Formations’,
    The Log Analyst, vol. 20, no. 4, pp. 1–11.

    Juhasz, I. (1981) ‘Normalised Qv--the key to shaly sand evaluation using the Waxman-Smits equation in the absence of core data’, 
    Society of Professional Well Log Analysts 22nd Annual Logging Symposium Transactions, no. Paper Z, p. 36.
    """
    return phi_n - phi_d / HI_dry_clay

def bvw(sw, phi):
    """
    Calculates Bulk Volume Water

    Parameters
    ----------
    sw : float
        Water saturation (dec)
    phi : float
        Porosity (dec)

    Returns
    -------
    float
        Bulk volume water (dec)
    """
    return sw * phi