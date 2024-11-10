import pandas as pd

s = pd.Series({"a": 3, "b": 1, "c": 2})
ind = ["a", "b", "c"]
s2 = pd.Series(1, index=ind)
s3 = pd.Series([3, 1, 2], index=["a", "b", "c"])
print(s3)

