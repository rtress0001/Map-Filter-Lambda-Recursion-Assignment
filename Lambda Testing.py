places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]


# Define a function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (9/5) * celsius + 32

# Sort the places list based on the converted temperatures
places.sort(key=lambda x: celsius_to_fahrenheit(x[1]))

# Print the sorted list
print(places)