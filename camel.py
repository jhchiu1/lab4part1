# Camel case

'''Display program name in a banner'''
msg = 'AWESOME camelCaseGenerator PROGRAM'
stars = '*' * len(msg)
print('\n', stars, '\n', msg, '\n', stars, '\n')



# Create sentence variable asking for user input
sentence = input("Enter a sentence:\n")

# Create newSentence variable as empty
newSentence = ""
pastFirstWord = False

# Use split method to break up the string
for word in sentence.split():
	   if pastFirstWord:
	       newSentence += word.capitalize()
	   else:
	       newSentence += word.lower()
	   pastFirstWord = True

# Print newly converted sentence
print(newSentence)

