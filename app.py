import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

########### Get Data

df_skarp = pd.read_csv('spektraldata_v2.csv')

########### Set up the chart

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Added color definition per data type. As seen below, both rgb and colornames work.
colors = {
            'Unfiltered daylight':'rgb(0,0,0)',
            'Parans 54m':'rgb(247,190,75)',
            'Parans 25m':'rgb(239,122,92)',
            'Fluorescent lamp FL5':'rgb(0,167,151)',
            'LED 2700 K':'rgb(51,37,85)',
            'LED 4000 K':'rgb(233,68,130)',
            'Daylight through glass':'rgb(149,200,232)',
}

########### Display the chart

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.layout = html.Div(children=[
    html.H1('Relative spectral power'),



    html.Label('Choose Lightsource'),

    dcc.Dropdown(
        id='droplista',
        options=[
            #{'label': 'beta_Unfiltered daylight', 'value': 'Unfiltered Daylight'},
            #{'label': u'beta_Daylight through Parans 50m', 'value': 'Parans 50 m'},
            #{'label': 'beta_Daylight through 2-pane thermal glass', 'value': 'Thermal Glass'},
            #{'label': 'beta_Daylight through 2-pane solar protection glass', 'value': 'Solar Protection Glass'},
            #{'label': 'beta_Cool white LED', 'value': 'Cool White LED'},
            #{'label': 'beta_Warm white LED', 'value': 'Warm White LED'},

            {'label': 'Unfiltered daylight', 'value': 'Unfiltered daylight'},
            {'label': 'Daylight through Parans 54 m', 'value': 'Parans 54m'},
            {'label': 'Daylight through Parans 25 m', 'value': 'Parans 25m'},
            {'label': 'Flourecent lamp FL5', 'value': 'Fluorescent lamp FL5'},
            {'label': 'Cool white LED', 'value': 'LED 2700 K'},
            {'label': 'Warm white LED', 'value': 'LED 4000 K'},
            {'label': 'Daylight through modern solar protection glass', 'value': 'Daylight through glass'}
        ],
        value=['Unfiltered daylight'],
        multi=True
    ),




    dcc.Graph(
        id='spektra'
    ),


    #html.Div(id='my-div', style={'marginBottom': 50, 'marginTop': 25}),

]
)

########### Callbacks!

#@app.callback(
#    Output(component_id='my-div', component_property='children'),
#    [Input(component_id='droplista', component_property='value')]
#)
#def update_output_div(input_value):
#    return 'You\'ve entered "{}"'.format(input_value)


@app.callback(
    dash.dependencies.Output('spektra', 'figure'),
    [dash.dependencies.Input('droplista', 'value')])
def update_graph(valda_serier):
    cols=valda_serier.copy()
    cols.extend(['Wavelength_nm'])
    df_vald = df_skarp[cols]
    trace=[]
    for serie in valda_serier:
        trace=trace+[go.Scatter(
            x=df_vald['Wavelength_nm'],
            y=df_vald[serie],
            hoverinfo="y",
            mode='lines',
            name=serie,
            line = dict(
                color = (colors[serie]), # colors['Unfiltered daylight'] = 'black', See Colors just below css import
                width = 2,)
        )]

    trace_text=go.Scatter(
    x=[550],
    y=[-0.12],
    text=['Visible spectra'],
    mode='text',
    showlegend=False
    )

    trace.extend([trace_text])

    return {
        'data': trace,


        'layout': go.Layout(
            title="Relative spectral power",
            xaxis={'title': 'Frequency [nm]', 'range': [300,2500]},
            yaxis={'title': 'Relative spectral power [%]', 'range': [-0.19, 1.05]},
            showlegend=True,
            shapes=[dict(type='rect',
                    layer='below',
                    xref='x',
                    yref='paper',
                    x0=380,
                    y0=0,
                    x1=740,
                    y1=1,
                    opacity=0.3,
                    fillcolor='#d3d3d3',
                    line=dict(width=0)
                )]


        )
    }


########### Run app!


if __name__ == '__main__':
    app.run_server()
