from sys import argv

script, filename = argv

print "We're goingt to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input('?')

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going toask you for three lines."

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "I'm going to write these to the file."

contents = """%s
%s
%s
""" % (line1, line2, line3)

target.write(contents)

print "And finally, we close it."
target.close()
