from sys import argv

source, filename = argv 

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

