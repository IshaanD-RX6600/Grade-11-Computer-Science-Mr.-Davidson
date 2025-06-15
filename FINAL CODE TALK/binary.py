#Binary explanation

"""
Computers handle all data as a stream of binary numbers 
1 <- a single bit is a single digit in binary,
10101010 <- byte is a group of 8 bits, <- 256 total combinations
Modern languages are converted into binary for processing by the compiler. 
The conventional counting system uses base 10, which is why we have digits 0-9.
Binary uses base 2, which is why we have digits 0 and 1.
Hexadecimal is another base system, which uses base 16.

example of binary
The reason why remainder is used is because we are converting from base 10 to base 2.
add remainders can only be 0 or 1, so we divide by 2 and keep track of the remainders.
13 ÷ 2 = 6 remainder 1
 6 ÷ 2 = 3 remainder 0
 3 ÷ 2 = 1 remainder 1
 1 ÷ 2 = 0 remainder 1
Read remainders bottom to top: 1101

Position values: 8 4 2 1
Binary digits:   1 1 0 1

Position 0: 1 × 1 = 1
Position 1: 0 × 2 = 0
Position 2: 1 × 4 = 4
Position 3: 1 × 8 = 8
#adds up all of the values at the end
Total: 13

2^0 =   1 =        1
2^1 =   2 =       10
2^2 =   4 =      100
2^3 =   8 =     1000
"""