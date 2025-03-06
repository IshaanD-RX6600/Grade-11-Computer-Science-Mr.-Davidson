#A1.06 Is it a Square?
#I. Dhiman

def is_square(points):
    #going to compute the squared distances between all pairs of points
    distance = []
    for i in range(4):
        for j in range(i+1,4):
            distanceX = points[i][0] - points[j][0]
            distanceY = points[i][1] - points[j][1]

            if distanceX == 0 and distanceY == 0:
                return False
            distance.append(distanceX * distanceX + distanceY * distanceY)

            distance.sort()
            return distance[0] != 0 and distance[0] == distance[1] == distance[2] == distance[3] and distance[4] == distance[5] and distance[4] == 2 * distance[0]

