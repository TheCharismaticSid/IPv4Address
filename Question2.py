#WAP to find factorial of a given number.
'''fact=1
x=int(input("Enter the number you want to find the factorial of : "))
if x==0:
    print("The factorial of 0 is 1")
else :
    for i in range(1,x+1):  #looked up the code for the for loop as i am still not used to this loop in python
        fact=fact*i
    print("The factorial of ",x," is ",fact)
input("Press Any key to exit the program")'''
import math
x=int(input("Enter the number : "))
print(math.factorial(x))

