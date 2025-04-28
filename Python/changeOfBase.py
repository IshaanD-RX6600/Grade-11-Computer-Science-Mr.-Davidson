#A2.5 Change of Base
#I Dhiman

while True:
    try:
        number = int(input("Enter a positive base-10 number: "))
        if number < 0:
            print("The number must be positive.")
            continue
        break
    except ValueError:
        print("Enter a valid integer.")

while True:
    try:
        base = int(input("Enter a base (2–9): "))
        if base < 2 or base > 9:
            print("The base must be between 2 and 9.")
            continue
        break
    except ValueError:
        print("Enter a valid base.")
if number == 0:
    print("0")
else:
    result = ""
    temp = number
    while temp > 0:
        remainder = temp % base
        temp //= base
        result = str(remainder) + result
    print(f"{number} in base {base} is {result}")