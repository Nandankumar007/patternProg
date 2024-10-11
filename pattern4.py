def pat(rw):
    raw=rw
    for i in range(1,rw+1):
        for n in range(raw-i):
            
            print(" ",end="") 
        for m in range(i):
                print("* ",end="")     
        print("")    
rw=10
pat(rw)        
