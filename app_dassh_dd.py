import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_table
import pandas as pd
import os


def load_file(file_name):
    ext = file_name.split(".")[-1]
    loaders = {
        "csv": lambda x: pd.read_csv(r"{}".format(x)),
        "xlsx": lambda x: pd.read_excel(r"{}".format(x)),
        "xls": lambda x: pd.read_excel(r"{}".format(x)),
    }
    return loaders[ext](file_name)


valid_fs = ('.csv', '.xlsx', '.xls')
arr = [f for f in os.listdir() if f.endswith(valid_fs)]
dfd = {}
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__,)# external_stylesheets=external_stylesheets)
app.layout = html.Div([
    dcc.Dropdown(id='demo-dropdown', options=[{'label': f, 'value': f} for f in arr], value=arr, multi=True),
    html.Div(id='dd-output-container'),
    html.Button('Submit', id='button'),
    html.Div(id='output-container-button', children=['Select a csv and press submit']),
    html.Div(id='submit-out-container', children=[])
])


@app.callback(
    dash.dependencies.Output('dd-output-container', 'children'),
    [dash.dependencies.Input('demo-dropdown', 'value')])
def update_output(value):
    return 'You have selected "{}"'.format(value)


@app.callback(
    dash.dependencies.Output('submit-out-container', 'children'),
    [dash.dependencies.Input('button', 'n_clicks')],
    [dash.dependencies.State('demo-dropdown', 'value')])
def update_output(n_clicks, value):
    if not n_clicks:
        return
    df = pd.DataFrame(load_file(value[0]))
    return dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        sort_action="native",
    )


if __name__ == '__main__':
    app.run_server(debug=True)
