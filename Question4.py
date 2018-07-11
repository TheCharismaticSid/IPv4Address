#WAP to take input of sequence of comma-seprated numbers and generate a list and a tuple like :-
# ['1','2','3']
#('1','2','3')
values=input()
list=values.split(",")   #looked for a way to split , on internet found this split function
tuple=tuple(list)      #used the hint from the mail
print (list)
print (tuple)
