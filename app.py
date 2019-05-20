import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
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

UFD_df = go.Scatter(
    x=df_test.Wavelength_nm,
    y=df_test.UFD,
    mode = 'lines',
    name='UFD',
    marker={'color':'red'}
)
P50M_df = go.Scatter(
    x=df_test.Wavelength_nm,
    y=df_test.P50M,
    mode = 'lines',
    name='P50M',
    marker={'color':'blue'}
)
TG_df = go.Scatter(
    x=df_test.Wavelength_nm,
    y=df_test.TG,
    mode = 'lines',
    name='TG',
    marker={'color':'blue'}
)
SPG_df = go.Scatter(
    x=df_test.Wavelength_nm,
    y=df_test.SPG,
    mode = 'lines',
    name='SPG',
    marker={'color':'blue'}
)
CLED_df = go.Scatter(
    x=df_test.Wavelength_nm,
    y=df_test.CLED,
    mode = 'lines',
    name='CLED',
    marker={'color':'blue'}
)
WLED_df = go.Scatter(
    x=df_test.Wavelength_nm,
    y=df_test.WLED,
    mode = 'lines',
    name='WLED',
    marker={'color':'blue'}
)

Spectra_data = [UFD_df, P50M_df, TG_df, SPG_df, CLED_df, WLED_df]
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
    
    #dcc.Input(id='my-id', value='initial value', type='text'),
    
    
    html.Label('Choose Lightsource'),
    
    dcc.Dropdown(
        id='droplista',
        options=[
            {'label': 'Unfiltered daylight', 'value': 'UFD_df'},
            {'label': u'Daylight through Parans 50m', 'value': 'P50M_df'},
            {'label': 'Daylight through 2-pane thermal glass', 'value': 'TG_df'},
            {'label': 'Daylight through 2-pane solar protection glass', 'value': 'SPG_df'},
            {'label': 'Cool white LED', 'value': 'CLED_df'},
            {'label': 'Warm white LED', 'value': 'WLED_df'}
        ],
        value=['UFD_df'],
        multi=True
    ),
    
    html.Div(id='my-div'),
    
    dcc.Graph(
        id='flyingdog',
        figure=Spectra_fig
    )]
)

########### Callbacks!

@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='droplista', component_property='value')]
)
def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)



########### Run app!


if __name__ == '__main__':
    app.run_server()
