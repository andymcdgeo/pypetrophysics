"""
Conversion functions
"""

# Depth and length conversions
def ft_to_m(inputvalue):
    """
    Converts feet to metres.

    Parameters
    ----------
    inputvalue : float
        Input value in feet.

    Returns
    -------
    float
        Returns value in metres.
    """
    return inputvalue * 0.3048

def m_to_ft(inputvalue):
    """
    Converts metres to feet.

    Parameters
    ----------
    inputvalue : float
        Input value in metres.

    Returns
    -------
    float
        Returns value in feet.
    """
    return inputvalue * 3.28084

def ft_to_in(inputvalue):
    """
    Converts feet to inches.

    Parameters
    ----------
    inputvalue : float
        Input value in feet.

    Returns
    -------
    float
        Returns value in inches.
    """
    return inputvalue * 12

def in_to_ft(inputvalue):
    """
    Converts inches to feet.

    Parameters
    ----------
    inputvalue : float
        Input value in inches.

    Returns
    -------
    float
        Returns value in feet.
    """
    return inputvalue / 12

# Velocity / Slowness conversions
def velocity_to_slowness(inputvalue):
    """
    Converts velocity to slowness.

    Parameters
    ----------
    inputvalue : float
        Input value in velocity units.

    Returns
    -------
    float
        Returns value in slowness units.
    """
    return 1000000/inputvalue

def slowness_to_velocity(inputvalue):
    """
    Converts slowness to velocity.

    Parameters
    ----------
    inputvalue : float
        Input value in slowness units.

    Returns
    -------
    float
        Returns value in velocity units.
    """
    return 1000000/inputvalue

# Temperature conversions
def temperature_convert(inputvalue, inputunits, outputunits):
    """
    Converts temperature from one unit to another.

    Parameters
    ----------
    inputvalue : float
        Input temperature value
    inputunits : string
        Input temperature units:
            c = celsius
            f = fahrenheit
            k = kelvin
    outputunits : string
        Output temperature units:
            c = celsius
            f = fahrenheit
            k = kelvin

    Returns
    -------
    float
        Returns temperature value in required units.
    """
    if inputunits.lower() == "c":
        if outputunits.lower() == "f":
            return (9/5)*inputvalue+32
        elif outputunits.lower() == "k":
            return inputvalue + 273.15
        elif outputunits.lower() == "c":
            return inputvalue
    
    if inputunits.lower() == "f":
        if outputunits.lower() == "c":
            return (5/9)*inputvalue-32
        elif outputunits.lower() == "k":
            return (inputvalue-32) * (5/9)+273.15
        elif outputunits.lower() == "f":
            return inputvalue
    
    if inputunits.lower() == "k":
        if outputunits.lower() == "c":
            return inputvalue - 273.15
        elif outputunits.lower() == "f":
            return (inputvalue-273.15)*(9/5)+32
        elif outputunits.lower() == "k":
            return inputvalue
    units = ["k", "c", "f"]
    
    if inputunits.lower() not in units or outputunits.lower() not in units:
        raise Exception("Enter a valid temperature inputunit or outputunit value. Must be: c, f or k")