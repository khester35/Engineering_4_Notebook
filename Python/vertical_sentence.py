# User types a sentence and code prints it vertically
# Kaymin Hester

sentence = input("Enter a sentence: ".lower())

for letter in sentence:
	print (letter)

print (" ")

sentence = sentence.split()
for word in sentence:
	print (word)
