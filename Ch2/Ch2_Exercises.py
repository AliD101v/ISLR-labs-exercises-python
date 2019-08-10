#%% [markdown]
## Chapter 2 Exercises: Applied
### Q8
#### Part (a)
import pandas as pd
# Edit the path on your platform to correctly point to the file
df = pd.read_csv('Datasets\College.csv')

#%% [markdown]
#### Part (b)
df.head()
#%%
df.rename(columns={df.columns.values[0]: 'Name'}, inplace=True)

#%% [markdown]
#### Part (c)
#%%
# i.
df.describe()
#%%
# ii.
from pandas.plotting import scatter_matrix
import numpy as np
# scatter_matrix(df[df.columns[0:9]], diagonal='kde')
#%%
# iii.
df_cat = df.pivot(values='Outstate', columns='Private')
df_cat.plot.box()
#%%
# iv.
df['Elite'] = np.where(df['Top10perc'] > 50, 'Yes', 'No')
print('The number of elite universities: ' + str(df['Elite'].value_counts()['Yes']))
df_cat = df.pivot(values='Outstate', columns='Elite')
df_cat.plot.box()
#%%
# v.
df.hist(column=['Room.Board', 'Books', 'Personal', 'Expend'], bins=25, figsize=(6, 4))

#%% [markdown]
### Q9
from IPython.core.display import display
df = pd.read_csv('Datasets\Auto.csv')
#%% [markdown]
#### Part (a)
df_predictors = df.dtypes
df_predictors = pd.DataFrame(list(df))
df_predictors.rename(columns={df_predictors.columns.values[0]: 'Predictor Name'}, inplace=True)
df_predictors['dtypes'] = df.dtypes.tolist()
df_predictors['Quantitative or Qualitative'] = np.where(df_predictors['dtypes'] == np.dtype('object'), 'Qualitative', 'Quantitative')
display(df_predictors.iloc[:,[0,2]])