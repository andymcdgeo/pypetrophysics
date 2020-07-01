"""
Salinity related calculations
"""

def chlorides_to_NaCl(salinity_chlorides):
    """
    Converts salinity value from ppm Chlorides to ppm NaCl equivalent.

    Parameters
    ----------
    salinity_chlorides : float
        Water Salinity (ppm Chlorides)

    Returns
    -------
    float
        Returns water salinity in ppm NaCl equivalent.
    """
    return salinity_chlorides * 1.645

def NaCl_to_chlorides(salinity_NaCl):
    """
    Converts salinity value from ppm NaCl equivalent to ppm Chlorides.

    Parameters
    ----------
    salinity_NaCl : float
        Water Salinity (ppm NaCl equivalent)

    Returns
    -------
    float
        Returns water salinity in ppm Chlorides.
    """
    return salinity_NaCl / 1.645

def rw_at_form_temp(rw, rw_temperature, temperature_units, new_temperature):
    """
    Converts formation water resistivity from a known temperature to formation temperature.

    Parameters
    ----------
    rw : float
        Water Resistivity (ohmmm)
    rw_temperature : float
        Temperature Rw was measured at.
    temperature_units : string
        Temperature units.
        Enter f for degrees farenheit or c for degrees celsius.
    new_temperature : float
        Temperature to convert resistivity to.

    Returns
    -------
    float
        Returns water resistivity value at the required formation temperature.

    Raises
    ------
    Exception
        Raise an exception if incorrect units are entered.
    """
    if temperature_units.lower() == 'f':
        return rw * ((rw_temperature + 6.77) / (new_temperature + 6.77))
    elif temperature_units.lower() == 'c':
        return rw * ((rw_temperature + 21.5) / (new_temperature + 21.5))
    else:
        raise Exception("Incorrect units. Enter 'f' for farenheit or 'c' for celsius.")
