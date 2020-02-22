import pandas as pd
import numpy as np
import sys
a= [1, 2, 3]
b = [4,5,6]

c = np.array([a,b])
c = np.transpose(c)
print(c)
sys.exit(0)
y_df=pd.DataFrame(data = c)

y_df.to_csv("C:/Users/sunng/PycharmProjects/Nba_Playoff_predic/raw_data/raw_data.csv", sep=',', encoding='utf-8')

