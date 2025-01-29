import sys
import math
def do_stuff():
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])

    d = b**2 - 4*a*c
    if d > 0:
        root1 = (-b + math.sqrt(d)) / (2*a)
        root2 = (-b - math.sqrt(d)) / (2*a)
        print(f'The solutions are: {root1}, {root2}')
    elif d == 0:
        root = -b / (2*a)
        print(f'The solution is: {root}')
    else:
        print('There are no real solutions.')   

do_stuff() 
#(i)the codes purpose is to compute the quadratic formula given 3 arguments.

# (ii)the errors withen the code are that it is possible for us to have a=0 which results in an error as our code does not account for division by 0.
# also the code does not check for how many arguments were provided which could lead in failure to run.
# also the closing apostrophes did not match the opening reseluting in an error
