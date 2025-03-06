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
    
# Test Cases
"""
1)
Enter a number that will be converted to feet -5
Invalid input

2)
Enter a number that will be converted to feet 0
0 inches

3)
Enter a number that will be converted to feet 10
10 inches

4)
Enter a number that will be converted to feet 12
That is 1 foot

5)
Enter a number that will be converted to feet 13
That is 1 foot 1 inches

6)
Enter a number that will be converted to feet 23
That is 1 foot 11 inches

7)
Enter a number that will be converted to feet 24
That is 2 feet

8)
Enter a number that will be converted to feet 25
That is 2 feet 1 inches

9)
Enter a number that will be converted to feet 36
That is 3 feet

10)
Enter a number that will be converted to feet 1
1 inches
"""