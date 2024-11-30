import pandas as pd
import numpy as np


df = pd.read_csv(r"C:\Users\turnt\OneDrive\デスクトップ\dataset\citibike_trips_2017_sampled.csv")
print(df)

print(df["tripduration"] + 3)

print(df["tripduration"].median())

print(df["tripduration"].max())

print(df["tripduration"].sum())