"""TODO:
    Replace your DF with my test df and let me know if it works
"""

import datetime as dt
import random

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd


def graph_it(df, figure_id, series_column, y_column, height=None, width=None):
    unq = df[series_column].unique()
    x_df_l = [df[df[series_column] == x] for x in unq]
    data_l = []
    for i, d in enumerate(x_df_l):
        data_l.append(
            dict(
                x=d[y_column].keys(),
                y=d[y_column].values,
                name=f'{unq[i]} {y_column}',
                marker=dict(color=f'rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})')
            )
        )
    return dcc.Graph(
        figure=dict(
            data=data_l,
            layout=dict(
                title=f'{unq} price over time',
                margin=dict(l=40, r=0, t=40, b=30)
            )
        ),
        style={
            'height': height,
            'width': width
        },
        id=figure_id
    )


if __name__ == '__main__':
    # Test DF Replace with your own df
    DATA_FRAME = pd.DataFrame(
        {
            'date': [
                dt.datetime.strptime(
                    date,
                    "%m/%d/%Y"
                ).date() for date in [
                    "10/24/2019", "10/24/2019", "10/25/2019", "10/25/2019",
                    "10/26/2019", "10/26/2019", "10/27/2019", "10/27/2019",
                ]
            ],
            'name': ["a", "b", "a", "b", "a", "b", "a", "b"],
            'brand': ["a", "b", "a", "b", "a", "b", "a", "b"],
            'retailer': ["ra", "ra", "ra", "ra", "ra", "ra", "ra", "ra"],
            'price': [8.99, 6.99, 8.59, 6.50, 9.50, 2.30, 9.50, 0.5],
            'stars': [4.5, 4.3, 4.4, 4.0, 4.9, 2.2, 4.8, 1.8],
            'category': ["ca", "ca", "ca", "ca", "ca", "ca", "ca", "ca"],
            'highlights': ["_", "_", "_", "_", "_", "_", "_", "_"]
        }
    ).set_index('date')
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css', ]
    app = dash.Dash(__name__, external_stylesheets=external_stylesheets, )
    app.layout = html.Div(
        children=[
            html.H1(children='Dashboard Title'),
            html.Div(children="Dashboard description text."),
            html.Div(children=graph_it(df=DATA_FRAME, figure_id='my-graph', series_column="brand", y_column="price")),
        ],
    )
    app.run_server(debug=True)
