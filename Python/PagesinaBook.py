#A2.7 Pages in a Book
#I. Dhiman
#Thinking process for this problem
"""
1) Firstly I will take the user input for the number of pages in a book.
2) Then I will use logic to find the number of digits in the page number
    a) lets take an example of 11 
    What I will do is 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 1 + 0 + 1 + 1 = 48
    So this will output 11 becuase there is a total of 11 pages but I will have to distiguish after the number 10
"""

target_sum = int(input("Enter a number: "))
# Function to compute the sum of digits from 1 to n
def sum_of_digits(n):\
    #Now within this function I will use another function to find the sum of dights in a singular number.
    def digit_sum(num):
        
        total = 0
        while num > 0:
            total += num % 10
            num //= 10
        return total




# Tests
"""
Enter a number: 900
900 matches with 99
"""