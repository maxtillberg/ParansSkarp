import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
from textwrap import dedent

########### Get Data

df_test = pd.read_csv('testspektra.csv')


# Gapminder dataset GAPMINDER.ORG, CC-BY LICENSE
url = "https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv"
df = pd.read_csv(url)
df = df.rename(index=str, columns={"pop": "population",
                                   "lifeExp": "life_expectancy",
                                   "gdpPercap": "GDP_per_capita"})


########### Set up the chart

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

UFD = go.Scatter(
    x=df_test.Wavelength_nm,
    y=df_test.UFD,
    mode = 'lines',
    name='UFD',
    marker={'color':'red'}
)
P50M = go.Scatter(
    x=df_test.Wavelength_nm,
    y=df_test.P50M,
    mode = 'lines',
    name='P50M',
    marker={'color':'blue'}
)
TG = go.Scatter(
    x=df_test.Wavelength_nm,
    y=df_test.TG,
    mode = 'lines',
    name='TG',
    marker={'color':'blue'}
)
SPG = go.Scatter(
    x=df_test.Wavelength_nm,
    y=df_test.SPG,
    mode = 'lines',
    name='SPG',
    marker={'color':'blue'}
)
CLED = go.Scatter(
    x=df_test.Wavelength_nm,
    y=df_test.CLED,
    mode = 'lines',
    name='CLED',
    marker={'color':'blue'}
)
WLED = go.Scatter(
    x=df_test.Wavelength_nm,
    y=df_test.WLED,
    mode = 'lines',
    name='WLED',
    marker={'color':'blue'}
)


Spectra_data = [UFD, P50M, TG, SPG, CLED, WLED]
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
    
    html.Div(id='my-div'),
    
    
    dcc.Graph(
        id='spektra',
        figure=Spectra_fig
    ),

    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': i, 'value': i} for i in df.country.unique()],
        multi=False,
        value=['Australia']
    ),
   
    dcc.Graph(id='timeseries-graph')
]
)

########### Callbacks!

@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='droplista', component_property='value')]
)
def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)


@app.callback(
    dash.dependencies.Output('timeseries-graph', 'figure'),
    [dash.dependencies.Input('country-dropdown', 'value')])
def update_graph(country_values):
    dff = df.loc[df['country'].isin(country_values)]

    return {
        'data': [go.Scatter(
            x=dff[dff['country'] == country]['year'],
            y=dff[dff['country'] == country]['GDP_per_capita'],
            text="Continent: " +
                  f"{dff[dff['country'] == country]['continent'].unique()[0]}",
            mode='lines+markers',
            name=country,
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'white'}
            }
        ) for country in dff.country.unique()],
        'layout': go.Layout(
            title="GDP over time, by country",
            xaxis={'title': 'Year'},
            yaxis={'title': 'GDP Per Capita'},
            margin={'l': 60, 'b': 50, 't': 80, 'r': 0},
            hovermode='closest'
        )
    } 
 
 
########### Run app!


if __name__ == '__main__':
    app.run_server()
