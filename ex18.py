# this one is like your scripts with argv
def print_two(*args): 
    #test line
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
## indentation errors

    #the star args *args operates like the argv parameter but for functions.  It must be between the parens
    #all function lines have to end with the colon
    #all lines indented 4 spaces will become attached to the function
    
    #In Notepad under the EDIT / Blank Operations - you will find a convert tab to space
    


# PS C:\Users\Andrea\mystuff> python ex18.py
# arg1: 'Zed', arg2: 'Shaw'
# arg1: 'Zed', arg2: 'Shaw'
# arg1: 'First!'
# I got nothin'.
