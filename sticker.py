# importing Numpy for Calculations
import numpy as np
from money import Money
# Sticker Costs
cost = Money(amount='2.00', currency='USD')
freshbook = list("facebook")
good_word = True
facebook = list("facebook")
userInput = raw_input("Please enter word to see how many stickers you will need: ")
# Counter for Stickers
counter = 1


def printinfo( word ):
   	# Takes a word makes sure its a string 
   	# turns it to lower case
   	lword = str(word).lower()
   	# print "Word: ", lword
   	# Turns Word to Array of single characters
   	warray = list(lword)
   	# print(warray)
   	# For Loop for each Character in String
   	for x in xrange(0,len(warray)):
   		if warray[x] in freshbook:
			letter = warray[x]
			# print(letter)
			if letter in facebook:
				facebook.remove(letter);
				# print(facebook)
			# If not in current facebook letters
			else:
				global counter
				counter += 1
				for x in xrange(0,len(freshbook)): 
					facebook.append(freshbook[x])
				# print(facebook)
		else:
			global good_word
			good_word = False;
			print("Sorry Word Must Contain F, A, C, E, B, O, O, K try again.")
			return
printinfo(userInput);

if good_word == True:
	#Print Out
	print("----LETTERS LEFT-----");
	for x in facebook: print x,
	print("");
	print("----STICKER COUNT----");
	print(counter);
	print("----COSTS OF STICKERS----");
	total = counter * cost
	print(total);
