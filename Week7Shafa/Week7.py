cylinder_radius = int(input("Enter the radius of the cylinder: "))
cylinder_height = int(input("Enter the height of the cylinder: "))

volume = 3.14 * (cylinder_radius*cylinder_radius) * cylinder_height

surface = (2*(3.14*(cylinder_radius*cylinder_radius))) + (2*(3.14*cylinder_radius*cylinder_height))

print("The volume of the cylinder is to 2 decimal places:", round(volume, 2))

print("the surface area ")
