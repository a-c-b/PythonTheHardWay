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