import pandas as pd


s = pd.Series({"a": 3, "b": 1})
t = pd.Series({"a": "paiza", "c": "daiza"})

df = pd.DataFrame({"count": s, "name":t})
print(df)