# traditional method where the module is imported and I use the method defined below
def replace_while(top, iterator):
    i = 0
    numbers = []

    while i < float(top):
        print "At the top i is %d:" % i
        numbers.append(i)

        i += float(iterator)
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i


    print "The numbers: "

    for num in numbers:
        print num
