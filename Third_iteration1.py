import plotly
import pandas as pd

#df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2015_06_30_precipitation.csv')
df = pd.read_csv('./time.csv');

scl =  [[0,"rgb(255,0,102)"],[0.08,"rgb(255,23,93)"],[0.17,"rgb(255,46,83)"],\
                    [0.25,"rgb(255,70,74)"],[0.34,"rgb(255,93,65)"],[0.42,"rgb(255,116,56)"],\
                    [0.5,"rgb(255,139,46)"],[0.6,"rgb(255,162,37)"],[0.7,"rgb(255,185,28)"],\
                    [0.8,"rgb(255,209,19)"],[0.9,"rgb(255,232,9)"],[1,"rgb(255,255,0)"]]

data = [ dict(
    lat = df['Latitude'],
    lon = df['Longitude'],
    text = 'Store Number:'+df['Store Number'].astype(str)+
                '<br>Store Name:'+df['Store Name'].astype(str)+
                '<br>Ownership Type:'+df['Ownership Type'].astype(str)+
                '<br>Street Address:'+df['Street Address'].astype(str)+
                '<br>City:'+df['City'].astype(str)+
                '<br>State/Province:'+df['State/Province'].astype(str)+
                '<br>Country:'+df['Country'].astype(str)+
                '<br>Postcode:'+df['Postcode'].astype(str)+
                '<br>Phone Number:'+df['Phone Number'].astype(str)+
                '<br>Timezone:'+df['Timezone'].astype(str)+
                '<br>TimezoneCounts:'+df['Time'].astype(str),
    marker = dict(
        color = df['Time'],
        colorscale = scl,
        reversescale = True,
        opacity = 0.7,
        size = 2,
        colorbar = dict(
            thickness = 50,
            title = '不同时区数量分布'
        ),
    ),
    type = 'scattergeo',

) ]

layout = dict(
    geo = dict(
        scope = 'world',
        showland = True,
        landcolor = "rgb(212, 212, 212)",
        subunitcolor = "rgb(255, 255, 255)",
        countrycolor = "rgb(255, 255, 255)",
        showlakes = True,
        lakecolor = "rgb(255, 255, 255)",
        showsubunits = True,
        showcountries = True,
        resolution = 50,
        projection = dict(
            type = 'equirectangular',
            rotation = dict(
                lon = -100
            )
        ),
        lonaxis = dict(
            showgrid = True,
            gridwidth = 0.5,
            range= [ -180.0, 180.0 ],
            dtick = 5
        ),
        lataxis = dict (
            showgrid = True,
            gridwidth = 0.5,
            range= [ -90.0, 90.0 ],
            dtick = 5
        )
    ),
    title = 'Data Analysis Of Starbucks',
)
fig = { 'data':data, 'layout':layout }
plotly.offline.plot(fig, filename='precipitation3')
