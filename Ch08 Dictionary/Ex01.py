# Write a program that reads the words in words.txt and stores them as keys in a
# dictionary. It does not matter what the values are. Then you can use the in
# operator as a fast way to check whether a string is in the dictionary.


def create_word_dictionary(filename):
    word_dict = {}
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()  # Split the line into individual words
            for word in words:
                word = word.strip()  # Remove leading/trailing whitespace
                word_dict[word] = None  # Store the word as a key with a None value

    return word_dict

# Example usage:
filename = '../code3/words.txt'
word_dictionary = create_word_dictionary(filename)
# print(word_dictionary)

# Check if a word is in the dictionary:
search_word = 'programming'
if search_word in word_dictionary:
    print(f"'{search_word}' is in the dictionary.")
else:
    print(f"'{search_word}' is not in the dictionary.")

