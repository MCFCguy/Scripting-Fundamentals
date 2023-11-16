word = input("Word to convert: ")
count = int(input("How many letters at the end of the word should be converted? "))
word_length = len(word)

first_half = word[0:-count]
second_half = word[-count:word_length]

second_half_caps = second_half.upper()

converted_word = first_half + second_half_caps

print(converted_word)
