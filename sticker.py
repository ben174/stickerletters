# importing Numpy for Calculations on Arrays
import numpy as np
# importing Money for Proper Handinling of Currency
from money import Money
# Sticker Costs
cost = Money(amount='2.00', currency='USD')
# Clean Facebook Input
freshbook = list("facebook")
# Checker for Proper Input
good_word = True
#Facebook Letter Array 
facebook = list("facebook")
#Terminal User Input
userInput = raw_input("Please enter word to see how many stickers you will need: ")
# Counter for Stickers
counter = 1

#Function to Solve Sticker Count
def printinfo( word ):
   	# Takes a word makes sure its a string 
   	# turns it to lower case
   	lword = str(word).lower()
   	#print "Word: ", lword
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
# Use Print Info with User Input			
printinfo(userInput);
# Only show if a Good Word
if good_word == True:
	#Print Out
	print("----LETTERS LEFT-----");
	for x in facebook: print x,
	print("");
	print("----STICKER COUNT----");
	print(counter);
	print("----COSTS OF STICKERS----");
	total = counter * cost
	# Total You Win
	print(total);
