import dash
import dash_html_components as html
import dash_table
import pandas as pd
import webbrowser
from tkinter import *
from tkinter import filedialog


def load_file(file_name):
    ext = file_name.split(".")[-1]
    loaders = {
        "csv": lambda x: pd.read_csv(r"{}".format(x)),
        "xlsx": lambda x: pd.read_excel(r"{}".format(x)),
    }
    return loaders[ext](file_name)


def prompt_for_file():
    root = Tk()
    f = filedialog.askopenfilename(
        filetypes=[
            ("csv Files", "*.csv"),
            ("xlsx Files", "*.xlsx"),
        ]
    )
    root.destroy()
    return f


app = dash.Dash(__name__, )
app.layout = html.Div([
    html.Button('Click to Select a csv or xlsx file', id='button'),
    html.Div(id='output-container-button', children=[]),
    html.Div(id='submit-out-container', children=[])
])


@app.callback(
    dash.dependencies.Output('submit-out-container', 'children'),
    [dash.dependencies.Input('button', 'n_clicks')])
def update_output(n_clicks):
    if not n_clicks:
        return
    df = pd.DataFrame(load_file(prompt_for_file()))
    return dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        sort_action="native",
    )


if __name__ == '__main__':
    webbrowser.open_new_tab("http://127.0.0.1:8050/")
    app.run_server(debug=True)
