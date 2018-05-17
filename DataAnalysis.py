import plotly
import pandas as pd

df = pd.read_csv('./directory.csv');

#data_analysis_1=df[(df.Longitude > 0) & (df.Longitude<15)]

for num in range(-180,180,15):
	data_analysis=df[(df.Longitude >= num) & (df.Longitude<=(15+num))]
	print(data_analysis.Longitude.describe())

