

%matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

big_data = pd.read_excel("p1_data.xlsx", sheetname=0)
big_data = big_data.fillna(value="missing")      # Fill NaN/missing/default value
big_data.columns
big_data.T
big_data.describe()
big_data.groupby("Name ").count().plot(kind='bar')
big_data.groupby("Name ").get_group('Praveen Thapliyal').groupby("Name ").count()
big_data.groupby("Name ").count()
big_data_Praveen_Thapliyal = (big_data.groupby("Name ")).get_group('Praveen Thapliyal')
big_data_Praveen_Thapliyal.groupby('Incident ID*+').get_group('missing')
