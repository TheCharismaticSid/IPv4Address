'''Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24'''
#Program
import math     #for the sqroot function
c=50
h=30
def calc(d):
    d=int(d)
    return sqrt((2*c*d)/h)

d=input().split(',')
d=list(map(calc,d))
print(",".join(d))

