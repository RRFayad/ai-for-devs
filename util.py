def convert_f_to_c(f):
    """
    Convert Fahrenheit to Celsius.
    :param fahrenheit: Temperature in Fahrenheit
    :return: Temperature in Celsius
    """
    return (f - 32) * 5 / 9

print("Fahrenheit to Celsius: ", convert_f_to_c(0))