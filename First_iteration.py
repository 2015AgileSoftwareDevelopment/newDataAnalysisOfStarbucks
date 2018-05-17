import plotly
import pandas as pd

#df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2015_06_30_precipitation.csv')
df = pd.read_csv('./directory.csv');

scl = [0,"rgb(150,0,90)"],[0.125,"rgb(0, 0, 200)"],[0.25,"rgb(0, 25, 255)"],\
[0.375,"rgb(0, 152, 255)"],[0.5,"rgb(44, 255, 150)"],[0.625,"rgb(151, 255, 0)"],\
[0.75,"rgb(255, 234, 0)"],[0.875,"rgb(255, 111, 0)"],[1,"rgb(255, 0, 0)"]

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
                '<br>Timezone:'+df['Timezone'].astype(str),
    marker = dict(
        color = df['Longitude'],
        colorscale = scl,
        reversescale = True,
        opacity = 0.7,
        size = 2,
    ),
    type = 'scattergeo'
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
plotly.offline.plot(fig, filename='precipitation1')
