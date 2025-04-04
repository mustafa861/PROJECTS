
import math

AB = float(input("Enter the length of side AB: "))

AC = float(input("Enter the length of side AC: "))

BC = math.sqrt(AB**2 + AC**2)

print("\n=== Pythagorean Theorem Calculation ===")

print(f"AB = {AB}")

print(f"AC = {AC}")

print("Using: BC² = AB² + AC²")

print(f"Hypotenuse (BC) = {BC:.2f}")


