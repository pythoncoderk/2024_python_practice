import numpy as np
import pandas as pd

df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                  columns=["C1", "C2", "C3"],
                  index=["I1", "I2", "I3"])

print(df)