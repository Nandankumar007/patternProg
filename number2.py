def pattern(k):
    for i in range (1,k+1):
        #print(i)
        for n in range (i):
            print(f"{i}", end=" ")
        print("")    
        
k=5
pattern(k)       


#for i in range (k+1):
        # _      one space will be there first
        # 1
        # 2 2
        # 3 3 3
        # 4 4 4 4
        # 5 5 5 5 5

#for i in range (1,k+1):
        #1 
        #2 2
        #3 3 3
        #4 4 4 4
        #5 5 5 5 5