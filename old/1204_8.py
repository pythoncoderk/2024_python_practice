import pandas as pd

df = pd.DataFrame([[1, 4, 7], [2, 5, 8], [3, 6, 9]],
                  columns=["カラム1", "カラム2", "カラム3"],
                  index=["インデックス1", "インデックス2", "インデックス3"])
print(df)


df = pd.DataFrame([[1, 4, 7],[2, 5, 8], [3, 6, 9]],
                  columns=["A", "B", "C"],
                  index=["1", "2", "3"])

print(df)

df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                  columns=["C1", "C2", "C3"],
                  index=["I1", "I2", "I3"])

print(df)

df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                  columns=["C1", "C2", "C3"],
                  index=["I1", "I2", "I3"])

print(df)


df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                  columns=["C1", "C2", "C3"],
                  index=["I1", "I2", "I3"])

print(df)