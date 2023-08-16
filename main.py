import string
#Opening File
f = open('TestFile.txt', 'r')

#Reading and printing contents of file
f_content = f.read()

#Finding the amount of words and printing it
f_length = len(f_content.split())
print(f'The file has a total of {f_length} words')

#Finding the average length of a word
f_content_words = f_content.split()
f_character_total = 0
for i in range(f_length):
	f_word_length = len(f_content_words[i])
	f_character_total += f_word_length
f_character_average = f_character_total // f_length
print(f'The average length of a word is {f_character_average} letters')

#Finding how many times a user specified word appears
print("What word do you want to know the accurance of from the file")
user_word = input()
word_found_count = 0
for x in range(f_length):
	if user_word == f_content_words[x]:
		word_found_count += 1
if word_found_count == 1:
	print(f'The word {user_word} appears in the file {word_found_count} time')
else:
	print(f'The word {user_word} appears in the file {word_found_count} times')

#Working out how many words start with each letter of the alphabet
f_content_words_first_letters = []
for word_count in range(f_length):
	f_content_words_first_letters.append(f_content_words[word_count][0])
alphabet = list(string.ascii_lowercase)
count = {}
for alphabet_count_one in range(26):
	count[alphabet_count_one] = 0
for wordcount in range(f_length):
	for alphabet_count_two in range(26):
		if f_content_words_first_letters[wordcount] == alphabet[alphabet_count_two]:
			variablename = alphabet[alphabet_count_two]
			count[alphabet_count_two] += 1
for alphabet_count_three in range(26):
	if count[alphabet_count_three] != 0:
		print(f'The letter {alphabet[alphabet_count_three]} is at the front of {count[alphabet_count_three]} words in the file')