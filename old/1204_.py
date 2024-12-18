import pandas as pd


s = [3, 1]
t = ["paiza", "daiza"]
w = []
df = pd.DataFrame({"num": s, "string": t},
                  index=["a", "b"], columns=["num", "string", "new"])

print(df)