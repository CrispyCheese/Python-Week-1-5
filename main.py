print ("Calculate the area of a wall.")
while True:     # Check for valid integer input for the width
    try:
        Feed = input("Enter the width in meters:")
        Width = int(Feed)
        break
    except ValueError:
        print("Please enter a valid integer for width.")
while True:     # Check for valid integer input for the height
    try:
        Feed = input("Enter the height in meters:")
        Height = int(Feed)
        break
    except ValueError:
        print("Please enter a valid integer for height.")
Area = Width * Height
print (f"Width is {Width}m and height is {Height}m.")
print (f"The wall will be {Area} square meters.")