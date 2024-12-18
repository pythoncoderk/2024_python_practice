import pandas as pd


s = pd.Series({"a": 3, "b": 1, "c": 2})
s["b"] = 813

print(s)