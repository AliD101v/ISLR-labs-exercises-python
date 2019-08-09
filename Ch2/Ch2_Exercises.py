#%% [markdown]
## Chapter 2 Exercises: Applied
### Q8
#### Part (a)
import pandas as pd
# Edit the path on your platform to correctly point to the file
df = pd.read_csv('Datasets\College.csv')

#### Part (b)
df.head()
df.rename(columns={df.columns.values[0]: 'Name'}, inplace=True)