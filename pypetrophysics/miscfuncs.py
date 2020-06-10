
    
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
