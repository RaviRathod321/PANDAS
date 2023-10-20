import pandas as pd
import numpy as np

# We create a Pandas Series that stores a grocery list of just fruits
# fruits = pd.Series(data = [10, 6, 3,], index = ['apples', 'oranges', 'bananas'])

# We display the fruits Pandas Series

fruits = pd.Series([10, 6, 5], ['Apple', 'oranges', 'banana'])
# print('Original grocery list of fruits:\n ', fruits)
print(fruits)

# print('fruits + 2:\n', fruits + 2) # We add 2 to each item in fruits
w = fruits + 2
print(w)

# print('fruits - 2:\n', fruits - 2) # We subtract 2 to each item in fruits
w1 = fruits - 2
print(w1)

# print('fruits * 2:\n', fruits * 2) # We multiply each item in fruits by 2
w2 = fruits * 2
print((w2))

# print('fruits / 2:\n', fruits / 2) # We divide each item in fruits by 2
w3 = fruits / 2
print(w3)

# We are using a numpy library and Adding the sqrt to a variable.
w4 = np.sqrt(fruits)
print(w4)

# exponential using Numpy
w5 = np.exp(fruits)
print(w5)

# Power of 2
w6 = np.power(fruits, 2)
print(w6)


print(fruits)

# Adding the value 2 to banana
w7 = fruits['banana'] + 2
print(w7)

# Subtracting using the ilocation
w8 = fruits.iloc[0]-2
print(w8)

# Multiplying the values by 2
w9 = fruits[['Apple', 'oranges']] * 2
print(w9)

# Division by 2
w10 = fruits.loc[['Apple', 'oranges']] / 2
print(w10)

print()

groceries = pd.Series(data =[30, 6, 'yes', 'no'], index=['eggs', 'apples','milk', 'bread'])
print(groceries)

w11 = groceries * 2
print(w11)