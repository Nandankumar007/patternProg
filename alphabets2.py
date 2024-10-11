# num=0
# for i in range(7,1,-1):
#     for j in range(i):
#         print(chr(65+j),end="")
#         #num+=1
#     print("")    
# ABCDEFG
# ABCDEF
# ABCDE
# ABCD
# ABC
# AB


num=0
for i in range(7):
    for j in range(i):
        print(chr(64+i),end="")
        #num+=1
    print("")
# A
# BB
# CCC
# DDDD
# EEEEE
# FFFFFF 