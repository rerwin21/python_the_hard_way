# This method takes arguments from the command line
from sys import argv

script, top, iterator = argv

def replace_while(top, iterator):
    i = 0
    numbers = []

    while i < int(top):
        print "At the top i is %d:" % i
        numbers.append(i)

        i += int(iterator)
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i


    print "The numbers: "

    for num in numbers:
        print num


replace_while(top, iterator)



