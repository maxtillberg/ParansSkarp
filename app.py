import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

########### Get Data

df_test = pd.read_csv('testspektra.csv')

########### Set up the chart

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


########### Display the chart

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.layout = html.Div(children=[
    html.H1('Header'),



    html.Label('Choose Lightsource'),

    dcc.Dropdown(
        id='droplista',
        options=[
            {'label': 'Unfiltered daylight', 'value': 'Unfiltered Daylight'},
            {'label': u'Daylight through Parans 50m', 'value': 'Parans 50 m'},
            {'label': 'Daylight through 2-pane thermal glass', 'value': 'Thermal Glass'},
            {'label': 'Daylight through 2-pane solar protection glass', 'value': 'Solar Protection Glass'},
            {'label': 'Cool white LED', 'value': 'Cool White LED'},
            {'label': 'Warm white LED', 'value': 'Warm White LED'}
        ],
        value=['Unfiltered Daylight'],
        multi=True
    ),

    html.Div(id='my-div'),


    dcc.Graph(
        id='spektra'
    )

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
    dash.dependencies.Output('spektra', 'figure'),
    [dash.dependencies.Input('droplista', 'value')])
def update_graph(valda_serier):

    cols=valda_serier.copy()
    cols.extend(['Wavelength_nm'])
    df_vald = df_test[cols]

    return {
        'data': [go.Scatter(
            x=df_vald['Wavelength_nm'],
            y=df_vald[serie],
            mode='lines',
            name=serie
        ) for serie in valda_serier],


        'layout': go.Layout(
            title="Daylight spectrum through filters",
            xaxis={'title': 'Frequency [nm]'},
            yaxis={'title': 'Relative energy intensity [%]'},
            showlegend=True
        )
    }


########### Run app!


if __name__ == '__main__':
    app.run_server()
