#using "for" loop

result1 = []
for i in range(1,11):
    result1.append(i**2)

#using map
result2 = list(map(lambda x: x**2, range(1, 11)))


#using list comprehension
result3 = [i**2 for i in range(1, 11)]

print(result1)
print(result2)
print(result3)