#A1.06 Is it a Square?
#I. Dhiman
#Source: https://www.sciencedirect.com/topics/computer-science/squared-distancetyou

def is_square(points):
    # Compute squared distances between all pairs of points.
    dists = []
    for i in range(4):
        for j in range(i + 1, 4):
            dx = points[i][0] - points[j][0]
            dy = points[i][1] - points[j][1]
            if dx == 0 and dy == 0:
                return False  
            dists.append(dx * dx + dy * dy)
    
    # Sort the distances
    dists.sort()

    return dists[0] != 0 and dists[0] == dists[1] == dists[2] == dists[3] and dists[4] == dists[5] and dists[4] == 2 * dists[0]

# Input points
points = []
for i in range(1, 5):
    while True:
        try:
            x = int(input(f"Enter x coordinate for point {i}: "))
            y = int(input(f"Enter y coordinate for point {i}: "))
            points.append((x, y))
            break
        except ValueError:
            print("Please enter valid integer coordinates.")

if is_square(points):
    print(f"The points ({points[0][0]},{points[0][1]}), ({points[1][0]},{points[1][1]}), ({points[2][0]},{points[2][1]}) and ({points[3][0]},{points[3][1]}) form a square.")
else:
    print(f"The points ({points[0][0]},{points[0][1]}), ({points[1][0]},{points[1][1]}), ({points[2][0]},{points[2][1]}) and ({points[3][0]},{points[3][1]}) do not form a square.")


#Test Cases
"""
1)
Enter x coordinate for point 1: 5
Enter y coordinate for point 1: 5
Enter x coordinate for point 2: 5
Enter y coordinate for point 2: 5
Enter x coordinate for point 3: 5
Enter y coordinate for point 3: 5
Enter x coordinate for point 4: 5
Enter y coordinate for point 4: 5
The points (5,5), (5,5), (5,5) and (5,5) do not form a square.

2)
Enter x coordinate for point 1: 6
Enter y coordinate for point 1: 7
Enter x coordinate for point 2: 4
Enter y coordinate for point 2: 1
Enter x coordinate for point 3: 3
Enter y coordinate for point 3: 8
Enter x coordinate for point 4: 4
Enter y coordinate for point 4: 0
The points (6,7), (4,1), (3,8) and (4,0) do not form a square.

3)
Enter x coordinate for point 1: 4
Enter y coordinate for point 1: 0
Enter x coordinate for point 2: 0
Enter y coordinate for point 2: 0
Enter x coordinate for point 3: 0
Enter y coordinate for point 3: 4
Enter x coordinate for point 4: 4
Enter y coordinate for point 4: 4
The points (4,0), (0,0), (0,4) and (4,4) form a square.

4)
Enter x coordinate for point 1: 6
Enter y coordinate for point 1: 4
Enter x coordinate for point 2: 6
Enter y coordinate for point 2: 8
Enter x coordinate for point 3: 10
Enter y coordinate for point 3: 8
Enter x coordinate for point 4: 10
Enter y coordinate for point 4: 4
The points (6,4), (6,8), (10,8) and (10,4) form a square.
"""

    