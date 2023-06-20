import pandas as pd
import random
lst = ['robot'] * 5
lst += ['human'] * 5
lst += ['cat'] * 5
lst += ['dog'] * 5
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
print(data)

for col in set(data['whoAmI'].to_list()):
  data.loc[data['whoAmI'] == col, col] = 1
  data.loc[data['whoAmI'] != col, col] = 0
data=data.loc[:, data.columns != 'whoAmI']
data=data.astype (int)
print(data)
