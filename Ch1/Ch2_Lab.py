#%% [markdown]
## Chapter 2 Lab: Introduction to R (now in Python!)
### Basic Commands
x = [1, 3, 2, 5]
print(x)
y = [1, 4, 3]
print(y)

#%% [markdown]
#### Get the length of a variable
print(len(x))
print(len(y))

#%% [markdown]
#### Element-wise addition of two lists
##### Pure Python
# Use [map](https://docs.python.org/2/library/functions.html#map) with [operator.add](https://docs.python.org/2/library/operator.html#operator.add) ([source](https://stackoverflow.com/a/18713494/4173146)):
from operator import add
x = [1, 6, 2]
print(list(map(add, x, y)))

#%% [markdown]
# or [zip](https://docs.python.org/2/library/functions.html#zip) with a list comprehension:
print([sum(i) for i in zip(x, y)])

#%% [markdown]
##### Using NumPy (will be faster than pure Python) ([source](https://stackoverflow.com/a/18713494/4173146)):
import numpy as np
x2 = np.array([1, 6, 2])
y2 = np.array([1, 4, 3])
print(x2 + y2)