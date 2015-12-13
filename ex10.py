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

# while True:
	# for i in [ "/", "-", "|", "\\", "|"]:
		# print "%s\r" % i,