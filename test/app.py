import dash
import string
import types
import plotly
import time 
import datetime
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import plotly.plotly as py
from plotly.graph_objs import *

dff = pd.read_csv('./directory.csv');
#ans = pd.read_csv('./third.csv');

lx=dff['Longitude']
ly=dff['Latitude']

def draw_plot(Lon,Lat,b,k):
    '''
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
                type = 'gnomonic',
                #rotation = dict(
                #    lon = -100
                #)
            ),
            center = dict(
                lon = Lon,
                lat = Lat
            ),
            lonaxis = dict(
                showgrid = True,
                gridwidth = 0.5,
                range= [ Lon-0.2*k, Lon+0.2*k ],
                dtick = 5
            ),
            lataxis = dict (
                showgrid = True,
                gridwidth = 0.5,
                range= [ Lat-0.1*k, Lat+0.1*k ],
                dtick = 5
            )
        ),
        title = 'Data Analysis Of Starbucks',
    )
    fig = { 'data':data, 'layout':layout }
    plotly.offline.plot(fig, filename='precipitation1')
    '''

    '''
    for i in range(len(b)):
        Lon1 = lx[b[i]]
        Lat1 = ly[b[i]]
        #ans.loc+=df.query("Longitude == '{}' & Latitude == '{}'",format(str(Lon1),str(Lat1)));
        ans.loc+=df[(df["Longitude"]==str(Lon1))&(df["Latitude"]==str(Lat1))]
        #ans.loc+=df.query("Longitude == 'lx[b[i]]' & Latitude == 'ly[b[i]]'")
    '''
    #mask = dff['Latitude'].isin(lx),
    #df=dff[mask],
    #lon11=df[df['Longitude'].isin(ly)],
    #print(str)
    #print(df)
    #lat11.to_csv('./third.csv')
    #df=lat11,
    df = pd.read_csv('./directory.csv')
    df=df.loc[b[0:len(b)]]
    print(df)

    data = Data([
    Scattermapbox(
        lat=df['Latitude'],
        lon=df['Longitude'],
        mode='markers',
        marker=Marker(
            size=9
        ),
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
        )
    ])
    mapbox_access_token="pk.eyJ1IjoiYXVyb3JheXF6IiwiYSI6ImNqZ2hleTFreDA5NnIzM2xrZHBmdXYxa2MifQ.Wg5AgaIalwBStatkhQFwgA"
    layout = Layout(
        autosize=True,
        hovermode='closest',
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            center=dict(
                lat=Lat,
                lon=Lon
            ),
            pitch=0,
            zoom=10
        ),
    )

    fig = { 'data':data, 'layout':layout }
    plotly.offline.plot(fig, filename='precipitation5')

############################################
import queue
import threading

class node(object):
    def __init__(self,priority,description):
        self.priority = priority
        self.description = description
    #下面两个方法重写一个就可以了
    def __lt__(self,other):#operator < 
        return self.priority < other.priority
    def __cmp__(self,other):
        #call global(builtin) function cmp for int
        return cmp(self.priority,other.priority)
    def __str__(self):
        return '(' + str(self.priority)+',\'' + self.description + '\')'



def top_k(lx,ly,k,x,y):
    que = queue.PriorityQueue()
    a=[]
    for i in range(len(lx)):
        #print(''+str(lx[i])+'='+str(ly[i]))
        dis=(lx[i]-x)*(lx[i]-x)+(ly[i]-y)*(ly[i]-y)
        que.put(node(dis,i))
    for i in range(k):
        
        if(que.empty()==False):
            node1=que.get()
            #print(''+str(node1.priority)+' ='+str(node1.description))
            a.append(int(node1.description))
    return a    
#b=top_k(lx,ly,k,x,y)
#for i in range(len(b)):
#    print(''+str(lx[b[i]])+' '+str(ly[b[i]]))

############################################
def op_k(b,k):
    for i in range(0,int(k)):
        print('???')


from dash.dependencies import Input, Output, State

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(id='input-1-state', type='text', value='116.32'),
    dcc.Input(id='input-2-state', type='text', value='39.9'),
    dcc.Input(id='input-3-state', type='text', value='5'),
    html.Button(id='submit-button', n_clicks=0, children='Submit'),
    html.Div(id='output-state')
])

@app.callback(Output('output-state', 'children'),
              [Input('submit-button', 'n_clicks')],
              [State('input-1-state', 'value'),
               State('input-2-state', 'value'),
               State('input-3-state', 'value')])


def update_output(n_clicks, input1, input2, input3):
    #input1=input1*2
    #print("hello"),
    m1=str(input1)
    t1=float(m1)
    m2=str(input2)
    t2=float(m2)
    m3=str(input3)
    k=int(m3)
    print("k="+str(k))
    b=top_k(lx,ly,k,t1,t2)
    #print('='+str(t*2.0)),
    #print("here"),
    time_start=time.time()
    draw_plot(t1,t2,b,k)
    time_end=time.time()

    return u'您输入的经度是:"{}" 您输入的纬度是:"{}" 要查找的店铺个数是:"{}"  程序执行的时间:{}秒'.format(input1,input2,input3,str(time_end-time_start))


if __name__ == '__main__':
    app.run_server(debug=True)
