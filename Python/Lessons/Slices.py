#L3.01 Slices
#I. Dhiman
coordinates = []

while True:
    x = int(input("Enter x:"))
    y = int(input("Enter y:"))
    if x == 0 and y == 0:
        break
    # elif y == 0:
    #     break
    else:
        coordinates.append(x)
        coordinates.append(y)
        
print(coordinates[0:])

