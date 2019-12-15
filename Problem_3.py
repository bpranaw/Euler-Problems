'''
Created on Dec 12, 2019
Calculate Largest Prime Factor
@author: Pranaw Bajracharya
'''

#The variable being tested
t = 600851475143

#Prime Number Checker
#Inputs: x (the number it is checking)
#Outputs: True (means the number is "prime") or False (Means the number is not prime)
#Notes: Unfortunately, this function does not catch numbers that are products of prime numbers
def checkIfPrime(x):
    #Checks to see if the number is any of the prime numbers from 1-10 and returns true if they are
    if x == 2 or x == 5 or x == 7:
        return True
    #Checks to see the number is not divisible by 2,3,5, or 7 (4 is divisible by 2, 6 and 9 by 3, therefore this isolate the prime numbers)
    if x % 2 != 0 and x % 3 != 0 and x % 5 != 0 and x % 7 != 0:
        return True
    return False

#Semiprime number check (checkIfPrime isolated the prime numbers to an extent, but it does factor in numbers that are products of prime numbers)
#Inputs: x (The prime number it is checking)
#Outputs: True (means number is "semiprime") or False (means number is prime)
def checkIfSemiprime(x):
    #Checks to see if the input is prime and ends the function with a message if it isn't
    if checkIfPrime(x) == False:
        print("This is not a prime number")
        return 
    #Checks to see if the number is "prime" with checkIfPrime()   
    if checkIfPrime(x) == True:
        #For loop that goes from 2 to x-1
        for z in range(2,x):
            #Checks to see if any of those numbers are factors of x
            if x % z == 0:
                #Returns True if those factors are prime (means the x is actually semiprime)
                if checkIfPrime(z) == True:
                    return True
    #Returns False because no semiprime numbers were found
    return False

#For loop that runs from 1 to the number to calculate all the prime factors of the number
for m in range(1,t+1):
    #Checks to see if m is a factor of the number, if m is prime, and if m is not semiprime
    if t % m == 0 and checkIfPrime(m) == True and checkIfSemiprime(m) == False:
        #Prints out the factor
        print(m)     
