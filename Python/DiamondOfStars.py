#A2.3 Diamond of Stars
#I Dhiman
while True:
    try:
        n = int(input("# of lines for diamonds"))
        if n > 0:
            break
        print("please enter a valid number")
        
    except ValueError:
        print("wrong input enter a valid number")
        
if n % 2 == 0:
    middle1 = (n // 2) - 1
    middle2 = n // 2
else: 
    middle1 = middle2 = n // 2
    
for row in range(n):
    dis = min(abs(row - middle1), abs(row - middle2))
    outerSpaces = dist
    innerSpaces = (n - 2) - (2 * dist)
    if innerSpaces < 0:
        print(" " * outerSpace + "#")
    else:
        print(" " * outerSpaces + "#" + " " * innerSpaces + "#")

