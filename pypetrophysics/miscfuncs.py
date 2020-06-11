def limit_vals(input_value, low_limit, high_limit):
    """
    Apply limits to an input value.

    Parameters
    ----------
    input_value : float
        Input value.
    low_limit : float
        Low limit. If value falls below this limit it will be set to this value.
    high_limit : float
        High limit. If value falls above this limit it will be set to this value.

    Returns
    -------
    float
        Returns input value unless it falls above or below the entered limits.
    """
    if input_value < low_limit:
        return low_limit
    elif input_value > high_limit:
        return high_limit
    else:
        return input_value

def dec_perc_convert(input_value, input_units):
    """
    Convert from decimal to percent or percent to decimal.

    Parameters
    ----------
    input_value : float
        Value to be converted.
    input_units : string
        Units of the input value.
        Enter either "percent" or "decimal"

    Returns
    -------
    float
        Returns converted value in percent or decimal.
    """
    if input_units == "percent":
        return input_value / 100
    elif input_units == "decimal":
        return input_value * 100
    else:
        print("Enter the correct value for input units: percent or decimal")
