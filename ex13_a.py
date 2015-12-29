from sys import argv

script, first = argv

print "The name of the script is:", script
print "The mandatory argument is:", first

# optional third argument
optional_second = raw_input("Optional argument: ")

print "You said %s is the optional argument." % optional_second
