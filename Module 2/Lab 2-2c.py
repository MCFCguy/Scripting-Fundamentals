# Prompt user for input and store the result
sentence = input("Sentence: ")

# Prompt user for input and store the result
substring = input("Word to look for in sentence: ")

# Format the inputs
formatted_sentence = sentence.strip().lower()
formatted_substring = substring.strip().lower()

# Count the instances of the substring present in the sentence
substring_count = formatted_sentence.count(formatted_substring)

# Print the result
print(f"There are {substring_count} occurrences of '{substring}' in the sentence")
