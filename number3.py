def pattern(k):
    num=1
    
    for i in range (k+1):
        #print(i)
        for j in  range (i):
            
            print(f"{num}", end=" ")
            num+=1
        print("")    
        
k=5
pattern(k)     