def pattern(k):
    for i in range (k+1):
        for n in range (1,i+1):
            print(f"{n}", end=" ")
        print("")    
        
k=15
pattern(k)       