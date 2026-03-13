import math

def prime(x):
    if x < 2:
        return False
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

count = 0

for n in range(7,1000,2):

    found = False
    
    for a in range(2,n):
        for b in range(2,n):
            
            c = n - a - b
            
            if prime(a) and prime(b) and prime(c):
                print(n,"=",a,"+",b,"+",c)
                count += 1
                found = True
                break
        
        if found:
            break

print("Co",count,"so nguyen le thoa man")
