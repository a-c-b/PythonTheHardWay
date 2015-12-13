formatter = "%r %r %r %r"
## when 'formatter' above only has 3 %r 
## error:
 # File "ex8.py", line 3, in <module>
    # print formatter % (1,2,3,4)
# TypeError: not all arguments converted during string formatting
# when %r changed to %d then error b/c string, not decimal expected


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

# 1 2 3 4
# 'one' 'two' 'three' 'four'
# True False False True
# '%r %r %r %r' '%r %r %r %r' '%r %r %r %r' '%r %r %r %r'
# 'I had this thing.' 'That you could type up right.' "But it didn't sing." 'So I said goodnight.'
