#WAP to find all no.s divisible by 7 and are not multiple of 5 btw 2000 & 3200
for x in range(2000,3200):    #loop will check between 2000,3200
    if(x%7)==0:                   
        y=x/5.0                           
        if(y%5)!=0:
            print(x)
