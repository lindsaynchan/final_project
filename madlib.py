#create stories with blank spaces, place in a dictionary
#welcome user
#display menu, fill in pre-written story and exit
#if select pre-written story, list out options
#ask the user to select a story
#depending on the story, it will ask user for the first blank
#then the next blank, the next, etc. until there's no more blanks
#print out the story with the blanks filled in
#ask if the user would like to play again or exit, return first menu

#loop that asks for user input, store it, and then continue to loop until there are no more blanks
#if blank is noun, ask for noun (make it a conditional)
#once no more blanks, print story

#API dictionary, add if everything working
#case sensitive
#check for empty strings
#make sure output looks good 

from madlib_stories import *
#dictionary containing different stories

blank_spaces = []
#list containing all the types of the blank spaces in the story
user_input = []
#list containing all the user input for each blank

def menu():
	#print menu choices and asking for menu selection
	print "0 - Main Menu"
	print "1 - Pick a Madlib"
	print "2 - Exit"
	menu_choice = raw_input("Please select an option: ")
	return menu_choice

def story_choice():
	#printing story choices, asking for choice, running 3 functions in function
	print "0 - The _____ who lived"
	print "1 - The _____ on fire"
	print "2 - _____ post"
	print "3 - The _____ house"
	print "4 - _____ Demented"
	print "5 - The _____ minister"
	print "6 - The _____ ascending"

	story_title = raw_input("Please select a Madlib: ")
	story_title = story_title.lower()
	chosen_story = stories_dictionary[story_title]
	type_blank_space(chosen_story)
	user_answers()
	replacement(chosen_story)

def type_blank_space(story):
	#obtaining blank space types
	for word in story.split():
		if "<" in word:
			# word = word[1:-1] 
			word = word.replace("<","")
			word = word.replace(">","")
			word = word.replace(".","")
			word = word.replace(",","")
			word = word.replace(";","")
			word = word.replace("'","")
			blank_spaces.append(word)

def user_answers():
	#takes in user input for each blank space
	for i in blank_spaces:
		fill_in_the_blank = raw_input("Please enter a/an %s " % (i))
		user_input.append(fill_in_the_blank)

def replacement(story):
	#replaces blank spaces with the appropriate user input
	user_picked_story = story
	index = 0
	for word in user_picked_story.split():
		if "<" in word:
			replacement = user_input[index]
			if "." in word:
				user_picked_story = user_picked_story.replace(word,replacement+".")
				index += 1
			elif "," in word:
				user_picked_story = user_picked_story.replace(word,replacement+",")
				index += 1
			elif "'s" in word:
				user_picked_story = user_picked_story.replace(word,replacement+"'s")
				index += 1
			elif ";" in word:
				user_picked_story = user_picked_story.replace(word,replacement+";")
				index += 1
			elif "'" in word:
				user_picked_story = user_picked_story.replace(word,"'"+replacement+"'")
				index += 1
			else:
				user_picked_story = user_picked_story.replace(word,replacement)
				index += 1
	print user_picked_story

def main():
	print "Welcome to Madlibs! Let's get started."
	choice = menu()
		
	while True:
		if choice == "0":
			choice = menu()
		elif choice == "1":
			story_choice()
			blank_spaces[:] = []
			user_input[:] = []
			choice = menu()
		elif choice == "2":
			break
		else:
			print "That is not an option."
			choice = menu()

if __name__ == '__main__':
	main()			





















