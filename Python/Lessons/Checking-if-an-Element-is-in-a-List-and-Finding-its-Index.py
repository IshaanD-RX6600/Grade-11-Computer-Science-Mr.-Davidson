myList = [1, 2, 3, 4, 5, 'a', 'b', 'c']

user_input = input("Enter a number or character: ")

if user_input.isdigit():
    user_input = int(user_input)

if user_input in myList:
    index_position = myList.index(user_input)
    print(f"True — '{user_input}' is in the list at index {index_position}.")
else:
    print(f"False — '{user_input}' is not in the list.")
