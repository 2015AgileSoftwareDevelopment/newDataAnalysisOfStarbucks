import plotly
import pandas as pd

df = pd.read_csv('./CountryCount.csv')

#df = df.head(100)

data = [ dict(
        type = 'choropleth',
        locations = df['Country'],
        z = df['Count'],
        text = df['Name'],
        colorscale = [[0,"rgb(255,0,102)"],[0.2,"rgb(255,23,93)"],[0.4,"rgb(255,46,83)"],\
                    [0.5,"rgb(255,70,74)"],[0.6,"rgb(255,93,65)"],[0.7,"rgb(255,116,56)"],\
                    [0.8,"rgb(255,139,46)"],[0.85,"rgb(255,162,37)"],[0.9,"rgb(255,185,28)"],\
                    [0.94,"rgb(255,209,19)"],[0.97,"rgb(255,232,9)"],[1,"rgb(255,255,0)"]],
        autocolorscale = False,
        reversescale = True,
        marker = dict(
            line = dict (
                color = 'rgb(180,180,180)',
                width = 0.5
            ) ),
        colorbar = dict(
            #autotick = False,
            #tickprefix = '$',
            thickness = 50,
            title = '数量和密度分布'),
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

fig = dict( data=data, layout=layout )
plotly.offline.plot(fig, validate=False,filename='precipitation2.html')