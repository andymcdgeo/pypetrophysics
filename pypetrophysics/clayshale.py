from . import miscfuncs
    
def gr_clay_shale_vol(minvalue, maxvalue, inputvalue, method="linear", limit_result=False, low_limit=0, high_limit=1):
    """
    Calculates a clay or shale volume from gamma ray log data.
    
    Maxvalue can be set to represent 100% shale value when working with VShale, or it can
    be set to 100% clay when working with VClay.

    Non-linear equations can be selected using the method argument:
        larionov-young
        larionov-old
        steiber
        clavier

    Parameters
    ----------
    minvalue : float
        Value representing a 100% clean interval.
    maxvalue : float
        Value representing either 100% clay or 100% shale.
    inputvalue : float
        Gamma ray value from log measurements.
    method : string
        Select method for calculating VClay or VShale:
        - linear
        - larionov-young
        - larionov-old
        - steiber
        - clavier
        
            By default: linear
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
        Returns a VShale or VClay in decimal units.
    
    References
    -------
    Bhuyan, K. and Passey, Q. R. (1994) ‘Clay estimation from GR and neutron-density porosity logs’, SPWLA 35th Annual Logging Symposium, pp. 1–15.
    Larionov VV (1969) Borehole radiometry: Moscow, U.S.S.R., Nedra
    Steiber RG (1973) Optimization of shale volumes in open hole logs. J Petrol Technol 1973(31):147–162

    Asquith and Krygowski (2004) Basic Well Log Analysis. Second Edition.
    Original paper reference cannot be found for Clavier (1971), however, the following discussion provides insight to its origins.
    https://www.researchgate.net/post/Volume_fraction_of_shale_full_reference_for_Clavier_1971
    """
    
    igr = (inputvalue - minvalue)/(maxvalue - minvalue)

    if method == "linear":
        result = igr
    elif method == "larionov-young":
        result = 0.083 * ((2**(3.71 * igr)) - 1)
    elif method == "larionov-old":
        result = 0.33 * ((2**(2 * igr)) - 1)
    elif method == "steiber":
        result = igr / (3 - 2 * igr)
    elif method == "clavier":
        result = 1.7 - ((3.38-(igr + 0.7)**2)**0.5)
    else:
        raise Exception("Enter a valid method value: linear, larionov-young, larionov-old, steiber, clavier")

    if limit_result is True:
        return miscfuncs.limit_vals(result, low_limit, high_limit)
    else:
        return result

def sp_clay_shale_vol(minvalue, maxvalue, inputvalue, limit_result=False, low_limit=0, high_limit=1):
    """
    Calculates a clay or shale volume from SP log.
    
    Maxvalue can be set to represent 100% shale value when working with VShale, or it can
    be set to 100% clay when working with VClay.

    Parameters
    ----------
     minvalue : float
        Value representing a 100% clean interval.
    maxvalue : float
        Value representing either 100% clay or 100% shale.
    inputvalue : float
        Gamma ray value from log measurements.
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
        Returns a VShale or VClay in decimal units.
    
    References
    ----------
    Dewan, J. T., 1983, Essentials of modern open- hole log interpretation: PennWell Books, Tulsa, Oklahoma.
    """
    
    result = (inputvalue - minvalue)/(maxvalue - minvalue)

    if limit_result is True:
        return miscfuncs.limit_vals(result, low_limit, high_limit)
    else:
        return result

def den_neu_shale_vol(neut_porosity, dens_porosity, neut_shale_porosity, dens_shale_porosity, limit_result=False, low_limit=0, high_limit=1):
    """
    Calculates a shale volume from density and neutron porosity logs.

    Parameters
    ----------
    neut_porosity : float
        Neutron porosity
    dens_porosity : float
        Density porosity
    neut_shale_porosity : [type]
        [description]
    dens_shale_porosity : [type]
        [description]
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
        Returns a shale volume in decimal units.

    References
    ----------
    Bhuyan, K. and Passey, Q. R. (1994) ‘Clay estimation from GR and neutron-density porosity logs’, SPWLA 35th Annual Logging Symposium, pp. 1–15.
    Dewan, J. T., 1983, Essentials of modern open- hole log interpretation: PennWell Books, Tulsa, Oklahoma.
    """
    result = (neut_porosity - dens_porosity)/(neut_shale_porosity - dens_shale_porosity)

    if limit_result is True:
        return miscfuncs.limit_vals(result, low_limit, high_limit)
    else:
        return result

def vshale_to_vclay(vshale, multiplier):
    """
    Converts a shale volume to clay volume using a multiplier.

    Parameters
    ----------
    vshale : float
        Shale volume
    multiplier : float
        Shale to clay multiplier (decimal)

    Returns
    -------
    float
        Returns a clay volume.

     References
    ----------
    Bhuyan, K. and Passey, Q. R. (1994) ‘Clay estimation from GR and neutron-density porosity logs’, SPWLA 35th Annual Logging Symposium, pp. 1–15.
    """
    return vshale * multiplier