from numpy import average
import pandas as pd
import plotly.express as px
#obtaining data
print("loading spotify dataset...")
dataframe=pd.read_csv("spotify-2023.csv", encoding='latin1')
#cleaning and categorising
dataframe['streams']=pd.to_numeric(dataframe['streams'],errors='coerce')
dataframe=dataframe.dropna(subset=['streams'])

average_streams=dataframe['streams'].mean()
print(f"average top song:{average_streams:,.0f} streams")

print("3d visulization")
figure=px.scatter_3d(
    dataframe,
    x='bpm',
    y='danceability_%',
    z='streams',
    color='streams',
    hover_name='track_name',
    title="spotify analytics"
)
figure.show()
