#%% [markdown]
## Chapter 2 Exercises: Applied
#%%
# imports
import pandas as pd
from pandas.plotting import scatter_matrix
import numpy as np
from IPython.core.display import display
import plotly.graph_objects as go

#%% [markdown]
### Q8
#### Part (a)
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
scatter_matrix(df[df.columns[0:9]], diagonal='kde')
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
# vi.
# 
# We will create a matrix of correlation coeeficients for every pair of variables.
# 
# First, filter out the qualitative variables.
quant_var_names = pd.DataFrame(list(df))
quant_var_names.rename(columns={quant_var_names.columns.values[0]: 'Variable Name'}, inplace=True)
quant_var_names['dtypes'] = df.dtypes.tolist()
quant_var_names = quant_var_names[quant_var_names['dtypes'] != np.dtype('object')].iloc[:,0]
#%% [markdown]
# Then, create the correlation matrix.
col_count = quant_var_names.shape[0]
cor_mat = np.zeros((col_count, col_count))
for i in range(col_count):
    for j in range(col_count):
        temp_mat = np.corrcoef(df[quant_var_names.iloc[i]], df[quant_var_names.iloc[j]])
        cor_mat[i,j] = temp_mat[0, 1]
df_cor_mat = pd.DataFrame(cor_mat, index=quant_var_names, columns=quant_var_names)
display(df_cor_mat)
#%% [markdown]
# Now, let's only display the interesting variable pairs, i.e. variable pairs that are highly linearly (un)correlated. That means we will filter the pairs whose absolute correlation is above a certain threshold: |correl(x,y)| >= theta. We will use 0.8 as the threshold value.
# 
# First, create a list of linearly (un)correlated variables as [x, y, correlation] per each row
theta = 0.2
correlated_vars = []
for i in range(col_count):
    for j in range(i+1, col_count):
        if np.abs(df_cor_mat.iloc[i,j]) >= 0.8:
                correlated_vars.append([quant_var_names.iloc[i], quant_var_names.iloc[j], df_cor_mat.iloc[i,j]])
#%% [markdown]
# Then, group by the first (x) variable.
df_correlated_vars = pd.DataFrame(correlated_vars, columns=['x', 'y', 'Correlation Coefficient'])
grouped_correlated_vars = df_correlated_vars.groupby('x')
#%% [markdown]
# ...and display the groups.
for key, item in grouped_correlated_vars:
        display(key)
        display(grouped_correlated_vars.get_group(key))
#%% [markdown]
# Next, let's list the most linearly correlated variables in each group, along with their correlation coefficients
max_grouped_correlated_vars = grouped_correlated_vars.max()
display(max_grouped_correlated_vars)
#%% [markdown]
# Lastly, let's visualize the max pairs from the previous step.
# 
# For each row in the maximum correlations dataframe, i.e. for each pair of variables (x, y), create the scatter plot.
# reset the index, and add the x column to the dataframe
max_grouped_correlated_vars.reset_index(inplace=True)
for i in range(max_grouped_correlated_vars.shape[0]):
        fig = go.Figure(data=go.Scatter(x=df[max_grouped_correlated_vars.iloc[i, 0]], y=df[max_grouped_correlated_vars.iloc[i, 1]], mode='markers', text=df['Name']))
        fig.update_layout(xaxis=go.layout.XAxis(title=go.layout.xaxis.Title(text=max_grouped_correlated_vars.iloc[i, 0])), yaxis=go.layout.YAxis(title=go.layout.yaxis.Title(text=max_grouped_correlated_vars.iloc[i, 1])))
        fig.show()
##################################################################
#%% [markdown]
### Q9
df = pd.read_csv('Datasets\Auto.csv')
#%% [markdown]
#### Part (a)
df_predictors = pd.DataFrame(list(df))
df_predictors.rename(columns={df_predictors.columns.values[0]: 'Predictor Name'}, inplace=True)
df_predictors['dtypes'] = df.dtypes.tolist()
df_predictors['Quantitative or Qualitative'] = np.where(df_predictors['dtypes'] == np.dtype('object'), 'Qualitative', 'Quantitative')
display(df_predictors.iloc[:,[0,2]])

#%% [markdown]
#### Part (b)
df.describe()

#%%
