#perform imputation technique using only pandas and numpy
import pandas as pd
import numpy as np


data = {"Name" : ["Rishabh", "Anvi", "Tanisha", "Tony", "Ram", "Mohan", "Prince"],
        "Marks" : [98, 86, None, 54, None, 35, None]} #marks are out of 100


pd_data = pd.DataFrame(data, index = [1,2,3,4,5,6,7])
print("BEFORE IMPUTATION")
print(pd_data)

pd_data['Marks'] = pd_data['Marks'].fillna(round(pd_data['Marks'].mean()))
print("\nAFTER IMPUTATION")
print(pd_data)

