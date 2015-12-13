from sys import exit
from os.path import exists # if a file exists, returns TRUE else FALSE
prompt = '>'


#def AddOne(yes,info)	#  passing in agreement to add a record, returning the record information.

def parser(x,text_file):
	l = []
	for line in text_file:
		l = line.split(" ")
		print l
		
		
	

## get the file which has 

print "Which file do you want to use for input?" 
filename = raw_input(prompt)
print "Filename %r." % filename  
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
raw_input("?")



print "Opening the file..."
text_file = open(filename, 'r') # open the filename object in read mode
lines = text_file.readlines() # this will return the correct ount on the number of lines with the len function
								# however, it will only return all the data in one line

print "\nThe variable 'text_file' is %r " % text_file
print "The variable 'filename' is %r \n" % filename
print len(lines) # gives how many lines are in the file.
		#prints out the data in the file
x = len(lines)

lista = parser(x,text_file)
print lista

print("\nAnd finally, we close it.")
text_file.close()



