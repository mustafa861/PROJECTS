 
Peturksbouipo_age:int=16

Stanlau_age:int=20

Mayengua_age:int=48

user_input_age=int(input("Enter your age and check wether u can vote or not:"))

if user_input_age >= Peturksbouipo_age:

    print(f"\n you can vote in Peturksbouipo bcz the voting age limit is  {Peturksbouipo_age} ." )

else:

    print(f" You cannot vote in Peturksbouipo bcz the voting age limit is : , {Peturksbouipo_age} .")
    
if user_input_age >= Stanlau_age:
    
    print(f"\n you can vote in Stanlau bcz the voting age limit is  {Stanlau_age} ." )

else:

    print(f" You cannot vote in Stanlau bcz the voting age limit is :  {Stanlau_age} .")
    
if user_input_age >= Mayengua_age:

    print(f"\n you can vote in Mayengua bcz the voting age limit is  {Mayengua_age} ." )

else:

    print(f" You cannot vote in Mayengua bcz the voting age limit is :  {Mayengua_age} .")
    