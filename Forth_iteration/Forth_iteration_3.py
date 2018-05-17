#!/usr/bin/python
#coding:utf-8
import dash
import string
import types
import plotly
import math
import time 
import datetime
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import plotly.plotly as py
from plotly.graph_objs import *
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

dff = pd.read_csv('./directory.csv');
#ans = pd.read_csv('./third.csv');

def draw_plot(Lon,Lat,k):
    ss1 = process.extract(k,dff['Store Name'],limit = 10)
    ss2 = process.extract(k,dff['Street Address'],limit = 10)
    ss3 = process.extract(k,dff['Store Number'],limit = 10)

    all_ss = ss1+ss2+ss3
    sort_ss = sorted(all_ss, key=lambda all_ss: all_ss[1], reverse = True)

    sss = []
    for x in sort_ss:
        sss.append(x[2])

    df = []
    df = dff.iloc[sss,:]
    #df.append(dff.iloc[sss2,:])

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
    plotly.offline.plot(fig, filename='precipitation4_3')

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
    dcc.Input(id='input-1-state', type='text', value='113.58'),
    dcc.Input(id='input-2-state', type='text', value='22.28'),
    dcc.Input(id='input-3-state', type='text', value='珠海'),
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
    k=str(m3)
    #print("k="+str(k))
    #b=top_k(lx,ly,k,t1,t2)
    #print('='+str(t*2.0)),
    #print("here"),
    time_start=time.time()
    draw_plot(t1,t2,m3)
    time_end=time.time()

    return u'您输入的经度是:"{}" 您输入的纬度是:"{}" 您输入的关键字是:"{}"  程序执行的时间:{}秒'.format(input1,input2,input3,str(time_end-time_start))


if __name__ == '__main__':
    app.run_server(debug=True)
