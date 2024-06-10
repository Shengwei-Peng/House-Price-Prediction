import os
import math
import pandas as pd
from pyproj import Proj
from tqdm import tqdm

def distance_score(data1, data2, threshold):

    score = []
    for i in tqdm(range(len(data1)),
                  desc=f"Distance < {threshold}m",
                  ncols=100,
                  unit_scale=True,
                  colour="red"
                  ):
        num = 0
        for j in range(len(data2)):
            distance = math.sqrt(
                ((data1["縱坐標"][i] - data2["縱坐標"][j]) ** 2)
                + ((data1["橫坐標"][i] - data2["橫坐標"][j]) ** 2)
                )
            if (distance) < threshold:
                num += 1
        score.append(num)

    return score

twd97 = Proj(proj="tmerc",
             lat_0=0,
             lon_0=121,
             k=0.9999,
             x_0=250000,
             y_0=0,
             ellps="GRS80")

path = "./data/30_Public Dataset_Public Sumission Template_v2"
train = pd.read_csv(f"{path}/public_dataset.csv")

folder_path = "./data/30_Training Dataset_V2/external_data"
files = os.listdir(folder_path)

for file in files:
    data2 = pd.read_csv(f"{folder_path}/{file}")
    data2 = data2[["lat", "lng"]]
    data2["lng"], data2["lat"] = twd97(data2["lng"], data2["lat"])
    data2 = data2.rename(columns={"lat": "縱坐標", "lng": "橫坐標"})
    train[f"{file}"] = distance_score(
        data1=train,
        data2=data2,
        threshold=10000)
    train.to_csv(
        f"{path}/public_dataset_processed.csv",
        index=False,
        )
