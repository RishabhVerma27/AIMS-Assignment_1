#perform ordinal encoding technique using only pandas and numpy
import pandas as pd
import numpy as np 


data = {"Name" : ["Rishabh", "Anvi", "Tanisha", "Tony", "Ram", "Mohan", "Prince"],
        "Grade" : ["A", "A", "B", "C", "B", "C", "B"]}

order = {"A":2, "B":1, "C":0}

pd_data = pd.DataFrame(data, index = [1,2,3,4,5,6,7])
pd_data["Ordinal Encoding"] = pd_data["Grade"].map(order)

print(pd_data)