import pandas as pd


s = pd.Series({"a": 3, "b": 1, "c": 2})
ind = ["d", "e", "f"]
s.index = ind

print(s)
