def main():
    """a program to solve age-related riddle!friends and their ages are as follows:
Anton is 21 years old.Beth is 6 years older than Anton.Chen is 20 years older than Beth.
Drew is as old as Chen's age plus Anton's age.Ethan is the same age as Chen."""

Anton_age:int=21
Beth_age:int=6+Anton_age
Chen_age:int=20+Beth_age
Drew_age:int=Chen_age+Anton_age
Ethan_age:int=Chen_age

print(f"Anton is {Anton_age} years old.")
print(f"Beth is {Beth_age} Years old.")
print(f"Chen is {Chen_age} Years old.")
print(f"Drew is {Drew_age} Years old.")
print(f"Ethan is {Ethan_age} Years old.")

if __name__ == '__main__':
    main()

