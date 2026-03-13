for a in range(1,100):
    for b in range(a+1,100):
        for c in range(b+1,100):
            
            if a*a + b*b == c*c:
                
                if (a+1==b and b+1==c):
                    print((a,b,c),": ba so nguyen lien tiep")
                
                if (a+2==b and b+2==c):
                    print((a,b,c),": ba so cach nhau 2")
