# importing Numpy for Calculations on Arrays
# i would recommend avoiding numpy for a problem as simple as this one.
import numpy as np

# importing Money for Proper Handinling of Currency
# definitely avoid importing libraries that aren't a part of the
# standard library unless completely necessary.
from money import Money

# Sticker Costs
cost = Money(amount='2.00', currency='USD')

# so using the standard libarary, cost would just be
COST = 2

# note use of all-caps for constants - a constant is a fixed value

# Clean Facebook Input
freshbook = list("facebook")
# this is good. using list() on a string is the ideal way to convert
# it to a list of characters


# Checker for Proper Input
good_word = True
# not necessary, and since the original test instructions explicity
# say you can assume that the input is only going to have the letters
# f,a,c,e,b,o,o,k this would actually be considered a bad thing to
# check for. simplicity is better and you want to do the minimal
# work to get the job done. I know it seems counterintuitive, but
# trust me on that. if a interview problem says "you can expect", it
# means "you _should_ expect". But it never hurts to say 'in the
# real world i would put error checking here if i didn't know exactly
# who was calling the function. especially if it's user input from
# a web form or something'

#Facebook Letter Array
facebook = list("facebook")


#Terminal User Input
userInput = raw_input("Please enter word to see how many stickers you will need: ")

# the instructions just say to 'create a function that'.. so
# an interactive terminal program isn't exactly what they asked
# for. it's probably fine though and this is just a bit nit
# picky

# Counter for Stickers
counter = 1
# global variables are generally regarded as bad.
# what if i wanted  to use this function multiple times in
# this file? keep your variables inside your function

#Function to Solve Sticker Count
# this function name doesn't tell me much, maybe
# calculate_sticker_cost ?
def printinfo( word ):
   	# Takes a word makes sure its a string
   	# turns it to lower case
   	lword = str(word).lower()
    # this is good, the instructions didn't say the
    # cause would be all lower, i probably would have
    # missed that check.
    # but if you're not going to use the orignal word
    # just reassign to the original word variable:
    # word = word.lower()

    # remove unnecessary comments
   	#print "Word: ", lword

   	# Turns Word to Array of single characters
    # not necessary - you can just loop through the word
   	warray = list(lword)

   	# print(warray)

   	# For Loop for each Character in String
    # could just be:
    # for letter in lword:
   	for x in xrange(0,len(warray)):
        # this check would be unecessary as stated above
   		if warray[x] in freshbook:
            # this would be unnecessary if looping as stated above
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
