#A1.04 Converting Inches To Feet
#I. Dhiman

convertingIntoFeet = int(input("Enter a number that will be converted to feet "))

if convertingIntoFeet < 0:
    print("Invalid input")
elif convertingIntoFeet / 12 == 1 and convertingIntoFeet % 12 == 0:
    print("That is", convertingIntoFeet // 12, "foot")
elif convertingIntoFeet / 12 > 1 and convertingIntoFeet % 12 == 0:
    print("That is", convertingIntoFeet // 12, "feet")
elif convertingIntoFeet >= 13 and convertingIntoFeet <= 23:
    print("That is", convertingIntoFeet // 12, "foot", convertingIntoFeet % 12, "inches")
elif convertingIntoFeet / 12 == 0 and convertingIntoFeet > 1:
    print(convertingIntoFeet, "feet")
elif convertingIntoFeet > 24 and convertingIntoFeet % 12 != 0:
    print("That is", convertingIntoFeet // 12, "feet", convertingIntoFeet % 12, "inches")
elif convertingIntoFeet < 12:
    print(convertingIntoFeet, "inches")