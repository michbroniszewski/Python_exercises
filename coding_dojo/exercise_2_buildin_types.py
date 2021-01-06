# 1) Write a program diplaying sorted list of words
#    stored in file "three_rings.txt".
#
# - words have no comas nor dots
# - same case (either uppercase or lowercase)
# - unique words

with open('three_rings.txt', 'r') as file:
    data = file.read().split()
    words = {word.strip(",.").lower() for word in data}
    print(sorted(words))

# 2) We have a file "people_age.txt" containing lines "name age".
#    Build a dictionary (use names as keys) out of this file and display it.

with open('people_age.txt', 'r') as file:
    data = file.readlines()
    temp = [tuple(elem.strip('\n').split()) for elem in data]
    dictionary = {element[0]: element[1] for element in temp}
    print(dictionary)


# OPTIONAL
# 3) We have a following list
#    ['v','x','a','m','c','n','t','o','a','r','r','n','y','y','y','r','e','b']
#    Convert it to string "banana" but not via concatenating single letters.

letters = ['v','x','a','m','c','n','t','o','a','r','r','n','y','y','y','r','e','b']
banana_letters = [letter for letter in letters if letter in 'banana']
print(banana_letters[::-1])