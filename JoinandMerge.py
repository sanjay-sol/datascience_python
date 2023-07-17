import pandas as pd
data1 = {'ID': [1, 2, 3, 4, 5],
         'Name': ['John', 'Alice', 'Bob', 'Lisa', 'Mike'],
         'Age': [28, 32, 45, 31, 27]}
df1 = pd.DataFrame(data1)
data2 = {'ID': [2, 4, 6, 8, 10],
         'Salary': [5000, 7000, 4000, 6000, 8000]}
df2 = pd.DataFrame(data2)
df_inner = pd.merge(df1, df2, on='ID', how='inner')
print("Inner Join:")
print(df_inner)
df_left = pd.merge(df1, df2, on='ID', how='left')
print("Left Join:")
print(df_left)
df_right = pd.merge(df1, df2, on='ID', how='right')
print("Right Join:")
print(df_right)
df_outer = pd.merge(df1, df2, on='ID', how='outer')
print("Outer Join:")
print(df_outer)
df_concat = pd.concat([df1, df2], axis=1)
print("Concatenation:")
print(df_concat)