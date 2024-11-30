import pandas as pd

df = pd.DataFrame(
    {
    "性別":["男", "女", "男"],
    "出身地":["okinawa", "hokkaido", "tokyo"],
    "身長":[177, 164, 172],
    "体重":[71, 51, 64],
    "氏名":["fukuda", "sonobe", "hashimoto"]
    }
    )

print(df)