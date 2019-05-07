import dash
import dash_table
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html

#df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')
df = pd.read_csv('2011_us_ag_exports.csv')
df1 = df[1:5]
app = dash.Dash(__name__)

server = app.server






external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])




#app.layout = dash_table.DataTable(
#    id='table',
#    columns=[{"name": i, "id": i} for i in df1.columns],
#    data=df1.to_dict("rows"),
#)



#dcc.Checklist(
#    options=[
#        {'label': 'New York City', 'value': 'NYC'},
#        {'label': 'Montréal', 'value': 'MTL'},
#        {'label': 'San Francisco', 'value': 'SF'}
#    ],
#    values=['MTL', 'SF']
#)



if __name__ == '__main__':
    app.run_server(debug=True)
