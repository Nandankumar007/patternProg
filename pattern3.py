

def pat(rw):
    for i in range(1,rw+1):
        for n in range(1,rw+1):
            if n+i<=rw:
                print(" ",end="") 
            else:
                print("*",end="")     
        print("")    
rw=4
pat(rw)        



