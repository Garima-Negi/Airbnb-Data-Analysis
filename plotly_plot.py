import plotly.plotly as py
from plotly.graph_objs import *
import csv

mapbox_access_token = 'pk.eyJ1IjoiYXJqdW5wcmFiaHUiLCJhIjoiY2oyZGNsdDJuMDYzdjJ3bzhhd2YzYnFoNSJ9.ICWaMZNysZL5JPNlK1iboQ'

latitude = []
longitude = []
info = []

with open("/Users/arjun/Zeppelin/NYC/listings_other/listings_other.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        latitude.append(row[0])
        longitude.append(row[1])
        info.append(row[3])

data = Data([
    Scattermapbox(
        lat=latitude,
        lon=longitude,
        mode='markers',
        marker=Marker(
            size=17,
            color='rgb(255, 0, 0)',
            opacity=0.7
        ),
        text=info,
        hoverinfo='text'
    )
])

layout = Layout(
    autosize=True,
    hovermode='closest',
    mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(
            lat=latitude[4],
            lon=longitude[4]
        ),
        pitch=0,
        zoom=10.4
    ),
)

fig = dict(data=data, layout=layout)
py.iplot(fig, filename='Other_NYC')