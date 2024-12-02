import pandas as pd


s = pd.Series({"a": 3, "b": 1, "c": 2})
new_s = s.rename("paiza")
s.rename("paiza", inplace=True)
print(s)