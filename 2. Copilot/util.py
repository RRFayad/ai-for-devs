# Create a function that receives a celscius or fahrenheit temperature and returns the converted temperature
def convert_temperature(temperature, to_unit):
    """
    Convert temperature between Celsius and Fahrenheit.

    Args:
        temperature (float): The temperature to convert.
        to_unit (str): The unit to convert to ('C' for Celsius, 'F' for Fahrenheit).

    Returns:
        float: The converted temperature.
    """
    if to_unit == 'C':
        return (temperature - 32) * 5.0/9.0
    elif to_unit == 'F':
        return (temperature * 9.0/5.0) + 32
    else:
        raise ValueError("Invalid unit. Use 'C' for Celsius or 'F' for Fahrenheit.")

