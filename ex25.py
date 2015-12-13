def break_words(stuff):
	""" This function will break up words for us."""
	words = stuff.split(' ')
	return words

def sort_words(words):
	"""Sorts the words."""
	return sorted(words)

def print_first_word(words):
	"""Prints the first word after popping it off."""
	word = words.pop(0)
	print word

def print_last_word(words):
	"""Prints the last word after popping it off,"""
	word = words.pop(-1)
	print word

def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words"""
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)

# PS C:\Users\Andrea\mystuff> python
# Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import ex25
# >>> ex25.print_first_word(words)
# Traceback (most recent call last):
  # File "<stdin>", line 1, in <module>
# NameError: name 'words' is not defined
# >>> sentence = "All good things come to those who wait."
# >>> words = ex25.break_words(sentence)
# >>> words
# ['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
# >>> ex25.print_first_word(words)
# All
# >>> ex25.print_last_word(words)
# wait.
# >>> sorted_words=ex25.sort_words(words)
# >>> ex25.print_last_word(sorted_words)
# who
# >>> sorted_words = ex25.sort_sentence(sentence)
# >>> sorted_words
# ['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
# >>> ex25.print_first_and_last(sentence)
# Traceback (most recent call last):
  # File "<stdin>", line 1, in <module>
# AttributeError: 'module' object has no attribute 'print_first_and_last'
# >>> import print_first_and_last
# Traceback (most recent call last):
  # File "<stdin>", line 1, in <module>
# ImportError: No module named print_first_and_last
# >>> ex25.print_first_word(words)
# good
# >>> ex25.print_last_word(words)
# who
# >>> words
# ['things', 'come', 'to', 'those']
# >>> sentence
# 'All good things come to those who wait.'
# >>> ex25.print_first_and_last_sorted(sentence)
# All
# who
# >>> sentence
# 'All good things come to those who wait.'
# >>> ex25.print_first_and_last(sentence)
# Traceback (most recent call last):
  # File "<stdin>", line 1, in <module>
# AttributeError: 'module' object has no attribute 'print_first_and_last'
# >>> ex25.print_first_and_last(sentence)
# Traceback (most recent call last):
  # File "<stdin>", line 1, in <module>
# AttributeError: 'module' object has no attribute 'print_first_and_last'
# >>> help(print_first_and_last)
# Traceback (most recent call last):
  # File "<stdin>", line 1, in <module>
# NameError: name 'print_first_and_last' is not defined
# >>> help(print_first_and_last_sorted)
# Traceback (most recent call last):
  # File "<stdin>", line 1, in <module>
# NameError: name 'print_first_and_last_sorted' is not defined
# >>> ex25.print_first_and_last_(sentence)
# All
# wait.