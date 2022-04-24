import sys


def show_sales(*args):
    from itertools import islice
    if len(args) == 0:
        with open("bakery.csv", "r") as show:
            s = show.read()
        return s
    elif len(args) == 1:
        with open("bakery.csv") as show:
            s = islice(show, args[0]-1, None)
            print(*s)
        return exit(0)
    elif len(args) == 2 and args[0] < args[1]:
        with open("bakery.csv") as show:
            s = islice(show, args[0]-1, args[1])
            print(*s)
        return exit(0)
    else:
        return exit(1)






#print(show_sales())
#print(show_sales(2, 3))
print(show_sales(4))

