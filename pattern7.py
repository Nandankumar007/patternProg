
def pattern(num):
    ke=0
    for i in range(1,num):
        for j in range(num-i):
            print(" ",end="")
        for k in range (i+ke):
            print("*",end="")
            
        print("")
        ke+=1
num=7
pattern(num)          



def pattern(num):
    # ke=(num*2)-1
    for i in range(num,0,-1):
        for j in range(num-i):
            print(" ",end="")
        for k in range ((i*2)-1):
            print("*",end="")
            
        print("")
        # ke+=1
num=7
pattern(num)          

#          *
#         ***
#        *****
#       *******
#      *********
#     ***********
#    *************
#   ***************
#  *****************
# *******************
#  *****************
#   ***************
#    *************
#     ***********
#      *********
#       *******
#        *****
#         ***
#          *