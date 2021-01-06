# def power(x, y):
#     return x**y
#
# print(power(2, 3))


# is_x2 = lambda x: x.endswith(('_X2', '_X2_QT'))
#
# my_strings = ['CLOUD_R4P_X2', 'CLOUD_F_X2_QT', 'CLOUD_F_QT', 'CLOUD_R4P']
# for my_string in my_strings:
#     print(is_x2(my_string))


fruits = ['cherry', 'apple', 'melon', 'grape', 'pomelo', 'strawberry']
countries = ['vietnam', 'poland', 'sweden', 'india', 'canada', 'finland', 'denmark']

#using "for" loop
result = []
for fruit in fruits:
    for country in countries:
        if fruit[0] == country[0]:
            result.append((fruit, country))

print(result)


#using list comprehension
result2 = [(fruit, country) for fruit in fruits for country in countries if fruit[0] == country[0]]

print(result2)

integers = [3, 1, 4, 6, 10]
strings = ['1', '5', '10', '3']

#using "for" loop
for_set_result = dict()
for integer in integers:
    for string in strings:
        if str(integer) == string:
            for_set_result.update({integer: string})


#using dict comprehension
comp_set_result = {integer: string for integer in integers for string in strings if str(integer) == string}

print(for_set_result)
print(comp_set_result)