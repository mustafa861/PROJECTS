mars=37.8/100
def calc_mars_weight(earth_weight):
    """Prompts the user for a weight on Earth  Then prints the equivalent weight on Mars planet."""
    return round(earth_weight*mars,2)
def main():
    try:   
        user_input=float(input("Enter your weight on earth :"))
        mars_weight=calc_mars_weight(user_input)
        print(f"Your weight on Mars would be {mars_weight}🛸.")
    except ValueError:
        print("Plz Enter a valid number")
if __name__ == "__main__":
    main()
    