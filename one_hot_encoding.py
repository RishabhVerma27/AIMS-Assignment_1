#perform one hot encoding technique using only pandas and numpy
import pandas as pd
import numpy as np

data = {"Color" : ["Red", "Blue", "Green", "Cyan", "Red", "Cyan", "Cyan", "Blue"]}

pd_data = pd.DataFrame(data, index=[1,2,3,4,5,6,7,8])

unique_color = pd_data["Color"].unique()

for val in unique_color:
    pd_data[val] = (pd_data['Color'] == val).astype(int)

print(pd_data) 

# pd_data["Is_Red"] = np.where(pd_data['Color'] == "Red", 1, 0)
# pd_data["Is_Blue"] = np.where(pd_data['Color'] == "Blue", 1, 0)
# pd_data["Is_Green"] = np.where(pd_data['Color'] == "Green", 1, 0)
# pd_data["Is_Cyan"] = np.where(pd_data['Color'] == "Cyan", 1, 0)

# print(pd_data)
