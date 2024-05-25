import pandas as pd
df = pd.read_csv('././data/gapminder.tsv', sep='\t')
print(df) # OK
print(type(df)) # 型
print(df.shape) # 属性のため、shape（）をつけるとエラーになる
print(df.columns) # 属性
print(df.dtypes) # 
print(df.info()) # method df for detail info
''' 1.2 '''
''' 1.3 '''
print(df.head()) # head five row

country_df = df['country'] # Only Country Columns Data
print(country_df.head())
print(country_df.tail()) # tail last five row

subset = df[['country', 'continent', 'year']]
print(subset) # 
# print(df[0]) # key error

country_df = df['country']
print(type(country_df)) # series
print(country_df)

country_df_list = df[['country']]
print(type(country_df_list)) # Data Frame
print(country_df_list)

print(df['country']) # [] Series 
print(df.country) # . Series

print(df) # index label row number default
print(df.loc[0]) # index label start row 0
print(df.loc[99]) # index label 100
#print(df.loc[-1]) # keyerror can't last index label
print(df.tail(1))
number_of_rows = df.shape[0]
print(number_of_rows) # total rows 1704
last_row_index = number_of_rows -1 # 1704 -1
print(last_row_index)
print(df.loc[last_row_index])
#print(df.loc[number_of_rows]) # keyerror index label 1704 Max index label 1703

print(df.tail(n=1))

subset_loc = df.loc[0]
subset_head = df.head(n=1)
print(type(subset_loc)) # Series
print(type(subset_head)) # DataFrame

print(df.loc[[0, 99, 999]])
print(df.iloc[1]) # OK
print(df.iloc[-1]) # OK last index label 
print(df.iloc[[0, 99, 999]])

subset = df.loc[:, ['year', 'pop']] # .loc[[rows], [columns]] is coumns name
print(subset)
subset = df.iloc[:, [2, 4, -1]] # .iloc[[row], [columns]] is index label

small_range = list(range(5))
print(small_range) # [0, 1, 2, 3, 4]
subset = df.iloc[:, small_range]
print(subset)

small_range = list(range(3, 6))
print(small_range) # 3, 4, 5
subset = df.iloc[:, small_range]
print(subset)

subset = df.iloc[:, :3]
print(subset)

subset = df.iloc[:, 3:6]
print(subset)

small_range = list(range(0, 6, 2))
subset = df.iloc[:, small_range]
print(subset)

subset = df.iloc[:, 0:6:2]
print(subset)

subset = df.iloc[:, 0:6:]
print(subset)

subset = df.iloc[:, 0::2]
print(subset)

subset = df.iloc[:, ::2]
print(subset)

subset = df.iloc[:, ::]
print(subset)

print(df.loc[42, 'country'])
print(df.iloc[42, 0])

print(df.iloc[[0, 99, 999], [0, 3, 5]])
print(df.loc[[0, 99, 999], ['country', 'lifeExp', 'gdpPercap']])

print(df.loc[10:13, :])  # 10 to 13
print(df.iloc[10:13, :])  # 10 to 12 Do you OK?
""" 
1.4 
"""
print(df)








