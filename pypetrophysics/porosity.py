"""
Porosity Calculations
"""

from . import miscfuncs

def porosity_density(rhomatrix, rhofluid, rhobulk, limit_result=False, low_limit=0, high_limit=0.6):
    """
    Calculate porosity from a density log

    Parameters
    ----------
    rhomatrix : float
        Matrix density. 
        
        Typical values:
            Sandstone: 2.65 g/cc
            Limestone: 2.71 g/cc
            Dolomite: 2.80 - 2.85 g/cc
    rhofluid : float
        Fluid density.
    rhobulk : float
        Bulk density from log measurements
    limit_result : bool, optional
        Apply limits to the result value.
        By default False
    low_limit : int, optional
        Low limit. If value falls below this limit it will be set to this value. 
        By default 0
    high_limit : float, optional
        High limit. If value falls above this limit it will be set to this value.
        By default: 0.6

    Returns
    -------
        float
        Density porosity value in decimal units.
    """
    porosity = (rhomatrix - rhobulk)/(rhobulk - rhofluid)

    if limit_result is True:
        return miscfuncs.limit_vals(porosity, low_limit, high_limit)
    else:
        return porosity
        
def porosity_sonic(dtmatrix, dtfluid, dtlog, method="wyllie", limit_result=False, low_limit=0, high_limit=0.6):
    """
    Caculate porosity from a sonic log using either the Wyllie-Time Average equation
    or Raymer-Hunt-Gardener equation.

    Parameters
    ----------
    dtmatrix : float
        Matrix slowness.

        Typical values:
            Sandstone: 52-55 us/ft
            Limestone: 47 us/ft
            Dolomite: 43 us/ft
    dtfluid : float
        Fluid slowness.
    dtlog : [type]
        Slowness (DT) from log measurements.
    method : string
        Select a method for calculating sonic porosity:
        "wyllie" - Wyllie Time Average (default)
        "raymer" - Raymer Hunt Gardner
    limit_result : bool, optional
        Apply limits to the result value.
        By default False
    low_limit : int, optional
        Low limit. If value falls below this limit it will be set to this value. 
        By default 0
    high_limit : float, optional
        High limit. If value falls above this limit it will be set to this value.
        By default: 0.6

    Returns
    -------
    float
        Sonic porosity value in decimal units.

    Raises
    ------
    Exception
        Raise an exception if method value is not 1 or 2.

    References
    ----------
    Wyllie, M.R.J., Gregory, A.R., and Gardner, L.W. 1956. Elastic Wave Velocities in Heterogeneous and Porous Media. Geophysics 21 (1): 41–70.
    Raymer, L.L., Hunt, E.R., and Gardner, J.S. 1980. An Improved Sonic Transit Time-to-Porosity Transform, paper P. Trans., 1980 Annual Logging Symposium, SPWLA, 1–12.
    """
    if method == "wyllie": #Wylie Time Average
        porosity = (dtlog - dtmatrix) / (dtfluid - dtmatrix)
    elif method == "raymer": #Raymer Hunt Gardener 
        alpha = (dtmatrix / (2 * dtfluid)) - 1
        porosity = -alpha-((alpha**2 + (dtmatrix / dtlog)-1)**0.5)
    else:
        raise Exception("Enter a valid method value: wyllie or raymer")

    if limit_result is True:
        return miscfuncs.limit_vals(porosity, low_limit, high_limit)
    else:
        return porosity

def porosity_effective(phit, vclay, phitclay):
    """
    Converts total porosity to effective porosity

    Parameters
    ----------
    phit : float
        Total porosity (decima)
    vclay : float
        Volume of clay (decimal)
    phitclay : float
        Clay porosity - taken from a shale interval (decimal)

    Returns
    -------
    float
        Returns effective porosity (decimal)
    """
    return phit - vclay * phitclay

def porosity_shale(dens_dry_shale, dens_wet_shale, dens_water):
    """
    Calculates shale porosity.

    Parameters
    ----------
    dens_dry_shale : float
        Dry shale density (g/cc)
    dens_wet_shale : float
        Wet shale density (g/cc)
    dens_water : float
        Water density (g/cc)

    Returns
    -------
    float
        Returns shale porosity (decimal).
    """
    return (dens_dry_shale - dens_wet_shale) / dens_water