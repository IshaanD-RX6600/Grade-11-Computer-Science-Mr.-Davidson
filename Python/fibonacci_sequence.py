#A2.2 Fibonacci Numbers
#I. Dhiman
while True:
    user_input = input("Enter a positive integer: ")
    try:
        n = int(user_input)
        if n > 0:
            break
        else:
            print("Please enter a positive integer.\n")
    except ValueError:
        print("Please enter a valid integer.\n")

a, b = 1, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
    