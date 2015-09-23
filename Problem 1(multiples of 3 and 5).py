var = 1000
ans = 0

while(var>0):
    var = var-1
    if(var%3 == 0 or var%5 == 0):
        ans = ans + var

    

print("final: " + str(ans))
