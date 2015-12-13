from sys import argv

script, filename = argv  ## will need to pass a file name when calling ex16.py
		## use a dead file or it will be overwritten
print "We're going to erase %r." % filename  
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
#target = open(filename) #open without the 'w' attribute.  Truncate function FAILS
target = open(filename, 'w') # open the filename object in write mode
								#truncates the file even without the '+' option

print "The variable 'target' is %r " % target
print "The variable 'filename' is %r " % filename
print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file"

# target.write(line1)
# target.write("\n")  #line break
# target.write(line2)
# target.write("\n")  #line break
# target.write(line3)
# target.write("\n")  #line break

#question3 code
#remove the repetition from the write statements above
new_file = "%r\n%r\n%r\n" % (line1, line2, line3)
#print new_file
target.write(new_file)

print("And finally, we close it.")
target.close()



