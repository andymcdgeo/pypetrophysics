"""
Temperature related calculations
"""

def temp_gradient(bottom_hole_temperature, surface_temperature, bottom_hole_depth):
    gradient = (bottom_hole_temperature - surface_temperature) / bottom_hole_depth
    return gradient

def formation_temperature(surface_temperature, gradient, depth):
    form_temp = surface_temperature + gradient * depth
    return form_temp