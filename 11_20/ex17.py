from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

in_file = open(from_file)
indata = in_file.read()

print "Do	es the output file exist? %r" % exists(to_file)

out_file = open(to_file, 'w')
out_file.write(indata)

out_file.close()
in_file.close()

# quick note indata = open(from_file).read() closes this file once it has been read, but
# the way I've coded it above does not
