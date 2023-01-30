import numpy as np

#Part a

a = np.array([5, 4, 9, 2, 0, 4, 7, 2])

print(a[-1])

#Part b

print(a[1:6])
#this prints all of the elements from position 1 to position 6.
print(a[:-2])
#this prints all of the elements apart from the last two.
print(a[::2])
#this prints every other element, starting from position 0.

#Part c

a[-1] = -9
print(a)

a[0:3] = 1
print(a)
#the first three elements are changed to a 1.