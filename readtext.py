print "Type the filename again:"
file_again = raw_input("> ")## prompt awaiting user input
#load the new data into variable txt_again
txt_again = open (file_again)
#print the data from text_again with the .read extension
print txt_again.read()

