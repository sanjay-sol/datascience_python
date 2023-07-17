data = {'Product': ['A', 'B', 'A', 'B', 'A', 'C', 'B', 'C', 'A', 'C'],
        'Quantity': [10, 15, 5, 8, 12, 7, 9, 4, 6, 11],
        'Price': [100, 150, 200, 120, 90, 80, 130, 70, 110, 60]}
df=pd.DataFrame(data)

df
df['Product'].unique()

print('Grouping Product to find sum:')
df.groupby(['Product']).agg('sum')

print('Grouping Product to find mean:')
df.groupby(['Product']).agg('mean')

print('Grouping Product to find min:')
df.groupby(['Product']).agg('min')

print('Grouping Product to find max:')
df.groupby(['Product']).agg('max')