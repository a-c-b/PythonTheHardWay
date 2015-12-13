## Functions area *** Rewrite the while loop for a f-loop and use the range() instead - see ex32.py
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