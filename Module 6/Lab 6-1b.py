def word_counter(string):
    formatted_string = string.strip()
    character_counter = {}
    for char in string:
        if char not in character_counter.keys():
            if char.isalpha() == True:
                character_counter.update({char:1})
            else:
                continue
        else:
            current_count = character_counter.get(char)
            character_counter.update({char:current_count+1})
    return character_counter

print(word_counter("Mississippi"))
