'''
Created 2020
Even Fibonacci numbers
@author: Pranaw Bajracharya
'''

#Fibonacci Sequence function (0,1,1,2,3,5,8, ...)
#Inputs: n (the number in the sequence)
#Output: y (The Value of the specified number in the sequence)
def fibonacci(n):
        #Negative inputs are not allowed
        if n <= 0:
            return 
        #Technically the value of the 1st term in the sequence starts at 0 
        if n == 1:
            return 0
        #The second number is inherently 1 in the sequence
        if n == 2:
            return 1
        #Calculates the values of the sequence beyond the second number
        if n > 2:
            # y (value of the current sequence number) = (value of previous sequence number) + (value of the sequence number two before)
            y = fibonacci(n-2) + fibonacci(n-1)
            return y
#Integer that stores the sum of fibonacci numbers under 4 million
m = 0

#Calculates all fibonacci numbers until the (arbitrarily large) 99th number
for x in range(1, 100):
    #Checks to see if the value of the current number under 4 million and an even number
    if fibonacci(x) < 4000000 and fibonacci(x) % 2:
        #Adds the current number to the previous sum
        m = m + fibonacci(x)  
    #Prints out the progress the program is making through the range
    print(x)
#Prints out the value of the calculated su 
print(m)
