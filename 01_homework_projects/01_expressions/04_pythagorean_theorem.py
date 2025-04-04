import math

def main():
    """A program that calculates the hypotenuse of a right triangle 
    using the Pythagorean theorem (by Greek thinker Pythagoras)."""

    # Get user input for the two perpendicular sides
    AB = float(input("Enter the length of side AB: "))
    AC = float(input("Enter the length of side AC: "))

    # Calculate the hypotenuse using Pythagoras' theorem: BC² = AB² + AC²
    BC = math.sqrt(AB**2 + AC**2)

    # Display results
    print("\n=== Pythagorean Theorem Calculation ===")
    print(f"AB = {AB}")
    print(f"AC = {AC}")
    print("Using: BC² = AB² + AC²")
    print(f"Hypotenuse (BC) = {BC:.2f}")

if __name__ == '__main__':
    main()
