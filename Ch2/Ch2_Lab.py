#%% [markdown]
## Chapter 2 Lab: Introduction to R (now in Python!)
# Please note that, the purpose of this file is *not* to demonstrate Python's basic functionalities (there are much more comprehensive guides, [like this](https://learnxinyminutes.com/docs/python3/)) but to mirror ISLR's lab in R as much as possible.
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

#%% [markdown]
#### List all the variables
def printvars():
   tmp = globals().copy()
   [print(k,'  :  ',v,' type:' , type(v)) for k,v in tmp.items() if not k.startswith('_') and k!='tmp' and k!='In' and k!='Out' and not hasattr(v, '__call__')]
printvars()

#%% [markdown]
#### Clear a variable's content
x = None
print(x)
#%% [markdown]
#### Delete a variable (its reference)
del y
print(y)
#%% [markdown]
#### Delete all varialbes ([source](https://stackoverflow.com/a/53415612/4173146))
for name in dir():
    if not name.startswith('_'):
        del globals()[name]

for name in dir():
    if not name.startswith('_'):
        del locals()[name]
print(x2)
print(y2)
#%% [markdown]
# or simply restart the interpreter.

#%% [markdown]
#### Declare matrices ([source](https://stackoverflow.com/questions/6667201/how-to-define-a-two-dimensional-array-in-python))
##### Pure Python
rowCount = 4
colCount = 3
mat = [[0 for x in range(colCount)] for x in range(rowCount)]
print(mat)
#%% [markdown]
# or a shorter version:
mat = [[0] * colCount for i in range(rowCount)]
print(mat)

#%% [markdown]
# However, it is best to use numpy arrays to represent matrices.
import numpy
mat = numpy.zeros((rowCount, colCount))
print(mat)

#%% [markdown]
#### The sqaure root of each element of a vector or matrix (numpy array)
import numpy as np
mat = [[16] * colCount for i in range(rowCount)]
mat = np.asarray(mat)
print(np.sqrt(mat))

#%% [markdown]
#### Generate a vector of random normal variables
# Dimensions are provided as arguements to the numpy function. 
# 
# For random samples from a Normal distribution with mean *mu* and standard deviation *sigma*, use:
# `sigma * np.random.randn(...) + mu` according to the [documentation](https://docs.scipy.org/doc/numpy-1.16.0/reference/generated/numpy.random.randn.html#numpy.random.randn)
import numpy as np
x = np.random.randn(50)
y = x + ( 0.1 * np.random.randn(50) + 50 )
#%% [markdown]
# To compute the [Pearson correlation coefficient](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient), or simply correlation, between the two vectors:
print(np.corrcoef(x, y))

#%% [markdown]
# To set the seed for random number generation, in Python:
import random
random.seed(0)
#%% [markdown]
# Or in numpy:
np.random.seed(0)
x = np.random.randn(50)
y = x + ( 0.1 * np.random.randn(50) + 50 )

#%% [markdown]
#### To compute the mean, variance, and standard deviation of a vector of numbers:
print(np.mean(x))
print(np.var(x))
print(np.std(x))
print(np.mean(y))
print(np.var(y))
print(np.std(y))

#%% [markdown]
### Graphics
#### Using matplotlib
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(0)
x = np.random.randn(100)
y = np.random.randn(100)

fig, ax = plt.subplots()
ax.scatter(x, y)
plt.show()

fig, ax = plt.subplots()
ax.set_xlabel(r'this is the x-axis')
ax.set_ylabel(r'this is the y-axis')
ax.set_title('Plot of X vs Y')
ax.grid(True)
fig.tight_layout()
ax.scatter(x, y)
#%% [markdown]
##### Save the plot to a file
fig.savefig('sample.png')
# remove the whitespace around the image
fig.savefig('sample.pdf', bbox_inches='tight')

#%% [markdown]
#### Using Seaborn
import seaborn as sns
fig, ax = plt.subplots()
ax.set_xlabel(r'this is the x-axis')
ax.set_ylabel(r'this is the y-axis')
ax.set_title('Plot of X vs Y')
ax.grid(True)
fig.tight_layout()
sns.scatterplot(x, y)

#%% [markdown]
#### Using Plotly
import plotly.graph_objects as go
fig = go.Figure(data=go.Scatter(x=x, y=y, mode='markers'))
fig.show()

#%% [markdown]
#### Using Bokeh
from bokeh.plotting import figure as bkfig, show as bkshow
fig = bkfig(title="Plot of X vs Y", tools='pan,wheel_zoom,box_zoom,reset,hover,crosshair', active_inspect='hover')
fig.circle(x=x, y=y)
fig.xaxis.axis_label = 'this is the x-axis'
fig.yaxis.axis_label = 'this is the y-axis'
bkshow(fig)

#%% [markdown]
#### Generating a sequence or range of numbers
# In pure Python, use `range(lower, upper, step)`:
# The following will generate a sequence of integers 1,...,10
x = range(1, 11)
for i in x:
        print(i)
#%% [markdown]
# To use non-decimal steps, or specify the number of elements to return, use the `linspace()` function in NumPy:
x = np.linspace(1, 10, 20)
print(x)
# Note that the PI constant in all of Python's math module, NumPy, and SciPy are the same.
x = np.linspace(-np.pi, np.pi, 50)
print(x)

#%% [markdown]
#### Contour plotting
import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt


x = np.linspace(-np.pi, np.pi, 50)
y = x
X, Y = np.meshgrid(x, y)
# [source](https://stackoverflow.com/a/45496154/4173146)
Z = np.cos(y) / (1 + x[:, None]**2)

fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z)
ax.clabel(CS, inline=1, fontsize=4)

CS = ax.contour(X, Y, Z, 45)
ax.clabel(CS, inline=1, fontsize=4)

Z2 = ( Z - Z.T ) / 2
fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z2, 15)
ax.clabel(CS, inline=1, fontsize=4)

#%% [markdown]
#### Filled contour (heatmap)
# Note: run the previous cell first.
fig, ax = plt.subplots(constrained_layout=True)
ax.contourf(X, Y, Z2, 15, cmap=plt.cm.plasma)
cbar = fig.colorbar(CS)

#%%
