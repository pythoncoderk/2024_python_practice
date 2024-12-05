import pandas as pd
import numpy as np

df = pd.DataFrame({"C1":[1, 2, 3],
                   "C2": [4, 5, 6],
                   "C3": [7, 8, 9]},
                  index=["I1", "I2", "I3"])

print(df.values)