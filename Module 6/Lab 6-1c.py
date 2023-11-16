def content_combiner(dict1, dict2):
    combined_dictionary = {}
    combined_dictionary.update(dict1)
    combined_dictionary.update(dict2)
    return combined_dictionary

# Test your function using the code below
if __name__ == '__main__':
    print(content_combiner({"gold": "Yellow"}, {"karats": 24}))
