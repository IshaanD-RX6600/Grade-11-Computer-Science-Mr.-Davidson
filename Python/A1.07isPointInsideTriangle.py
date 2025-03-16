#A1.07 Is Point Inside Triangle?
#I . Dhiman
#https://www.khanacademy.org/math/cc-eighth-grade-math/cc-8th-geometry/pythagorean-distance/v/distance-formula

def is_valid_triangle(x1, y1, x2, y2, x3, y3):
    # Calculate the sides of the triangle using distance formula
    a = ((x2 - x1)**2 + (y2 - y1)**2)**0.5  
    b = ((x3 - x2)**2 + (y3 - y2)**2)**0.5
    c = ((x3 - x1)**2 + (y3 - y1)**2)**0.5  

    # Check if the triangle is valid using triangle inequality theorem
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return False
    else:
        return True

def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

def is_point_inside_triangle(x1, y1, x2, y2, x3, y3, px, py):
    # First check if the triangle is valid
    if not is_valid_triangle(x1, y1, x2, y2, x3, y3):
        print("These points cannot form a valid triangle")
        return False

    # Calculate area of the main triangle
    A = area(x1, y1, x2, y2, x3, y3)
    
    # Calculate areas of the three smaller triangles
    A1 = area(px, py, x2, y2, x3, y3)
    A2 = area(x1, y1, px, py, x3, y3)
    A3 = area(x1, y1, x2, y2, px, py)
    
    # Check if point is inside (using a small threshold for floating point comparison)
    if abs(A - (A1 + A2 + A3)) < 1:
        print("The point is inside the triangle")
        return True
    else:
        print("The point is outside the triangle")
        return False

# Main function 
def main():
    # Get triangle vertices
    x1 = int(input("Enter the x-coordinate of point 1: "))
    y1 = int(input("Enter the y-coordinate of point 1: "))
    x2 = int(input("Enter the x-coordinate of point 2: "))
    y2 = int(input("Enter the y-coordinate of point 2: "))
    x3 = int(input("Enter the x-coordinate of point 3: "))
    y3 = int(input("Enter the y-coordinate of point 3: "))
    
    # Get point to check
    px = int(input("Enter the x-coordinate of point p: "))
    py = int(input("Enter the y-coordinate of point p: "))
    
    # Check if point is inside triangle
    is_point_inside_triangle(x1, y1, x2, y2, x3, y3, px, py)

if __name__ == "__main__":
    main()
    
#How I came to this solution:
"""
I used the formula for the area of a triangle to check if the point is inside the triangle.
I used the distance formula to check if the triangle is valid.
I used the area of the triangle to check if the point is inside the triangle.
I used the area of the triangle to check if the point is outside the triangle.
I used the area of the triangle to check if the point is on the triangle.
"""

# Get input from the user
while True:
    letter = input("Enter a letter: ")
    if letter.isalpha() == False or len(letter) > 1:
        print("Please enter a single letter.")
    else:
        letter = letter.upper()
        break

# Write your code here.
CharArray = ['A', 'B']  # Use string literals for letters