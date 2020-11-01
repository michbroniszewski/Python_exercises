import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.scatter(input_values, squares, s=100)

plt.title("Kwadraty liczb", fontsize=24)
plt.xlabel("Wartość", fontsize=14)
plt.ylabel("Kwadraty wartości", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)
plt.show()
