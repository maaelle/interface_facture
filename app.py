import base64
import os
from flask import Flask, send_from_directory
from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc

# App Instance
app = dash.Dash(name="name")
app.title = "name"
########################## Navbar ##########################
# Input
# Output
navbar = dbc.Nav()
# Callbacks
@app.callback()
def function():
    return 0
########################## Body ##########################
# Input
inputs = dbc.FormGroup()
# Output
body = dbc.Row([
        ## input
        dbc.Col(md=3),
        ## output
        dbc.Col(md=9)
])
# Callbacks
@app.callback()
def function():
    return 0
########################## App Layout ##########################
app.layout = dbc.Container(fluid=True, children=[
    html.H1("name", id="nav-pills"),
    navbar,
    html.Br(),html.Br(),html.Br(),
    body
])
########################## Run ##########################
if __name__ == "__main__":
    app.run_server(debug=True)