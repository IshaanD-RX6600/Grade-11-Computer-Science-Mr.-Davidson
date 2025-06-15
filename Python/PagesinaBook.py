#A2.7 Pages in a Book
#I. Dhiman
#Thinking process for this problem
"""
1) Firstly I will take the user input for the number of pages in a book.
2) Then I will use logic to find the number of digits in the page number
    a) lets take an example of 11 
    What I will do is 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 1 + 0 + 1 + 1 = 48
    So this will output 11 becuase there is a total of 11 pages but I will have to distiguish after the number 10
3) For the first function I will use a while loop to find the sum of the digits in a number
"""

target_sum = int(input("Enter a number: "))
# Function to compute the sum of digits from 1 to n
def sum_of_digits(n):
    # This function will calculate the sum of all digits in all page numbers from 1 to n
    # For example, if n = 11 it will calculate 1 + 2 + 3 + ... + 9 + 1 + 0 + 1 + 1 = 48

    # The point of this fucntion is to when a target number or sum is given
    def digit_sum(num):
        # Now within this function I will use another function to find the sum of dights in a singular number.

        total = 0 # going to hold the sum of the digits
        while num > 0: # loop will continue as long as the number is larger or greater than 0
            total += num % 10 # Taking the right most digit of the number and additing to the teltaol
            num = num // 10 # This line will removethe right digit from the number
        # This will continue until the number is 0
        return total
    
    #Returning to the main function
    # Now I will use a for loop to iterate through the numbers from 1 to n
    total_sum = 0 # Varaible to hold the total sum of the digits
    for i in range(1, n + 1):
        total_sum += digit_sum(i) #Calling the fucntion above to fidn the addition of digits in that page number
    return total_sum

# Acually algorithm


# Tests
"""
Enter a number: 900
900 matches with 99
"""