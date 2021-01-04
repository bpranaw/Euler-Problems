'''
Created on Jan 3, 2021
Find the difference between the sum of all the squares of natural numbers and the
square of the sum of natural numbers between 1-100
@author: Pranaw Bajracharya
'''

"""
I've been considering speed on this one. I think we would have to cycle through
all the values between 1-100 anyways but only doing that once would save time,
making the time complexity O(n)
"""

#This variable is the sum of the squares of natural numbers
natural_square_sum = 0.0

#This variable is the square of the sum of natural numbers
square_of_natural_sum = 0.0

for x in range(1,101):
    natural_square_sum += x*x
    square_of_natural_sum += x
    
square_of_natural_sum = square_of_natural_sum * square_of_natural_sum

difference = abs(square_of_natural_sum - natural_square_sum)

print("Difference: " + str(difference))

