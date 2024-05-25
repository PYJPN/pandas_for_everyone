import pandas as pd
df = pd.read_csv('././data/gapminder.tsv', sep='\t')
print(df) # OK
print(type(df)) # 型
print(df.shape) # 属性のため、shape（）をつけるとエラーになる
print(df.columns) # 属性
print(df.dtypes) # 
print(df.info()) # method df for detail info


