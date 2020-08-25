'''
Created on Aug 23, 2020
Calculate Largest Palindrome of the product of two three digit numbers
@author: Pranaw Bajracharya
'''

"""
Since the question is find the largest palindrome of the product of two three digit numbers,
I suppose the simplest/most brute force method would be to find the minimum and maximum value of
the product of two three digit numbers. The smallest three digit number is 100 and the greatest
is 999. Thus, the palindrome will be between 100*100 and 999*999.

I'm guessing it would be a lot closer to the 999*999 so we will start from there and move down,
checking to see if the numbers in between are palindromes.

"""

import sys

maximum = 999
minimum = 100

for x in range(maximum,minimum,-1):
    for y in range(maximum,minimum,-1):
        multiplied = x * y
              
        number = str(multiplied)
        length = len(number)
        
        first, second = number[:length//2], number[length//2:]
                    
        if(first[::-1] == second):
            print(number)
           
