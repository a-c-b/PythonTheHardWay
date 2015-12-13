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