


for i in range( 5):
    for j in range(i):
        print("* ", end=" ")
    print("")


# Without end="", the print("* ") would print * and
# then move to the next line each time.

# With end="", * is printed on the same line multiple times ,
# allowing you to control when a new line starts manually 
# (in this case, with the separate print("") statement outside the inner loop).