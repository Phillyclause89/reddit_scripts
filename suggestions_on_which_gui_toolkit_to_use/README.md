# r/learnpython Adventure Summary
  TEXT

## File Overview:
  File | SIZE | BRIEF
--- | --- | ---
README.md | ![GitHub file size in bytes](https://img.shields.io/github/size/Phillyclause89/reddit_scripts/suggestions_on_which_gui_toolkit_to_use/README.md?style=plastic) | README.md file for this adventure.
requirements.txt | ![GitHub file size in bytes](https://img.shields.io/github/size/Phillyclause89/reddit_scripts/suggestions_on_which_gui_toolkit_to_use/requirements.txt?style=plastic) | requirements.txt for this adventure.
app_dassh_dd.py | ![GitHub file size in bytes](https://img.shields.io/github/size/Phillyclause89/reddit_scripts/suggestions_on_which_gui_toolkit_to_use/app_dassh_dd.py?style=plastic) | A pure dash approach to loading a file
app_tky.py | ![GitHub file size in bytes](https://img.shields.io/github/size/Phillyclause89/reddit_scripts/suggestions_on_which_gui_toolkit_to_use/app_tky.py?style=plastic) | A pure tkinter approach to loading a file by u/baubleglue
frankensteinish_app.py | ![GitHub file size in bytes](https://img.shields.io/github/size/Phillyclause89/reddit_scripts/suggestions_on_which_gui_toolkit_to_use/frankensteinish_app.py?style=plastic) | A hybrid tkinter dash app to load a file
music_playlist.csv | ![GitHub file size in bytes](https://img.shields.io/github/size/Phillyclause89/reddit_scripts/suggestions_on_which_gui_toolkit_to_use/music_playlist.csv?style=plastic) | csv for testing scripts

## Source Link:
  * [ r/learnpython/.../suggestions_on_which_gui_toolkit_to_use ]( https://www.reddit.com/r/learnpython/comments/e5qw6m/suggestions_on_which_gui_toolkit_to_use/ )
  
## Post Title:
  > suggestions on which GUI toolkit to use?
  
## Post Body:
  > It's been while since I've used Python. Not much GUI experience, I believe I played around with tkinter a bit though I can't say for sure if that was what I used since it's been so long. I'd like to create a desktop app to do the following.
  > 
  > 1) User gives the program an existing spreadsheet
  > 
  > 2) Spreadsheet is then analyzed for occurrences of various problematic scenarios
  > 
  > and then ideally:
  > 
  > 3) User is given a list of these problematic scenarios found, along with the proposed way to correct them
  > 
  > 4) User chooses which ones they want to fix
  > 
  > 5) The changes are saved to a new spreadsheet - user can either enter the name or the program can generate the new name, this isn't important
  > 
  > Thank you.

### My Comment(s):
  > Lol I’m building almost exactly this right now. Also this is like the second question about what GUI lib to use posted to this sub in like 2 hours, so I’m going to paraphrase what i said in that thread. Look into using a web app GUI framework using dash or flask. IMO it’s the way of the future for python GUIs.
#### u/baubleglue's Response (Not OP):
  > Then you will need to learn JavaScript because any Web GUI generated on server side is garbage. For small user prompt Tk will be just fine.
#### My Reply:
  > [Dash applications are web servers running Flask and communicating JSON packets over HTTP requests. Dash’s frontend renders components using React.js, the Javascript user-interface library written and maintained by Facebook.](https://link.medium.com/zUT6rWOl81)
#### Their Reply:
  > That is exactly my point, whole UI part is a wrapper around heavy React.js application, except plots of cause.
#### My Reply:
  > But how does that make it garbage? Because it is a wrapper for a thing and not actually the thing?
  > 
  > I’m mean at the end of the day a lot of python is just a wrapper around some other code. Is all that python garbage too? tkinter is just [wrapper around a complete Tcl interpreter embedded in the Python interpreter.](https://en.wikipedia.org/wiki/Tkinter?wprov=sfti1)  Does that make it garbage too?
#### Their Reply:
  > UI generated on the client - it isn't Python (server) code.
#### My Reply:
  > I feel like you’re a smart person who probably knows a bit about these things but you are putting no effort into supporting your opinion here. Have you tried building the exact same program using both frameworks and measured their performance diffs or something? At least link me to a white paper or something that supports your argument here.
#### Their Reply:
  > I am not a UI developer, but I've built few apps. There are few problems with keeping UI logic on server
  > 
  > server has no direct interaction with user. All user's events occurred on client. Simple action like button click need to be wrapped in JavaScript Ajax call if you don't want to refresh page. Action like collapse tree will require reloading at list a part of the page.
  > 
  > Server doesn't know exact state of the application. You need to maintain a model of app state without ability directly to validate it (you send popup alert to user, on next UI event is it closed or need to send another alert)
  > 
  > It's slow to transfer user events, order of events may be not consistent. You click "stop execution" and wait for 1/3 sec
#### My Reply:
  > Thank you for taking the time to elaborate on your argument. I believe all these points are potentially valid and I’ll keep them in mind as I build this tool. That being said I have not noticed these issues during testing. If they are present then they are currently too minimal for me to worry about.
#### Their Reply:
  > Actually I cut my arguments in the middle because my subway arrived to the stop. In general it is easy to build UI with HTML (directly or by using python/javascript/... templates) but it isn't easy to write web application. As an example simple app with described in the OP question will require: start/stop server; upload XLS files functionality; output results...
  > 
  > Wrappers around something is a problem (potential) for few reasons:
  > 
  > It creates dependencies. Ex. you want to upgrade React.js (new features/bug fixes/some cool plugin which you need), but python wrapper still is not supporting it.
  > 
  > Wrapper exposes only part of the library - you limited to a set of features (that actually is a purpose to have wrapper)
  > 
  > In general if you look in github JS UI frameworks are booming (big companies finance them) and Python UI frameworks are rarely updated. Currently I am using few applications with Python's UI Apache Airflow, Apache Superset - the UI looks OK, but acts like few decades old (and buggy).
  > 
  > Current trend is to let server pass data to JS app running in browser and JS Client asks server for data and/or requests to do something with data. It makes server and UI simpler.
#### My Reply:
  > I do agree that the most optimal framework for a web app would be all JS, HTML and CSS, but so far in my experiments with dash, I’ve been able to everything I need in what feels like less lines of code than it would take me using tkinter, but that is just a feeling, I haven’t actually used tkinter in like over a year. The last python GUI I used was Kivy a few months ago.
#### Their Reply:
  > Of cause code for desktop application is bigger. But lets go back to the original topic, don't you think that webserver, file upload form... is a bit overkill for GUI which only need to select file/s? Even the number of code lines will be smaller.
  > ```python
  > from tkinter import Tk, Menu
  > from tkinter import ttk
  > from tkinter.filedialog import askopenfilename
  > 
  > def OpenFile():
  >     name = askopenfilename(
  >         initialdir="C:/temp/",
  >         filetypes=(("Excel File", "*.xlsx"), ("All Files", "*.*")),
  >         title="Choose a file.")
  >     try: 
  >         # code for Spreadsheet analyzer ...   
  >         with open(name, 'r') as UseFile:
  >             print(UseFile.read())
  >     except Exception as e:
  >         print("No file exists", e)
  > def app():
  >     root = Tk()
  >     root.title("Spreadsheet Analyzer")
  >     label = ttk.Label(
  >             root,
  >             text="Result will be here",
  >             foreground="black",
  >             font=("Helvetica", 11))
  >     label.pack(padx=100, pady=100)
  >     menu = Menu(root)
  >     root.config(menu=menu)
  >     file = Menu(menu)
  >     file.add_command(label='Open', command=OpenFile)
  >     file.add_command(label='Exit', command=lambda: exit())
  >     menu.add_cascade(label='File', menu=file)
  >     root.mainloop()
  > if __name__ == "__main__":
  >     app()
  > ```
#### My Reply:
  > This was the last tkinter app i made:  [https://github.com/Phillyclause89/Skittles-AI/blob/master/data\_editor.py](https://github.com/Phillyclause89/Skittles-AI/blob/master/data_editor.py)
  > the dash code for uploading a csv is here:  [https://dash.plot.ly/dash-core-components/upload](https://dash.plot.ly/dash-core-components/upload)
  > if you don't care about it being on a server and want to run the app locally you can do something like this to load and view the csv.
  > ```python
  > import dash
  > import dash_html_components as html
  > import dash_core_components as dcc
  > import dash_table
  > import pandas as pd
  > import os
  >  
  >  
  > def load_file(file_name):
  >     ext = file_name.split(".")[-1]
  >     loaders = {
  >         "csv": lambda x: pd.read_csv(r"{}".format(x)),
  >         "xlsx": lambda x: pd.read_excel(r"{}".format(x)),
  >     }
  >     return loaders[ext](file_name)
  >  
  >  
  > valid_fs = ('.csv', '.xlsx', '.xls')
  > arr = [f for f in os.listdir() if f.endswith(valid_fs)]
  > dfd = {}
  > external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
  > app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
  > app.layout = html.Div([
  >     dcc.Dropdown(id='demo-dropdown', options=[{'label': f, 'value': f} for f in arr], value=arr, multi=True),
  >     html.Div(id='dd-output-container'),
  >     html.Button('Submit', id='button'),
  >     html.Div(id='output-container-button', children=['Select a csv and press submit']),
  >     html.Div(id='submit-out-container', children=[])
  > ])
  >  
  >  
  > @app.callback(
  >     dash.dependencies.Output('dd-output-container', 'children'),
  >     [dash.dependencies.Input('demo-dropdown', 'value')])
  > def update_output(value):
  >     return 'You have selected "{}"'.format(value)
  >  
  >  
  > @app.callback(
  >     dash.dependencies.Output('submit-out-container', 'children'),
  >     [dash.dependencies.Input('button', 'n_clicks')],
  >     [dash.dependencies.State('demo-dropdown', 'value')])
  > def update_output(n_clicks, value):
  >     if not n_clicks:
  >         return
  >     df = pd.DataFrame(load_file(value[0]))
  >     return dash_table.DataTable(
  >         id='table',
  >         columns=[{"name": i, "id": i} for i in df.columns],
  >         data=df.to_dict('records'),
  >         sort_action="native",
  >     )
  >  
  >  
  > if __name__ == '__main__':
  >     app.run_server(debug=True)
  > ```
  > Also here is a different [dash app](https://github.com/Phillyclause89/PandaDasher/blob/master/demo_app/graph_it_app.py)  that i made the other night since I can't really show you the one I'm making at work. So far [heroku](https://graph-it-demo-app.herokuapp.com/) does a fine job running it on their lowest tier server.
  > 
#### Their Reply:
  > It is really cool, the problem is that you can't easily share it with other people. In order to run your example I need to install dash (20M it can be more, but I have some of the packages installed). Then you need to start the server. User also need to be connected to internet (loading CSS) - it isn't the use case described in the question.
  > P.S There is a bug in parse_contents
  > You continue with the code if selected file isn't CSV/Excel.
  > 
  > You also can add filter (accept) for the select file dialog
  >
  > # <input type="file" accept=".jpg, .png, .jpeg, .gif, .bmp, .tif, .tiff|image/*">
  > ```python
  > app.layout = html.Div([
  >     dcc.Upload(
  >         ....,
  >         multiple=True,
  >         accept=".csv, .xls, .xlsx"), 
  >     html.Div(id='output-data-upload'),
  > ])
  > ```
#### My Reply:
  > > the problem is that you can't easily share it with other people. In order to run your example I need to install dash (20M it can be more, but I have some of the packages installed). Then you need to start the server. User also need to be connected to internet (loading CSS) - it isn't the use case described in the question.
  > The difficulty of sharing a dash app is dependent on the distribution method:
  > An externally hosted dash app does come with the user requirement that they be connected to the external host server (whether that be on the internet or a private network) and has additional hurdles for the developer during the deployment stage, but IMO it is the optimal UX for the end user as they just need a somewhat modern internet browser to use the app.
  > A locally running dash app transfers some of the set-up hurdles from the dev to the user, but setup flow can be automated by for example on windows using a .bat file that runs all the pip freeze > requirements.txt stuff. Setup time for them should only push 20min if their internet is really slow. I've tested the fresh set up flow on a venv for my other project which requires Dash, Pandas, Numpy and a few other libs and it only takes like 5 minutes max to get up and running (my home comcast service is about 300 Mbps down). Once all the requirements are installed, the user no longer requires the internet to run the script (even if you accidently leave stylesheet paths hard coded to the example URL, the app will still function without the css. it just won't be as stylish.) since the app will be accessible from a local http://127.0.0.1:8050/ URL. Launching this Dash based desktop app can be further automated using another .bat file that runs the cmd command to run the python script.
  > As for OPs use case:
  > > I'd like to create a desktop app to do the following.
  > > 1) User gives the program an existing spreadsheet
  > > 2) Spreadsheet is then analyzed for occurrences of various problematic scenarios
  > >
  > > and then ideally:
  > > 3) User is given a list of these problematic scenarios found, along with the proposed way to correct them
  > > 4) User chooses which ones they want to fix
  > > 5) The changes are saved to a new spreadsheet - user can either enter the name or the program can generate the new name, this isn't important
  >
  > All of those functional requirements can be achieved using either a traditional Python GUI framework like tkinter or using a webapp GUI framework like Dash. My example only demonstrated requirement 1, because your example only demonstrated requirement 1. I personally like my example better because the spreadsheet data is more neatly presented in the bowser UI as opposed to how your example just prints it to the console. to present that data neatly in the tkinter app window, you would need a fair bit more code and would likely end up using additional libs like how I used pandas in my example.
  > 
  > One final thought, one could also go down the route of making a mutant tkinter and dash hybrid app if they are feeling frankensteinish.
  > ```python
  > import dash
  > import dash_html_components as html
  > import dash_table
  > import pandas as pd
  > import webbrowser
  > from tkinter import *
  > from tkinter import filedialog
  > 
  > 
  > def load_file(file_name):
  >     ext = file_name.split(".")[-1]
  >     loaders = {
  >         "csv": lambda x: pd.read_csv(r"{}".format(x)),
  >         "xlsx": lambda x: pd.read_excel(r"{}".format(x)),
  >     }
  >     return loaders[ext](file_name)
  > 
  > 
  > def prompt_for_file():
  >     root = Tk()
  >     f = filedialog.askopenfilename(
  >         filetypes=[
  >             ("csv Files", "*.csv"),
  >             ("xlsx Files", "*.xlsx"),
  >         ]
  >     )
  >     root.destroy()
  >     return f
  > 
  > 
  > app = dash.Dash(__name__, )
  > app.layout = html.Div([
  >     html.Button('Click to Select a csv or xlsx file', id='button'),
  >     html.Div(id='output-container-button', children=[]),
  >     html.Div(id='submit-out-container', children=[])
  > ])
  > 
  > 
  > @app.callback(
  >     dash.dependencies.Output('submit-out-container', 'children'),
  >     [dash.dependencies.Input('button', 'n_clicks')])
  > def update_output(n_clicks):
  >     if not n_clicks:
  >         return
  >     df = pd.DataFrame(load_file(prompt_for_file()))
  >     return dash_table.DataTable(
  >         id='table',
  >         columns=[{"name": i, "id": i} for i in df.columns],
  >         data=df.to_dict('records'),
  >         sort_action="native",
  >     )
  > 
  > 
  > if __name__ == '__main__':
  >     webbrowser.open_new_tab("http://127.0.0.1:8050/")
  >     app.run_server(debug=True)
  > ```