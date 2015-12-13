#Create a list
elements = []

#append empty lists in first two indexes.
elements.append([])	#Index 0
print elements

elements.append([])	#Index 1
print elements

#Add elements to empty lists.
elements[0].append(1)
print elements

elements[0].append(2)
print elements

elements[1].append(3)
print elements
elements[1].append(4)
print elements

#Display top-left element.
print(elements[0][0])

# [[]]
# [[], []]
# [[1], []]
# [[1, 2], []]
# [[1, 2], [3]]
# [[1, 2], [3, 4]]




#loop over rows.
# for row in elements:
	#loop over columns.
	# for column in row:
		# print (column, end = "")
	# print(end="\n")
	
	
