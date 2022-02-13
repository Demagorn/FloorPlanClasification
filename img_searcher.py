import pandas as pd
df = pd.read_csv(r"C:\Users\marin\PycharmProjects\FloorPlanClasification\Data\More Floorplans Dataset (1).csv")
for value in df['Number of bedrooms'].unique():
  df_new = df.loc[df['Number of bedrooms']==value]
  df_new["Image Path"].to_csv(f"{value}.csv")
