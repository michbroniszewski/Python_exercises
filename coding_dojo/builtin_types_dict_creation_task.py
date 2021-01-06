keys = 'abcdefg'
values = [1, 2, 3, 4, 5, 6, 7]

new_dict = {keys[i]: values[i] for i in range(len(keys))}
dict_2 = {element: values[i] for i, element in enumerate(keys)}
print(new_dict)
print(dict_2)