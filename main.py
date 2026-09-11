print ("Calculate the area of a wall.")
Feed = (input("Enter the width in meters: "))
Width = float(Feed)
Feed = input("Enter the height in meters:")
Height = float(Feed)
Area = Width * Height
print (f"Width is {Width}m and height is {Height}m.")
print (f"The wall will be {round(Area, 2)} square meters.")