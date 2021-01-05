
'''
Created on Jan 2, 2021
Calculate the smallest number that is evenly divisible by all the numbers 1-20
@author: Pranaw Bajracharya
'''

"""
Theoretically we could just do this by counting by 1, but since the number we are 
looking for is divisble by 20 evenly, that means that we can find it by incrementing by 20. 
This will be faster

"""

#This is just a default to check if something is wrong
number = 0

#This variable allows the loop to continue until we have found the number in quesiton
is_found = False

#Loops until we have found the number
while is_found == False:

	#Increments by 20 because 20 is greatest increment value for the given conditions
	#but also the limiting factor when determining the SMALLEST possible number for the conditions
	number += 20
	print("Current Number: " + str(number))

	#Means we have found the number if this is unchanged
	is_divisible = True
		
	#This is for checking if the current number is divisible by 1-20
	index = 1

	#Checks to see if the current number is evenly divisible by all the numbers
	while is_divisible == True and index < 20:
		if number % index != 0:
			is_divisible = False
		else:
			index += 1
	
	#This is the condition that we have found the number in quesiton
	#The number is printed out and the loop is stopped
	if is_divisible:
		is_found = True
		print("Smallest number evenly divisible by 1-20: " + str(number))

