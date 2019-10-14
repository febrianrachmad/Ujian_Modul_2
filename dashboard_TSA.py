import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
from sqlalchemy import create_engine

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

engine = create_engine("mysql+mysqlconnector://root:P@ssw0rd@localhost/ujian2?host=localhost?port=3306")
conn = engine.connect()

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
dfTSA = pd.read_csv('tsa_claims_dashboard_ujian.csv')


app.layout = html.Div(children = [
        html.H1('Ujian Modul 2 Dashboard TSA'),
        html.P('Created By: Febrian Rachmad'),
        dcc.Tabs(value = 'tabs', id = 'tabs-1', children = [
            dcc.Tab(label = 'DataFrame-Table', value = 'tab-nol', children = [
            html.H1('DATAFRAME TSA', style = {'text-align' : 'center'}),
            # Insert Your Code Here
            ]),

            dcc.Tab(label = 'Bar-Chart', value = 'tab-satu', children = [
            # Insert Your Code Here
            ]),
                
            dcc.Tab(label = 'Scatter-Chart', value = 'tab-dua', children = [
            # Insert Your Code Here
            ]),

            dcc.Tab(label = 'Pie-Chart', value = 'tab-tiga', children = [
            # Insert Your Code Here
            ])
            ],
            content_style = {
            'fontFamily' : 'Arial',
            'borderBottom' : '1px solid #d6d6d6',
            'borderLeft' : '1px solid #d6d6d6',
            'borderRight' : '1px solid #d6d6d6',
            'padding' : '44px'
            })
        ],
        style = {
        'maxWidth' : '1800px',
        'margin' : '0 auto'
    })


if __name__ == '__main__':
    app.run_server(debug=True)