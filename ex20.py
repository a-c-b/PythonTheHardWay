#Functions are defined at the top of the script.  No values
# are held until the function is called.

from sys import argv  ## will need to pass a file name in the same directory

script, input_file = argv
# This function receives the file and does a read of the file.  
def print_all(f):# f variable is used for files.  A file in Python is like an old tape drive.  
	print f.read() # this is a read head
	
# This function moves to the start of a file	
def rewind(f):
	f.seek(0) #f.seek(0) moves you to the start of a file

# This function reads in the line of interest and returns the line number
#  it is looking to accept two variables, one which is called line_count,
# the second is a file
def print_a_line(line_count, f):
	print line_count, f.readline()
	return line_count
## End of functions 



# Begin Script
## assigns current_file the file from the argv	
current_file = open(input_file)

print "First let's print the whole file:\n"
## call the print_all function and send it the value from the variable held in current_file
print_all(current_file)

#take the file back to the beginning.
print "Now let's rewind, kind of like a tape."
rewind(current_file)

print "Let's print three lines: "
#set the variable to the first line
current_line = 1

#call the function print_a_line and send it the number 1 
#to read the first line from the file held in current_file
# The variable current_line will be assigned to the variable line_count once it is sent to the function
print_a_line(current_line,current_file)

#current_line = current_line+1
current_line+=1
print_a_line(current_line,current_file)

#current_line = current_line+1
current_line+=1
print_a_line(current_line, current_file)



# First let's print the whole file:

# line1
# line2
# line3
# line4
# line5
# line6
# line7
# line8
# line9
# line10

# Now let's rewind, kind of like a tape.
# Let's print three lines:
# 1 line1

# 2 line2

# 3 line3