
MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14
EARTH_GRAVITY = 1.0

def planets_gravity():
    """a Program to calculate the weight of earthlings on different Planets asking use for Planet and weight on Earth"""
    try:
        planet = input("Enter the planet: ").strip().lower()
        if planet not in ["mercury", "venus", "mars", "jupiter", "saturn", "uranus", "neptune"]:
            raise ValueError("Invalid planet name")



        earth_weight = float(input("Enter your weight on Earth (kg): "))

       
        if planet == "mercury":
            gravity_constant = MERCURY_GRAVITY
        elif planet == "venus":
            gravity_constant = VENUS_GRAVITY
        elif planet == "mars":
            gravity_constant = MARS_GRAVITY
        elif planet == "jupiter":
            gravity_constant = JUPITER_GRAVITY
        elif planet == "saturn":
            gravity_constant = SATURN_GRAVITY
        elif planet == "uranus":
            gravity_constant = URANUS_GRAVITY
        else:
            gravity_constant = NEPTUNE_GRAVITY  

 
        planetary_weight = earth_weight * gravity_constant
        rounded_planetary_weight = round(planetary_weight, 2)
 
        print(f"Your weight on {planet.capitalize()}: {rounded_planetary_weight} kg")
   
    except ValueError as e:
        print(f"Error: {e}. Please enter the correct information.")


if __name__ == "__main__":
    planets_gravity()
    
