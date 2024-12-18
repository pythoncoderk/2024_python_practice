import pandas as pd


s = pd.Series({"c": 1, "d": 2, "e": 3})
ind = ["c", "e"]

print(s[ind])