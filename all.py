#python -m pydoc raw_input
##
#python help directory
# python -m pydoc raw_input  *** or whatever other command you want to use.  Do this at the powershell

## to get into python, just type in the word "python"
## you can run little pieces of the code this way.
## to exit, type quit()

## NOTATIONS:
# += adds another value with the variable's value and assigns the new value to the variable.

# >>> x = 3
# >>> x += 2
# >>> print x
# 5
# -=, *=, /= does similar for subtraction, multiplication and division.
####





#EX1.PY
print "Hello World!"
print "Hello Again"
print "I like typing this"
print "This is fun"
print 'Yay! Printing'
print "I'd much rather you 'not'."
print 'I "said" do not touch this.'

# Hello World!
# Hello Again
# I like typing this
# This is fun
# Yay! Printing
# I'd much rather you 'not'.
# I "said" do not touch this.

*********************************************************

# EX3.PY
## between quotes is the text.  Comma separated for the calculation which 
## will then print a result.

print "I will now count my chickens:"

print "Hens", 25+30/6
print "Roosters", 100-25* 3 %4

print "Now I will count the eggs:"

print 3+2+1 - 5 + 4 % 2 -1 / 4 + 6

print "Is it true that 3+2 < 5 -7?"

print 3 + 2 < 5 - 7

print "What is 3+2?", 3+2
print "What is 5-7?", 5-7

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5>=-2
print "Is it less or equal", 5 >= -2
print "Is it less or equal?", 5<= -2

# I will now count my chickens:
# Hens 30
# Roosters 97
# Now I will count the eggs:
# 7
# Is it true that 3+2 < 5 -7?
# False
# What is 3+2? 5
# What is 5-7? -2
# Oh, that's why it's False.
# How about some more.
# Is it greater? True
# Is it less or equal True
# Is it less or equal? False

*********************************************************

# EX4.PY
## SETTING NUMERIC VARIABLE values

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available"
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today"
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# There are 100 cars available.
# There are only 30 drivers available
# There will be 70 empty cars today.
# We can transport 120.0 people today
# We have 90 to carpool today.
# We need to put about 3 in each car.

*********************************************************

# EX5.PY
## syntax for inserting variables or multiple variables in a line
## setting text variable values - uses a SINGLE quote
my_name = 'Zed A. Shaw'
my_age = 35 #not a lie
my_height = 74 # inches
my_weight = 180 #lbs
my_eyes = 'Blue'
my_teeth = 'White' 
my_hair = 'Brown'
# %s looks to determine string type
#%d looks to reference the decimal number after the % sign
#%d is decimal

#no need to use parenthesis when passing a single variable
## when passing multiple variables, use parenthesis

print "Let's talk about %s." % my_name
print "He's %d inches tall."  % my_height
print "He's %d pounds heavy." % my_weight
print "Actually, that's not too heavy." 
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	my_age, my_height, my_weight, my_age + my_height + my_weight)
	
	
# Let's talk about Zed A. Shaw.
# He's 74 inches tall.
# He's 180 pounds heavy.
# Actually, that's not too heavy.
# He's got Blue eyes and Brown hair.
# His teeth are usually White depending on the coffee.
# If I add 35, 74, and 180 I get 289.

*********************************************************	

#EX6.PY

x = "There are %d types of people." % 10 # %d looks to reference the decimal number 10 after the % sign
#%d is decimal
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." %(binary, do_not) # %s looks to determine string type

print x
print y

print "I said: %r."% x  # % r is raw data - use for debugging
print "I also said:  '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e 
#ex6.py renamed, p.30
# There are 10 types of people.
# Those who know binary and those who don't.
# I said: 'There are 10 types of people.'.
# I also said:  'Those who know binary and those who don't.'.
# Isn't that joke so funny?! False
# This is the left side of...a string with a right side.

*********************************************************

#  EX7.PY

print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."
print "." * 10 # what'd that do?  This will print 10 periods.

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

#watch that comma at the end after the word "end6".  try removing it and see what happens
## What happens is that when there is a comma after the word
## 'end6' then the two lines below print on one line.
## when the comma is removed, then Cheese Burger is printed
## on two lines

print end1 + end2 + end3 + end4 + end5 + end6#,
print end7 + end8 + end9 + end10 + end11 + end12

# Mary had a little lamb.
# Its fleece was white as snow.
# And everywhere that Mary went.
# ..........
# Cheese
# Burger

*********************************************************

#EX8.PY

formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)
#  file also named print formatter.py

# for weird characters (non-ascii), use %s to print.  %s should usually be used and only use
# %r for debugging information about something.  The %r will give you the 'raw programmer's'
# version of the variable, also known as the representation.

#%r = raw programmer version of the variable, the representation
#%s = string



# 1 2 3 4
# 'one' 'two' 'three' 'four'
# True False False True
# '%r %r %r %r' '%r %r %r %r' '%r %r %r %r' '%r %r %r %r'
# 'I had this thing.' 'That you could type up right.' "But it didn't sing." 'So I said goodnight.'

*********************************************************

#EX9.PY

# Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"  # if you wanted Jan to start on a new line, then lead with \nJan, etc.
#\n = newline

## pay attention to the use of the comma.
## here is the first time it's used.  It's in
##passing a variable without an internal
## reference like %s or %d or %r
## in those cases, there is NO COMMA

print "Here are the days:", days
print "Here are the months:", months

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5 or 6
"""

# Here are the days: Mon Tue Wed Thu Fri Sat Sun
# Here are the months: Jan
# Feb
# Mar
# Apr
# May
# Jun
# Jul
# Aug

# There's something going on here.
# With the three double-quotes.
# We'll be able to type as much as we like.
# Even 4 lines if we want, or 5 or 6

*********************************************************

#EX10.PY

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split \non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

        # I'm tabbed in.
# I'm split
# on a line.
# I'm \ a \ cat.

# I'll do a list:
        # * Cat food
        # * Fishies
        # * Catnip
        # * Grass


# escape sequences: the way we put difficult to type characters into a string.
# double backslash \\ will print just one backslash.
# escape sequence for quotes:
# print "I am 6'2\" tall." #escape double-quote inside string.
# print 'I am 6\'2" tall.' # escape single quote inside string.
# I am 6'2" tall.
# I am 6'2" tall.

*********************************************************

# Escape sequences	What it does.
# \\ 	Backslash ()
# \' 	Single-quote (')
# \" 	Double-quote (")
# \a 	ASCII bell (BEL)
# \b 	ASCII backspace (BS)
# \f 	ASCII formfeed (FF)
# \n 	ASCII linefeed (LF)
# \N{name} 	Character named name in the Unicode database (Unicode only)
# \r ASCII 	Carriage Return (CR)
# \t ASCII 	Horizontal Tab (TAB)
# \uxxxx 	Character with 16-bit hex value xxxx (Unicode only)
# \Uxxxxxxxx 	Character with 32-bit hex value xxxxxxxx (Unicode only)
# \v 	ASCII vertical tab (VT)
# \ooo 	Character with octal value ooo
# \xhh 	Character with hex value hh

## The code below :
## needs to have colons at the end of the lines
## you will need to break (^C) to get out of the output
## which is a spinning slash/dash
		while True:
	for i in [ "/", "-", "|", "\\", "|"]:
		print "%s\r" % i,

************************************************************

#EX11.PY
print "How old are you?",
age = raw_input ()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)
	
# How old are you? 23
# How tall are you? 5'4"
# How much do you weigh? 130
# So, you're '23' old, '5\'4"' tall and '130' heavy.


*******************************************************************

#EX12.PY
##Prompting for input and capturing the variables.
## the variable is assigned the value 
## response to the prompt

age = raw_input ("How old are you? ")
height = raw_input("how tall are you? ")
weight = raw_input("how much do you weight? ")

print "So, you're %r  old, %r tall and %r heavy." % (
	age, height, weight)
	
# How old are you? 23
# how tall are you? 5'4"
# how much do you weight? 135
# So, you're '23'  old, '5\'4"' tall and '135' heavy.

*******************************************************************
			#EX13.PY
## sys is a package and we're pulling the argv feature.			
from sys import argv
#below is line 3
script, first, second, third = argv #script is a reserved word and will return the name of ex13.py.  Three other words need to be submitted
									# in the command line:  python ex13.py word1 word2 word3 - or an error will be returned
## commas used here to pass the variables
## because there is no internal call to the variable
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

## introduces the argv - argument variable
## 'import' adds features aka modules aka libraries to your script from the Python
## feature set.  

## argv - the argument variable holds the arguments
# you pass to your python script

## line 3 "unpacks" argv so that rather than holding
## all the arguments, it gets assigned to variables
#you can work with from the left in order.

## to get the script to run, you have to modify 
## your command line so that instead of just typing:
## python ex13.py
## you must instead type:
## python ex13.py word1 word2 word3
## because the word 'script' refers
## to the python filename itself

## for the first results of the exercise
## you were to type:
#python ex13.py first 2nd 3rd

# PS C:\Users\Andrea\mystuff> python ex13.py word1 word2 word3
# The script is called: ex13.py
# Your first variable is: word1
# Your second variable is: word2
# Your third variable is: word3
 
 ## THE ERROR you would get if you don't pass the correct number of variables in
 ## would tell you that 'you need more than 3 values' to unpack'
 
#python ex13.py first 2nd 3rd

# The script is called: ex13.py
# Your first variable is: first
# Your second variable is: 2nd
# Your third variable is: 3rd

# python ex13.py apple orange grapefruit
# The script is called: ex13.py
# Your first variable is: apple
# Your second variable is: orange
# Your third variable is: grapefruit


#**********ex13extra.py*********************************

#Question #3 
#combine raw_input with argv to make a script that gets more input from a user

from sys import argv
party = raw_input("What is your political party?  ")
sex = raw_input ("What is your sex?  ")

script, color, love = argv
## cases where will be NO COMMA between the print text
## and the passed variables
print "My favorite color is: %s.  Even though I am a %s" % (color, sex)
print "And on the same line is the name of my love:  %s." % love
print "I am a %s." % sex,
print "The file name is %s" % script

## cases where a COMMA MUST be used between
## the print text and the variables

print "" #blank line
print "" #blank line
print "Need a comma between string and variable:", color
print "Another example is", love, " is a ", sex

#************EX14.PY ***********************
# passing variables and taking input
# argv is the argument variable - passes variables in

## will need to type python ex14.py Andrea 
## to send Andrea - the user name to the argv

from sys import argv

script, user_name = argv
prompt = '>'

print "Hi %s, I'm the % script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
## the line below sends the prompt to the screen
## and waits for input from the user


print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer.  Nice.
""" % (likes, lives, computer)

#***********ex15.py*******************************

## new syntax:
# open(somefile)
#somefile.read()

### need to add a filename to the python ex15.py ex15.py

## this prints the text of the file you tell it to
## within the working directory you're in.
from sys import argv

#argv collects the script name from the system
# and the filename from what's input by the user
#when calling ex15.py

##always need to call 'script' first
script, filename = argv 

# the txt variable collects the code of the file
# you've said you want to collect.
txt = open(filename)

# this prints the file's name
print "Here's your file %r:" % filename

# this prints the text of the script from variable txt
print txt.read()

#prompts for a new file name
print "Type the filename again:"

## file_again FILE created from the input
file_again = raw_input("> ")## prompt awaiting user input

#load the data from the FILE into variable txt_again
txt_again = open (file_again)
#print the data from text_again with the .read extension
print txt_again.read()

## close the files after you've operated on them
txt_again.close()
txt.close()


#********** ex16.py *********************
## working with files
# close -- Closes the file. Like File->Save.. in your editor.
# ◦read -- Reads the contents of the file. You can assign the result to a variable.
# ◦readline -- Reads just one line of a text file.
# ◦truncate -- Empties the file. Watch out if you care about the file.
# ◦write('stuff') -- Writes "stuff" to the file.
# You only need to remember that write takes a parameter of a string you want to write to the file.



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

target.write(line1)
target.write("\n")  #line break
target.write(line2)
target.write("\n")  #line break
target.write(line3)
target.write("\n")  #line break

print("And finally, we close it.")
target.close()


#question3 code
#remove the repetition from the write statements above
new_file = "%r\n%r\n%r\n" % (line1, line2, line3)
#print new_file
target.write(new_file)

print("And finally, we close it.")
target.close()

#question 4 -
# We had to pass a 'w' as an extra parameter or truncate won't work.
# I don't understand why we used truncate when w truncated anyway.



## open the file
# target = open(filename, 'w')
##then do stuff
# target.truncate()
# target.write(stuff)
# target.read
# target.readline
# target.close()




#*******ex17.py************

# semi-colons are used to combine python statements
# onto a single line

from sys import argv
script, from_file, to_file = argv
#we could do these two on one line too, how?
in_file = open(from_file); indata = in_file.read()
out_file = open(to_file, 'w'); out_file.write(indata)
out_file.close(); in_file.close()

### ex17 extended and played with
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


**************ex18.py**************************

# this one is like your scripts with argv
def print_two(*args): 
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#okay, that *args is actually pointless, we can just do this
def print_two_again (arg1, arg2):
    print"arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

#this one takes no arguments
def print_none():
    print "I got nothin'."


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()


##  with Notepad - the use of tab for indentation causes
## indentation errors.  In Notepad under the EDIT / Blank Operations - you will find a convert tab to space

	#the star args *args operates like the argv parameter but for functions.  It must be between the parens
	#all function lines have to end with the colon
	#all lines indented 4 spaces will become attached to the function


# PS C:\Users\Andrea\mystuff> python ex18.py
# arg1: 'Zed', arg2: 'Shaw'
# arg1: 'Zed', arg2: 'Shaw'
# arg1: 'First!'
# I got nothin'.

#************EX19.PY***************************
## different ways to call functions and use variables 

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"
    

print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)


print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
cheese_and_crackers(10+20, 5+6)


print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers + 1000)

#********************EX20.PY***************************
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


########    EX21.PY ***************

def add(a,b):
	print "ADDING %d + %d" % (a,b)
	return a+b
	
def subtract(a,b):
	print "SUBTRACTING %d - %d" %(a,b)
	return a-b
	
def multiply(a,b):
	print "MULTIPLYING %d * %d" % (a,b)
	return a*b

def divide (a,b):
	print "DIVIDING %d / %d" % (a,b)
	return a/b
	

print "Let's do some math with just functions!"

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" %(age, height, weight, iq)

# a puzzle for the extra credit, type it anyway.
print "\nHere is a puzzle"

what = add (age, subtract(height, multiply(weight, divide(iq,2))))

print "That becomes: ", what, "Can you do it by hand?"

################  boxsize.py ************************
#Practice on functions, printing and returning values

def WOS(deep, wide, long):
#	print "Width of stock = "
	return (2*deep) + long
def LOS(deep, wide, long):
	return (3*deep) + (2*wide)
	


depth = raw_input ("How deep is the box? ") # a variable
width = raw_input("How wide is the card? ") #b variable
length = raw_input("How long is the card? ") #c variable
slop_width = raw_input("How much extra space do you want on the width? ")
slop_length = raw_input("How much extra space do you want on the length? ")


# depth = 1
# width = 4
# length = 6 

a = float(depth)
b = float(width)+float(slop_width)
c = float(length)+float(slop_length)

print "So, your box ", depth, "inches deep, ", width, " wide,  and ", length, " long." 
#likes = raw_input(prompt)

print "%r deep" % a
print  "%r wide" % b
print "%r long" % c

# call the function and send the dimensionsbox_dim.  Set the return value to a new variable
width_of_stock = WOS(a,b,c)
length_of_stock = LOS(a,b,c)
# width_of_stock = (2*a) + c
# length_of_stock = (3*a) + (2*b)

print "Width of stock = ", width_of_stock 
print "Length of stock = ", length_of_stock 
print "The card stock would need to be n%r\n%r\n wide by %f long." % (width_of_stock, length_of_stock)


## BETTER VERSION OF BOXSIZE.PY

def WOS(deep, wide, long):
	print "Width of stock = %.2f inches" % ((2*deep) + long) #wide variable goes unused
	return (2*deep) + long
def LOS(deep, wide, long):
	print "Length of stock = %.2f inches" % ((3*deep) + (2*wide))#long variable goes unused
	return (3*deep) + (2*wide)
	


depth = raw_input ("\nHow deep is the box? ") # a variable
width = raw_input("How wide is the card? ") #b variable
length = raw_input("How long is the card? ") #c variable
slop_width = raw_input("\nNow, how much extra space do you want on the width? ")
slop_length = raw_input("How much extra space do you want on the length? ")


a = float(depth)
b = float(width)+float(slop_width)
c = float(length)+float(slop_length)

print "\nSo, your box of %r inches deep x %r inches wide x %r inches long " % (depth, width, length)
print "will be spec'd at %.2f inches deep, %.2f inches wide, %.2f inches long\n\n" % (a,b,c)
#likes = raw_input(prompt)



# call the function and send the dimensionsbox_dim.  Set the return value to a new variable
width_of_stock = WOS(a,b,c)
length_of_stock = LOS(a,b,c)
# width_of_stock = (2*a) + c
# length_of_stock = (3*a) + (2*b)

print "The card stock would need to be %.2f inches wide by %.2f inches long.\n\n" % (width_of_stock, length_of_stock)

###############   EX21.PY

def add(a,b):
	print "ADDING %d + %d" % (a,b)
	return a+b
	
def subtract(a,b):
	print "SUBTRACTING %d - %d" %(a,b)
	return a-b
	
def multiply(a,b):
	print "MULTIPLYING %d * %d" % (a,b)
	return a*b

def divide (a,b):
	print "DIVIDING %d / %d" % (a,b)
	return a/b
	

print "Let's do some math with just functions!"

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" %(age, height, weight, iq)

# a puzzle for the extra credit, type it anyway.
print "\nHere is a puzzle"

what = add (age, subtract(height, multiply(weight, divide(iq,2))))

print "That becomes: ", what, "Can you do it by hand?"

##
# Let's do some math with just functions!
# ADDING 30 + 5
# SUBTRACTING 78 - 4
# MULTIPLYING 90 * 2
# DIVIDING 100 / 2
# Age: 35, Height: 74, Weight: 180, IQ: 50

# Here is a puzzle
# DIVIDING 50 / 2
# MULTIPLYING 180 * 25
# SUBTRACTING 74 - 4500
# ADDING 35 + -4426
# That becomes:  -4391 Can you do it by hand?

#********************  EX24.PY (no 22 or 23) *********

print "\n\nLet's practice everything."

#make sure there are no spaces between some of those single quote chars
print 'You\'d need to know \'bout escapes with \\ that do \n new lines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires and explanation
\n\twhere there is none.
"""

print "\n\n------------"
print poem
print "------------\n\n"


five = 10-2+3-6
print "This should be five: %s \n\n" % five

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 1000
	return jelly_beans, jars, crates
	
start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d beans" % start_point
print "We'd have %d beans, %d jars, and %d crates.\n" % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way for %d beans" % start_point
print "We'd have %d beans, %d jars, and %d crates.\n\n\n\n" % secret_formula(start_point)



# PS C:\Users\Andrea\mystuff> python ex24.py


# Let's practice everything.
# You'd need to know 'bout escapes with \ that do
 # new lines and   tabs.


# ------------

        # The lovely world
# with logic so firmly planted
# cannot discern
 # the needs of love
# nor comprehend passion from intuition
# and requires and explanation

        # where there is none.

# ------------


# This should be five: 5


# With a starting point of: 10000 beans
# We'd have 5000000 beans, 5000 jars, and 5 crates.

# We can also do that this way for 1000 beans
# We'd have 500000 beans, 500 jars, and 0 crates.




# PS C:\Users\Andrea\mystuff>

#################### - create functions and make function calls######################
### ex25.py
##################


def break_words(stuff):
	""" This function will break up words for us."""
	words = stuff.split(' ')
	return words

def sort_words(words):
	"""Sorts the words."""
	return sorted(words)

def print_first_word(words):
	"""Prints the first word after popping it off.""" #removes the word from the list
	word = words.pop(0)
	print word

def print_last_word(words):
	"""Prints the last word after popping it off,"""
	word = words.pop(-1)
	print word

def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words"""
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)		#call to another function print_first_words
	print_last_word(words)		#call to another function

def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)


## Once you save your functions, you go to your PowerShell prompt
# type the word 'python' at the prompt in powershell.
# then import the module, ex25 with the import command
# load up your variables  'sentence'
# and	then the other variables will be assigned
# as you calls the various functions

# you can get help for the module by using:  help(ex25)
# or have the definition shown by using help(ex25.function_name)

# When you've made an error in a function, or want to change a function
# in the module, you have to exit out of python with the CTRL-Z.  Changes
# are not automatically loaded.  You make your changes then go back into Python
# and reload your variables.
	
	
# PS C:\Users\Andrea\mystuff> python
# Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import ex25
# >>> ex25.print_first_word(words)
# Traceback (most recent call last):
  # File "<stdin>", line 1, in <module>
# NameError: name 'words' is not defined
# >>> sentence = "All good things come to those who wait."
# >>> words = ex25.break_words(sentence)
# >>> words
# ['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
# >>> ex25.print_first_word(words)
# All
# >>> ex25.print_last_word(words)
# wait.
# >>> sorted_words=ex25.sort_words(words)
# >>> ex25.print_last_word(sorted_words)
# who
# >>> sorted_words = ex25.sort_sentence(sentence)
# >>> sorted_words
# ['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
# >>> ex25.print_first_and_last(sentence)
# Traceback (most recent call last):
  # File "<stdin>", line 1, in <module>
# AttributeError: 'module' object has no attribute 'print_first_and_last'
# >>> import print_first_and_last
# Traceback (most recent call last):
  # File "<stdin>", line 1, in <module>
# ImportError: No module named print_first_and_last
# >>> ex25.print_first_word(words)
# good
# >>> ex25.print_last_word(words)
# who
# >>> words
# ['things', 'come', 'to', 'those']
# >>> sentence
# 'All good things come to those who wait.'
# >>> ex25.print_first_and_last_sorted(sentence)
# All
# who
# >>> sentence
# 'All good things come to those who wait.'
# >>> ex25.print_first_and_last(sentence)
# Traceback (most recent call last):
  # File "<stdin>", line 1, in <module>
# AttributeError: 'module' object has no attribute 'print_first_and_last'
# >>> ex25.print_first_and_last(sentence)
# Traceback (most recent call last):
  # File "<stdin>", line 1, in <module>
# AttributeError: 'module' object has no attribute 'print_first_and_last'
# >>> help(print_first_and_last)
# Traceback (most recent call last):
  # File "<stdin>", line 1, in <module>
# NameError: name 'print_first_and_last' is not defined
# >>> help(print_first_and_last_sorted)
# Traceback (most recent call last):
  # File "<stdin>", line 1, in <module>
# NameError: name 'print_first_and_last_sorted' is not defined
# >>> ex25.print_first_and_last_(sentence)
# All
# wait.

########  EX29.PY  IF statements 
people = 20
cats = 30
dogs = 15


if people < cats:
	print "Too many cats!  The world is doomed!"
	
if people > cats:
	print "Not many cats!  The world is saved!"
	
if people < dogs:
	print "The world is drooled on!"
	
if people > dogs:
	print "The world is dry!"
	

	dogs += 5

if people >= dogs:
	print "People are greater than or equal to dogs."

if people <= dogs:
	print "People are less than or equal to dogs."


if people == dogs:
	print "People are dogs."people = 20
cats = 30
dogs = 15


if people < cats:
	print "Too many cats!  The world is doomed!"
	
if people > cats:
	print "Not many cats!  The world is saved!"
	
if people < dogs:
	print "The world is drooled on!"
	
if people > dogs:
	print "The world is dry!"
	

	dogs += 5

if people >= dogs:
	print "People are greater than or equal to dogs."

if people <= dogs:
	print "People are less than or equal to dogs."


if people == dogs:
	print "People are dogs."

	
##***************************************************

##  ELSE IF statements
### *******ex30

people = 30
cars = 40
buses = 15


if cars > people:
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't decide."
	
if buses > cars:
	print "That's too many buses."
elif buses < cars:
	print "Maybe we could take the buses."
else:
	print "We still can't decide."
	
	
if people > buses:
	print "Alright, let's just take the buses."
else:
	print "Fine, let's stay home then."

##################  EX31.PY - NESTING IF & ELSEIF (ELIF) & ELSE SYNTAX

print "You enter a dark room with two doors.  Do you go through door #1 or door #2?"

door = raw_input ("> ")

if door == "1":
	print "There's a giant bear here eating a cheese cake?  What do you do?"
	print "1.  Take the cake."
	print "2.  Scream at the bear."
	
	bear = raw_input("> ")
	
	if bear == "1":
		print "The bear eats your face off.  Good job!"
	elif bear == "2":
		print "The bear eats your legs off.  Good job!"
	else:  
		print "Well, doing %s is probably better.  Bear runs away." % bear

elif door == "2":
	print "You stare into the endless abyss at Cthulu's retina."
	print "1.  Blueberries"
	print "2.  Yellow jacket clothespins"
	print "3.  Understanding revolvers yelling melodies."
	
	insanity = raw_input("> ")
	
	if insanity == "1" or insanity == "2":
		print "Your body survives powered by the mind of jello.  Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck.  Good job!"
		
else:
	print "You stumble around and fall on a knife and die.  Good job!"
	
###  EX32 LOOPS AND LISTS

the_count = [1,2,3,4,5]	#syntax of a list
fruits = ['apples', 'oranges', 'pears', 'apricots'] #syntax for text list
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
	print "This is count %d" % number
	
# # same as above
for fruit in fruits:
	print "A fruit of type %s" % fruit

# # also we can go through mixed lists too
# # notice we have to use %r since we don't know what's in it
for i in change:
	print "I got %r" % i

# # we can also build lists, first start with an empty one
elements = []

# # then use the range function to do 0 to 5 counts
for i in range (-1,6):
	print "Adding %d to the list." % i
	 # append is a function that lists understand
	elements.append(i)

# # now we can print them out too
for i in elements:
	 print "Element was: %d" %i
	
# This is count 1
# This is count 2
# This is count 3
# This is count 4
# This is count 5
# A fruit of type apples
# A fruit of type oranges
# A fruit of type pears
# A fruit of type apricots
# I got 1
# I got 'pennies'
# I got 2
# I got 'dimes'
# I got 3
# I got 'quarters'
# Adding 0 to the list.
# Adding 1 to the list.
# Adding 2 to the list.
# Adding 3 to the list.
# Adding 4 to the list.
# Adding 5 to the list.
# Element was: 0
# Element was: 1
# Element was: 2
# Element was: 3
# Element was: 4
# Element was: 5	


## EX33.PY - While Loops
i = 0	#set i = 0
numbers = [] # create a blank list

print "\n\n\n\n"	#get some space away from the initial prompt
while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)
	
	i = i + 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d " % i


print "\nThe numbers:"

for num in numbers:
	#print "\n"
	print num
	
## EX33X.py - WHILE loop with a function
## Functions area ***
def Funkshun(f, numbers):  #create a function which receives a whole number in variable 'f'
#adding an indent to move the while statement to the function funct
	i = 0	# i needs to be defined within the function
	
	while i < f:
		print "At the top i is %d" % i
		numbers.append(i)
		
		i = i + 1
		print "Numbers now: ", numbers
		print "At the bottom i is %d " % i
		
	return numbers

## Begin program
print "\n\n\n\n"	#get some space away from the initial prompt

# set variables, and lists
numbers = [] # create a blank list

f = raw_input ("What whole number to loop to? ") 
f = float(f)

Funkshun(f, numbers)

print "\nThe numbers:"

for num in numbers:
	#print "\n"
	print num
	
##	33x3.py - move the while loop into a function and change the amount 
## it increments.

## Functions area ***
def Funkshun(f, g, numbers):  #create a function which receives a whole number in variable 'f'
#adding an indent to move the while statement to the function funct
	i = 0	# i needs to be defined within the function
	
	while i < f:
		print "At the top i is %d" % i
		numbers.append(i)
		
		i = i + g  # add the new variable - g - the increment change to variable i.
		
		print "Numbers now: ", numbers
		print "At the bottom i is %d " % i
		
	return numbers

## Begin program
print "\n\n\n\n"	#get some space away from the initial prompt

# set variables, and lists
numbers = [] # create a blank list

f = raw_input ("What whole number to loop to? ") 
g = raw_input ("How much do you want to increment by? ")
f = float(f)
g = float(g)

Funkshun(f, g, numbers)

print "\nThe numbers:"

for num in numbers:
	#print "\n"
	print num

### ex35x5.py 	
##  *** Rewrite the while loop for a f-loop and use the range() instead - see ex32.py
def Funkshun(f, g, numbers):  #create a function which receives a whole number in variable 'f'
#adding an indent to move the while statement to the function funct
	i = 0	# i needs to be defined within the function
	
	for i in range (1,f):  #using the range function forces i to increment in steps of 1
	#for i <= f:  # does not execute, gives invalid syntax errors.  Looks like this is a reason why you use the while loop
		print "At the top i is %d" % i
		numbers.append(i)
		
		i = i + g
		print "Numbers now: ", numbers
		print "At the bottom i is %d " % i
	
	# while i < f:
		# print "At the top i is %d" % i
		# numbers.append(i)
		
		# i = i + g
		# print "Numbers now: ", numbers
		# print "At the bottom i is %d " % i
		
	# return numbers

## Begin program
print "\n\n\n\n"	#get some space away from the initial prompt

# set variables, and lists
numbers = [] # create a blank list

f = raw_input ("What whole number to loop to? ") 
g = raw_input ("How much do you want to increment by? ")
f = int(f)
g = int(g)

Funkshun(f, g, numbers)

print "\nThe numbers:"

for num in numbers:
	#print "\n"
	print num	

##########EX35.PY - the game
from sys import exit

def gold_room():
	print "This room is full of gold.  How much do you take?"
	
	next = raw_input(">")
	if "0" in next or "1" in next:
		how_much = int(next)
	else:
		dead("man, learn to type a number.")
	
	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		dead("You greedy bastard!")
		

def bear_room():
	print "There is a bear here."
	print "The bear hasa a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	print "\n\uPossible Responses:"
	print "take honey"
	print "taunt bear"
	bear_moved = False
	
	while True:
		next = raw_input("> ")
		
		if next == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif next == "taunt bear" and not bear_moved:
			print "The bear has moved from the door.  You can go through it now."
			bear_moved = True
		elif next == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif next == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means."


def cthulu_room():
	print "Hear you see the great evil Cthulu"
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"
	
	next = raw_input("> ")
	
	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well that was tasty!")
	else:
		chtulu_room()

		
def dead(why):
	print why, "Good Job!"
	exit(0)

def start():
	print "You are in a dark room."
	print "There is a door to your right and left"
	print "Which one do you take?"
	
	next = raw_input("> ")
	
	if next == "left":
		bear_room()
	elif next == "right":
		chtulu_room()
	else:
		dead("you stumble around the room until you starve.")

start()


############### ex38.py 
### pop(ping) and appending lists.  slicing lists.

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "\n\nprint ten_things: \n", ten_things
print "\n"
print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ')
print "\nprint stuff:", stuff
print "\n"
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
print "\nprint more_stuff:", more_stuff
print "\n"
while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There's %d items now." % len(stuff)
	print "Here is stuff now: ", stuff
	print "\n"
	
print "There we go, here is stuff: ", stuff

print "Let's do some things with stuff.\n"

print "This is position 1: ", stuff[1]
print "\n"
print "This is position -1: ", stuff[-1] #whoa!  fancy
print "\n"
print stuff.pop()
print "\n"
print ' '.join(stuff) 	#what?  cool!
print "here is stuff now: ", stuff
print "\n"
print '#'.join(stuff[3:5]) 	#super stellar

# print ten_things:
# Apples Oranges Crows Telephone Light Sugar

# Wait there's not 10 things in that list, let's fix that.
# print stuff: ['Apples', 'Oranges', 'Crows', 'Telephone', 'Light', 'Sugar']
# print more_stuff: ['Day', 'Night', 'Song', 'Frisbee', 'Corn', 'Banana', 'Girl', 'Boy']

# Adding:  Boy
# There's 7 items now.
# Here is stuff now:  ['Apples', 'Oranges', 'Crows', 'Telephone', 'Light', 'Sugar', 'Boy']

# Adding:  Girl
# There's 8 items now.
# Here is stuff now:  ['Apples', 'Oranges', 'Crows', 'Telephone', 'Light', 'Sugar', 'Boy', 'Girl']

# Adding:  Banana
# There's 9 items now.
# Here is stuff now:  ['Apples', 'Oranges', 'Crows', 'Telephone', 'Light', 'Sugar', 'Boy', 'Girl', 'Banana']

# Adding:  Corn
# There's 10 items now.
# Here is stuff now:  ['Apples', 'Oranges', 'Crows', 'Telephone', 'Light', 'Sugar', 'Boy', 'Girl', 'Banana', 'Corn']

# There we go, here is stuff:  ['Apples', 'Oranges', 'Crows', 'Telephone', 'Light', 'Sugar', 'Boy', 'Girl', 'Banana', 'Cor
# n']
# Let's do some things with stuff.

# This is position 1:  Oranges
# This is position -1:  Corn
# Corn
# Apples Oranges Crows Telephone Light Sugar Boy Girl Banana
# here is stuff now:  ['Apples', 'Oranges', 'Crows', 'Telephone', 'Light', 'Sugar', 'Boy', 'Girl', 'Banana']
# Telephone#Light
#############################
	
	
	











