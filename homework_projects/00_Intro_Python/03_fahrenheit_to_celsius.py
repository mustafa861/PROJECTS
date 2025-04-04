def main():
   """ this program prompts the user for a temperature in Fahrenheit 
   (this can be a number with decimal places!) and outputs the temperature converted to Celsius."""
degrees_fahrenheit:float=float(input("Enter the temperature in Fahrenheit:"))
degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0
print(f"Temperature {degrees_fahrenheit}F = {degrees_celsius}C.")

if __name__ ==  '__main__':
    main()





