x = "There are %d types of people." % 10 # %d looks to reference the decimal number 10 after the % sign
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