#from sys import argv
from os.path import exists # if a file exists, returns TRUE else FALSE
prompt = '>'

print "Which file do you want to use for input?" 
from_file = raw_input(prompt)

print "Which file do you want to use for output?" 
to_file = raw_input(prompt)

#script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

#we could do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file really exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

out_file = open(to_file)
outdata = out_file.read()

print "Alright, all done"

#delete text from in_file
in_file = open(from_file, 'w')
in_file.truncate()

#read new file lengths
in_file = open(from_file)
indata = in_file.read()

print "The input file %s is now %d bytes long" % (in_file, len(indata))
print "The output file %s is now %d bytes long" % (out_file, len(outdata))

out_file.close()
in_file.close()
