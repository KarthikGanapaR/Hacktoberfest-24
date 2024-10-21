# Program to convert Celsius to Fahrenheit by taking user input

def celsius_to_fahrenheit(celsius):
   
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Input temperature in Celsius from the user
celsius = float(input("Enter temperature in Celsius: "))

#  conversion function calling
fahrenheit = celsius_to_fahrenheit(celsius)


print(f"{celsius}°C is equal to {fahrenheit}°F")
