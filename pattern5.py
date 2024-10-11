

def pattern(num):
    ke=0
    for i in range(1,num):
        for j in range(num-i):
            print(" ",end="")
        for k in range (i+ke):
            print("*",end="")
            
        print("")
        ke+=1
num=10
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