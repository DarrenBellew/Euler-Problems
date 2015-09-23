#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.

val = 1
lastval = 1
ans = 0


while(val < 4000000):

    if(val % 2 == 0):
        ans = ans+val
    
    temp = val
    val = val+lastval
    lastval = temp

print ("Final: " +  str(ans))

