# get 4 integers from the user called a1, a2, a3, a4

a1 = int(input("Enter First Integer: "))
a2 = int(input("Enter Second Integer: "))
a3 = int(input("Enter Third Integer: "))
a4 = int(input("Enter Fourth Integer: "))

s1 = 0
s2 = 0
s3 = 0
s4 = 0


if a2 >= a1:
    s1 = a1
    s2 = a2
else:
    s1 = a2
    s2 = a1

if a4 >= a3:
    s3 = a3
    s4 = a4
else:
    s3 = a4
    s4 = a3
if s3 >= s2:
    print(s1, s2, s3, s4)
elif s3 >= s1:
    if s4 >= s2:
        print(s1, s3, s2, s4)
    elif s4 >= s1:
        print(s1, s3, s4, s2)
    else:
        print(s3, s1, s4, s2)
else:
    if s4 >= s2:
        print(s3, s1, s2, s4)
    elif s4 >= s1:
        print(s3, s1, s4, s2)
    else:
        print(s3, s4, s1, s2)

#test cases
"""
1)
Enter First Integer: 1
Enter Second Integer: 2
Enter Third Integer: 3
Enter Fourth Integer: 4
1 2 3 4

2)
Enter First Integer: 3
Enter Second Integer: 5
Enter Third Integer: 4
Enter Fourth Integer: 8
3 4 5 8

3)
Enter First Integer: 3
Enter Second Integer: 8
Enter Third Integer: 4
Enter Fourth Integer: 7
3 4 7 8

4)
Enter First Integer: 6
Enter Second Integer: 10
Enter Third Integer: 2
Enter Fourth Integer: 12
2 6 10 12

5)
Enter First Integer: 6
Enter Second Integer: 10
Enter Third Integer: 2
Enter Fourth Integer: 8
2 6 8 10

6)
Enter First Integer: 5
Enter Second Integer: 7
Enter Third Integer: 2
Enter Fourth Integer: 4
2 4 5 7

7)
Enter First Integer: 5
Enter Second Integer: 5
Enter Third Integer: 5
Enter Fourth Integer: 5
5 5 5 5
"""