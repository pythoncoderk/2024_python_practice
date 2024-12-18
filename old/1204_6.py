import pandas as pd


s = pd.Series({"a": 3, "b": 1})
t = pd.Series({"a": "paiza", "c": "daiza"})
df = pd.DataFrame({"num": s, "string": t})

print(df.loc["a"])