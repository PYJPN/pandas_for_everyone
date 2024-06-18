import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('././data/gapminder.tsv', sep='\t')
print(df)  # OK
print(type(df))  # 型
print(df.shape)  # 属性のため、shape（）をつけるとエラーになる
print(df.columns)  # 属性
print(df.dtypes)  # 属性
print(df.info())  # method df for detail info
'''
1.2
'''
'''
1.3
'''
print(df.head())  # head five row

country_df = df['country']  # Only Country Columns Data
print(country_df.head())
print(country_df.tail())  # tail last five row

subset = df[['country', 'continent', 'year']]
print(subset)  # country continent year columns data
# print(df[0]) # key error

country_df = df['country']
print(type(country_df))  # series
print(country_df)

country_df_list = df[['country']]
print(type(country_df_list))  # Data Frame
print(country_df_list)

print(df['country'])  # [] Series
print(df.country)  # . Series

print(df)  # index label row number default
print(df.loc[0])  # index label start row 0
print(df.loc[99])  # index label 100
# print(df.loc[-1]) # keyerror can't last index label
print(df.tail(1))
number_of_rows = df.shape[0]
print(number_of_rows)  # total rows 1704
last_row_index = number_of_rows - 1  # 1704 -1
print(last_row_index)
print(df.loc[last_row_index])
# print(df.loc[number_of_rows])
# keyerror index label 1704 Max index label 1703

print(df.tail(n=1))

subset_loc = df.loc[0]
subset_head = df.head(n=1)
print(type(subset_loc))  # Series
print(type(subset_head))  # DataFrame

print(df.loc[[0, 99, 999]])
print(df.iloc[1])  # OK
print(df.iloc[-1])  # OK last index label
print(df.iloc[[0, 99, 999]])

subset = df.loc[:, ['year', 'pop']]  # .loc[[rows], [columns]] is coumns name
print(subset)
subset = df.iloc[:, [2, 4, -1]]  # .iloc[[row], [columns]] is index label

small_range = list(range(5))
print(small_range)  # [0, 1, 2, 3, 4]
subset = df.iloc[:, small_range]
print(subset)

small_range = list(range(3, 6))
print(small_range)  # 3, 4, 5
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
print(df.groupby('year')['lifeExp'].mean())

grouped_year_df = df.groupby('year')
print(type(grouped_year_df))  # DataFrameGroupBy
print(grouped_year_df)  # DataFrameGroupBy object

grouped_year_df_lifeExp = grouped_year_df['lifeExp']
print(type(grouped_year_df_lifeExp))  # SeriesGroupBy
print(grouped_year_df_lifeExp)  # SeriesGroupBy object

mean_lifeExp_by_year = grouped_year_df_lifeExp.mean()
print(mean_lifeExp_by_year)  # Series
multi_group_var = (
    df.groupby(['year', 'continent'])[
        ['lifeExp', 'gdpPercap']]
    .mean()
)
print(multi_group_var)
multi_group_var.index
print(multi_group_var.index)
# flat.index
# print(flat.index)
flat = multi_group_var.reset_index()
print(flat.index)
# print(grouped_year_df['lifeExp']) # SeriesGroupBy object
# print(grouped_year_df['lifeExp'].mean()) # Series

print(df.groupby('continent')['country'].nunique())
print(df.groupby('continent')['country'].value_counts())
# print(df.groupby('continent')['country'].unique())
'''
1.5
'''
global_yearly_life_expectancy = df.groupby('year')['lifeExp'].mean()
print(global_yearly_life_expectancy)

global_yearly_life_expectancy.plot()
plt.show()
'''
2.1
'''
s = pd.Series(['banana', 42])
print(s)  # 0    banana\n1    42\ndtype: object
s = pd.Series(
    data=['Wes McKinney', 'Creator of Pandas'],
    index=['Person', 'Who']
    )
print(s)
# Person         Wes McKinney\nWho    Creator of Pandas\ndtype: object

scientists = pd.DataFrame(
    data={
        'Name': ['Rosaline Franklin', 'William Gosset'],
        'Occupation': ['Chemist', 'Statistician'],
        'Born': ['1920-07-25', '1876-06-13'],
        'Died': ['1958-04-16', '1937-10-16'],
        'Age': [37, 61]
    },
    index=['Rosaline Franklin', 'William Gosset'],
    columns=['Occupation', 'Born', 'Died', 'Age']
)
print(scientists)
#  Occupation        Born        Died  Age\n
#  Rosaline Franklin    Chemist  1920-07-25  1958-04-16   37\n
#  William Gosset  Statistician  1876-06-13  1937-10-16   61
#  print(scientists)
#  Name Occupation        Born        Died  Age\n
#  0  Rosaline Franklin    Chemist  1920-07-25  1958-04-16   37\n
#  1     William Gosset  Statistician  1876-06-13  1937-10-16   61

first_row = scientists.loc['William Gosset']
print(type(first_row))  # Series
print(first_row)
# Occupation    Statistician\n
# Born            1876-06-13\n
# Died            1937-10-16\n
# Age                     61\n
# dtype: object
print(first_row.index)
# Index(['Occupation', 'Born', 'Died', 'Age'], dtype='object')
print(first_row.values)
# ['Statistician' '1876-06-13' '1937-10-16' 61]
print(first_row.keys())
# Index(['Occupation', 'Born', 'Died', 'Age'], dtype='object')
print(first_row.index[0])
print(first_row.keys()[0])
print(first_row.index[-1])
print(first_row.keys()[-1])

ages = scientists['Age']
print(ages)
print(ages.mean())
print(ages.min())
print(ages.max())
print(ages.std())
print(ages.describe())
"""
2024/05/27
"""
'''
2.2.2
'''
scientists = pd.read_csv('././data/scientists.csv')
ages = scientists['Age']
print(ages)
print(ages.describe())
print(ages.mean())
print(ages[ages > ages.mean()])  # True
print(ages > ages.mean())  # True False

manual_bool_values = [True, True, False, False, True, True, False, True]
print(ages[manual_bool_values])  # True
print(ages + ages)  # 2 * ages
print(ages * ages)  # ages ** 2
print(ages + 100)  # ages + 100
print(ages * 2)  # 2 * ages
print(pd.Series([1, 100]))
# 0      1\n1    100\n
# dtype: int64
print(ages + pd.Series([1, 100]))  # NaN 100

# print(ages + np.array([1, 100]))  # NaN 100 Value Error
print(ages)
rev_ages = ages.sort_index(ascending=False)
print(rev_ages)
print(ages * 2)  # 2 * ages
print(ages + rev_ages)  # ages + rev_ages
# 2024/06/16 19:56
# 2.3 P.43
print(ages * 2)

scientists.index
scientists.columns
