# chatgpt: create a dash app that contains a plotly scatter plot
# using the pickled file plotly_data.pkl. the x-axis should be
# column 0, the y axis column 1 and the hover data competitorname

import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import pickle

# Load data from the pickled file
with open('plotly_data.pkl', 'rb') as file:
    data = pickle.load(file)

# Dash app
app = dash.Dash(__name__)

# Layout of the app
app.layout = html.Div([
    dcc.Graph(
        id='scatter-plot',
        figure=px.scatter(
            data,
            x=0,
            y=1,
            title='Interactive Scatter Plot',
            labels={'0': 'X-axis', '1': 'Y-axis'},
            hover_data=['competitorname']
        )
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
