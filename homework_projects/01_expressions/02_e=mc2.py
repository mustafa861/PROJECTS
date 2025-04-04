def main():
     """ a program that takes input mass from the user and then outputs the equivalent energy using
     Einstein's mass-energy equivalence formula
     (E stands for energy, m stands for mass, and C is the speed of light"""
c = 299792458  # Speed of light in m/s
mass_in_kg = float(input("Enter mass in kilograms: "))

    # Calculate energy using Einstein's equation
energy_in_joules = mass_in_kg * (c ** 2)

    # Display results
print("\n=== Energy Calculation ===")
print(f"m = {mass_in_kg} kg")
print(f"C = {c} m/s")
print(f"E = {energy_in_joules} joules")

if __name__ == '__main__':
    main()
