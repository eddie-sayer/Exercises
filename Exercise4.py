import numpy as np

r = np.random.randint(1,9,20)
r_array = np.array(r)
print(r_array)
idx = r_array<5
print(idx)
#the result is an array of True/False strings, where True is in 
#place of the elements that are less than 5, and False otherwise.

r_array[idx] = 0
print(r_array)
#this has converted every element that is less than 5 to a 0.