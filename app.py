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

#beers=['Chesapeake Stout', 'Snake Dog IPA', 'Imperial Porter', 'Double Dog IPA']

bitterness = go.Scatter(
    x=df_test.Wavelength_nm,
    y=df_test.UFD,
    mode = 'lines',
    name='UFD',
    marker={'color':'red'}
)
alcohol = go.Scatter(
    x=df_test.Wavelength_nm,
    y=df_test.P50M,
    mode = 'lines',
    name='P50M',
    marker={'color':'blue'}
)

Spectra_data = [bitterness, alcohol]
Spectra_layout = go.Layout(
    barmode='group',
    title = 'Liiiiight!!!'
)

Spectra_fig = go.Figure(data=Spectra_data, layout=Spectra_layout)

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
        figure=Spectra_fig
    )]
)

if __name__ == '__main__':
    app.run_server()
