import pandas as pd

df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                  columns=["C1", "C2", "C3"],
                  index=["I1", "I2", "I3"])

print(df)

df = pd.DataFrame([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16]],
                  columns=["C1", "C2", "C3", "C4"],
                  index=["I1", "I2", "I3", "I4"])

print(df)