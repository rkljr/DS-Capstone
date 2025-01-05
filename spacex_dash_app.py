# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)
items = [{'label': 'All Sites', 'value': 'ALL'}, {'label': 'site1', 'value': 'site1'}]
items = [{'label': 'All Sites', 'value': 'ALL'}]
launch_sites = spacex_df["Launch Site"].unique()
for site in launch_sites:
    items.append({'label': site, 'value': site})
# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                
                                dcc.Dropdown(id='site-dropdown',  options=items, value='ALL', searchable=True, placeholder='Select a Launch Site'),
                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                #dcc.RangeSlider(id='payload-slider',...)

                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
# add callback decorator
@app.callback( Output(component_id='success-pie-chart', component_property='figure'),
               Input(component_id='site-dropdown', component_property='value'))

# Add computation to callback function and return graph
def get_graph(entered_site):
    if entered_site == 'ALL':
        pie_data =  spacex_df
    else:
        pie_data =  spacex_df[spacex_df['Launch Site']== entered_site]

    # Group the data by Month and compute average over arrival delay time.
    #pie_data = df.groupby('Month')['ArrDelay'].mean().reset_index()
    fig = px.pie(pie_data, values='class', names={'Success', 'Failure"'},
    title = 'Site Success/Failure')
    return fig
# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output


# Run the app
if __name__ == '__main__':
    app.run_server()
