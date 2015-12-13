from sys import argv

script, user_name = argv
prompt = '>'

print "Hi %s, I'm the % script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer.  Nice.
""" % (likes, lives, computer)

# PS C:\Users\Andrea\mystuff> python ex14.py zed
# Hi zed, I'm the ex14.pycript.
# I'd like to ask you a few questions.
# Do you like me zed?
# >yes
# Where do you live zed?
# >west seattle
# What kind of computer do you have?
# >hp

# Alright, so you said 'yes' about liking me.
# You live in 'west seattle'.  Not sure where that is.
# And you have a 'hp' computer.  Nice.



