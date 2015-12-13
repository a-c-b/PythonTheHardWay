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

def secret_formula(start_point):
	jelly_beans = start_point * 500
	jars = jelly_beans / 1000
	crates = jars / 1000
	return jelly_beans, jars, crates
	
start_point = 10000
jelly_beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d beans" % start_point
print "We'd have %d beans, %d jars, and %d crates.\n" % (jelly_beans, jars, crates)

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