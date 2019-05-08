import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

########### Get Data

df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/'
    'c78bf172206ce24f77d6363a2d754b59/raw/'
    'c353e8ef842413cae56ae3920b8fd78468aa4cb2/'
    'usa-agricultural-exports-2011.csv')

df_test = pd.read_csv('testspektra.csv')

########### Set up the chart

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

beers=['Chesapeake Stout', 'Snake Dog IPA', 'Imperial Porter', 'Double Dog IPA']

bitterness = go.Scatter(
    x=beers,
    y=[35, 60, 85, 75],
    mode = 'lines',
    name='IBU',
    marker={'color':'red'}
)
alcohol = go.Scatter(
    x=beers,
    y=[5.4, 7.1, 9.2, 4.3],
    mode = 'lines',
    name='ABV',
    marker={'color':'blue'}
)

beer_data = [bitterness, alcohol]
beer_layout = go.Layout(
    barmode='group',
    title = 'Liiiiight!!!'
)

beer_fig = go.Figure(data=beer_data, layout=beer_layout)

########### Display the chart

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.layout = html.Div(children=[
    html.H1('Parans Beta'),
    
    html.Label('Choose Lightsource'),
    
    dcc.Dropdown(
        options=[
            {'label': 'Unfiltered daylight', 'value': 'UFD'},
            {'label': u'Daylight through Parans 50m', 'value': 'P50M'},
            {'label': 'Daylight through 2-pane thermal glass', 'value': 'TG'},
            {'label': 'Daylight through 2-pane solar protection glass', 'value': 'SPG'},
            {'label': 'Cool white LED', 'value': 'CLED'},
            {'label': 'Warm white LED', 'value': 'WLED'}
        ],
        value=['UFD'],
        multi=True
    ),
    
    
    dcc.Graph(
        id='flyingdog',
        figure=beer_fig
    )]
)

if __name__ == '__main__':
    app.run_server()
