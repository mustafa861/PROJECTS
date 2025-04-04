def main():
    """A program that converts feet to inches. 
    1 foot = 12 inches (American unit of measurement)."""
    
    feet = float(input("Enter the number of feet to convert: "))
    inches = feet * 12  # Conversion factor: 1 foot = 12 inches
    
    # Display results
    print("\n=== Feet to Inches Conversion ===")
    print(f"Feet: {feet}")
    print("1 Foot = 12 Inches")
    print(f"Total Inches: {inches}")

if __name__ == '__main__':
    main()
