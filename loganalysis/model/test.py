import pandas as pd

data = []
data.extend([('x', 'b', 1), ('x', 'c', 2), ('y', 'c', 5), ('x', 'b', 2)])
df = pd.DataFrame(data,
    columns=['url', 'method', 'count']
)
print(df)
print(df.groupby(['url', 'method']).sum())
print(df.groupby(['url', 'method']).sum().to_json(orient='index'))