'''
Created 2019
Multiples of 3 and 5
@author: Pranaw Bajracharya
'''

#Variables(x is the number that are tested for divisibility by 3 or 5, and y is the sum of all those numbers within the range)
y = 0 
x = 0
    
#Loop that cycles from x=0 to x=1001 (meaning it goes from 0 to 1000)
for x in range(0,1001):
    #Checks to see if number is divisible by 3 or 5 evenly
    if x % 5 == 0 or x % 3 == 0:
        #If so, it adds current number to the sum
        y = y + x
            
#Prints total sum
print(y)
