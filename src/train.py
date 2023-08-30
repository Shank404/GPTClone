# Read training data
from SimpleTokenizer import SimpleTokenizer


with open("./data/input.txt", "r", encoding="utf-8") as textIOWrapper:
    text = textIOWrapper.read()

# Print length of training data
# print("Length of training data: ", len(text))

# Print first 1000 characters of training data
# print(text[:1000])

# Get a set of all unique characters in the training data
training_set = set(text)

# Get a list of all the data in the training set
training_list = list(training_set)

# Sort the list of training data
training_list.sort()

# Print the length of the training list
# print("Number of unique characters in the training data: ", len(training_list))

# Print all the unique characters in the training list
# print("Characters: ", training_list)

# Create a dictionary mapping from characters to integers
characterMapping = dict((character, integer)
                        for integer, character in enumerate(training_list))
# print("Character to integer:", characterMapping)

# Create a dictionary mapping from integers to characters
integerMapping = dict((integer, character)
                      for integer, character in enumerate(training_list))
# print("Integers to characters:", integerToCharacters)

# Initialize tokenizer
simpleTokenizer = SimpleTokenizer()

# Print encoded example string
# encoded_example = simpleTokenizer.encode(characterMapping, "hii meine kerle")
# print(encoded_example)

# Print decoded example string
# decoded_example = simpleTokenizer.decode(integerMapping, encoded_example)
# print(decoded_example)
