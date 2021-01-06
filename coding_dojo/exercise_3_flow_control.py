# 1) Take all the words from file "three_rings.txt" and print them
#    in 20-character right-justified column.

with open('three_rings.txt', 'r') as three_rings:
    for word in three_rings.read().split():
        print(word.rjust(20))

# 2) Take file "three_rings.txt" and build file "three_wings.txt".
#    (by exchanging any Ring into Wing).

with open('three_rings.txt', 'r') as three_rings:
    with open('three_wings.txt', 'w') as three_wings:
        for line in three_rings:
            for word in line.split():
                if word == "Ring" and not word == "Rings":
                    word = "Wing"
                three_wings.write(word + " ")
            three_wings.write("\n")
        # three_wings.write(''.join(data))


# 4) Write program that displays number of bits set in itself
#    (means: calculating number of bits '1' in binary representation of that program)
#    and displaying its binary representation.


# OPTIONAL:
# 3) Calculate surface area of Sierpinski carpet
#    (http://en.wikipedia.org/wiki/Sierpinski_carpet)
#    which has edge size=27 and iterations number iter=3.