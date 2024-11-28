import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\turnt\OneDrive\デスクトップ\dataset\citibike_trips_2017_sampled.csv")
print(df)

df2 = df.query('(dayofweek == "Mon")')

print(df2["tripduration"].sum())

