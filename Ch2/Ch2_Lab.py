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
CS = ax.contourf(X, Y, Z2, 15, cmap=plt.cm.plasma)
cbar = fig.colorbar(CS)

#%% [markdown]
#### 3D contour plots
# 3D wireframe plot
from mpl_toolkits.mplot3d import axes3d
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(X, Y, Z2)
plt.show()

#%% [markdown]
# 3D surface (color map)
from matplotlib.ticker import LinearLocator, FormatStrFormatter
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, Z2, cmap=cm.terrain)
fig.colorbar(surf)
plt.show()

#%% [markdown]
# Project filled contour 'profiles' onto the 'walls' of the graph
from matplotlib.ticker import LinearLocator, FormatStrFormatter
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, Z2, cmap=cm.terrain, alpha=0.8)
fig.colorbar(surf)
# Plot projections of the contours for each dimension.  By choosing offsets
# that match the appropriate axes limits, the projected contours will sit on
# the 'walls' of the graph (from the [matplotlib documentation](https://matplotlib.org/3.1.1/gallery/mplot3d/contourf3d_2.html#sphx-glr-gallery-mplot3d-contourf3d-2-py))
cset = ax.contourf(X, Y, Z2, zdir='z', offset=ax.get_zlim()[0], cmap=cm.plasma, alpha=0.8)
# cset = ax.contourf(X, Y, Z2, zdir='x', offset=ax.get_xlim()[0], cmap=cm.plasma, alpha=0.8)
# cset = ax.contourf(X, Y, Z2, zdir='y', offset=ax.get_ylim()[1], cmap=cm.plasma, alpha=0.8)
plt.show()

#%% [markdown]
# Vary the viewing angle
for elev in [20, 70, 40]:
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        surf = ax.plot_surface(X, Y, Z2, cmap=cm.terrain, alpha=0.8)
        fig.colorbar(surf)
        cset = ax.contourf(X, Y, Z2, zdir='z', offset=ax.get_zlim()[0], cmap=cm.plasma, alpha=0.8)
        ax.azim = 30
        ax.elev = elev

        plt.show()

#%% [markdown]
### Indexing Data
import numpy as np
A = np.array(np.arange(1, 17, 1)).reshape(4, 4).T
print(A)
# Python's arrays are zero-indexed
print(A[1, 2])
#%% [markdown]
#### Select multiple rows and columns
print(np.array([A[0,1], A[0,3], A[2,1], A[2,3]]).reshape(2,2))
print(A[:3, 1:4])
print(A[:2, :])
print(A[:, :2])
print(A[0])
#%% [markdown]
#### Keep all rows or columns except those indicated in the index
# To exclude whole rows or columns, use a boolean mask.
mask = np.ones(len(A), dtype=bool)
# Set the excluded indices to False
mask[[0,2]] = False
# Use the boolean/logical mask to index into the array
print(A[mask,...])
#%% [markdown]
# Get the dimensions of the array (matrix)
print(A.shape)

#%% [markdown]
### Loading Data
# We will use pandas to load and read the data
import pandas as pd
# Edit the path on your platform to correctly point to the file
df = pd.read_csv('Datasets\Auto.csv')
df.head()

#%% [markdown]
# Pass `'?'` as a NaN string
df = pd.read_csv('Datasets\Auto.csv', na_values='?')
df.head()
print(df.shape)
print(df.iloc[10:20,:])
# Find and display only rows with NaN's
df1 = df[df.isna().any(axis=1)]
df1.head()
print(df1.shape)

#%% [markdown]
# Drop the NaN values
df = df.dropna()
print(df.shape)

#%% [markdown]
# Get a list of column names in the DataFrame
print(list(df))

#%% [markdown]
### Additional Graphical and Numerical Summaries
# Scatterplots of the quantitative variables
df.plot.scatter(x='cylinders', y='mpg')

#%% [markdown]
# Boxplots, which are more suitable if the variable on the x-axis is categorical.
df_cat = df.pivot(columns='cylinders', values='mpg')
df_cat.plot.box()
df_cat.plot.box(vert=False)

#%% [markdown]
# Plot a histogram
df.hist(column='mpg')
df.hist(column='mpg', bins=15)

#%% [markdown]
# Plot a scatterplot matrix
from pandas.plotting import scatter_matrix
scatter_matrix(df[['mpg', 'displacement', 'horsepower', 'weight', 'acceleration']], diagonal='kde')

#%% [markdown]
# Plot the scatterplot, with custom variable values on mouse hover (using Plotly)
# Marker color and size can also be set to variables.
import plotly.graph_objects as go
fig = go.Figure(data=go.Scatter(x=df['horsepower'], y=df['mpg'], mode='markers', text=df['name']))
fig.update_layout(xaxis=go.layout.XAxis(title=go.layout.xaxis.Title(text='Horsepower')), yaxis=go.layout.YAxis(title=go.layout.yaxis.Title(text='MPG')))
fig.show()

#%% [markdown]
#### Descriptive statistics
# Include all variables
df.describe()

#%% [markdown]
# Include only a subset of variables
df['mpg'].describe()

#%% [markdown]
#### Serialization - save or load the current session
import dill
filename = 'globalsave.pkl'
dill.dump_session(filename)

# and to load the session again:
dill.load_session(filename)