import pandas as pd
from dateutil.parser import parse

df = pd.read_csv('testdtindex.csv', header=0)
for i, s in enumerate(df["DateTime"]):
    ps = parse(s[:-2])
    df = df.replace(s, ps)

df = df.set_index("DateTime", drop=True, )
print(df)
print(df.index)
