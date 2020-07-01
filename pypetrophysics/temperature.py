"""
Temperature related calculations
"""

def temp_gradient(bottom_hole_temperature, surface_temperature, bottom_hole_depth):
    """
    Temperature gradient calculation.

    Parameters
    ----------
    bottom_hole_temperature : float
        Bottom hole temperature (deg F or deg C)
    surface_temperature : float
        Surface temperature (deg F or deg C)
    bottom_hole_depth : float
        Bottom hole depth (ft or m)

    Returns
    -------
    float
        Returns temperature gradient in deg per depth unit (degF/ft or deg C/m)
    """
    gradient = (bottom_hole_temperature - surface_temperature) / bottom_hole_depth
    return gradient

def formation_temperature(surface_temperature, gradient, depth):
    """
    Calculates formation temperature based on a gradient.

    Parameters
    ----------
    surface_temperature : float
        Surface temperature (deg F or deg C)
    gradient : float
        Temperature gradient (degF/ft or degC/m)
    depth : float
        Depth at which temperature is required (ft or m)

    Returns
    -------
    float
        Returns formation temperature at a entered depth
    """
    form_temp = surface_temperature + gradient * depth
    return form_temp

print(formation_temperature(60, 0.01125, 8000))