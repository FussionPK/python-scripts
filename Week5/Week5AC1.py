Name = "Ryan Charkuoth Noah"
Age = 20
Favourite_Color = "Yellow"

with open("my_profile.txt", "w") as fwrite:
    fwrite.write(f"Name: {Name}, Age = {Age}, Favourite Color: {Favourite_Color}")



with open("my_profile.txt", "r") as fread:
    var = fread.read()
    print(var)