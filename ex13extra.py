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


