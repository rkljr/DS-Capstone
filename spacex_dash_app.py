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

spacex_df["Count"] = 1
spacex_df["Outcome"] = 'Failure'
spacex_df.loc[spacex_df["class"] == 1, "Outcome"] = 'Success'
#spacex_df.to_csv('spacex_df.csv')

# Create a dash application
app = dash.Dash(__name__)

#get the data for the dropdown
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
                                dcc.RangeSlider(id='payload-slider',min = min_payload, max = max_payload, step = 1000, value = [min_payload, max_payload]),

                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart'))
                                ])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
@app.callback( Output(component_id='success-pie-chart', component_property='figure'),
               Input(component_id='site-dropdown', component_property='value'))

def get_pie(entered_site):
    if entered_site == 'ALL':
        pie_data =  spacex_df.loc[spacex_df['class'] == 1]
        fig = px.pie(pie_data, values='class', names='Launch Site', title = 'Launch Site Success Rate')
        return fig
    else:
        pie_data =  spacex_df.loc[spacex_df['Launch Site'] == entered_site]
        pie_data.to_csv('pie_data.csv')
        fig = px.pie(pie_data, values='Count', names='Outcome', title = 'Site Success/Failure')
        return fig

    # Group the data by Month and compute average over arrival delay time.
    #pie_data = df.groupby('Month')['ArrDelay'].mean().reset_index()
    
# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback( Output(component_id='success-payload-scatter-chart', component_property='figure'),
               Input(component_id='site-dropdown', component_property='value'),
               Input(component_id='payload-slider', component_property='value'))

def get_scatter(entered_site, entered_payload):
    if entered_site == 'ALL':
        plot_data =  spacex_df
        fig = px.scatter(plot_data, x ='Payload Mass (kg)', y ='class', title = 'Launch Site Success by Booster', color='Booster Version Category')
        return fig
    else:
        plot_data =  spacex_df.loc[spacex_df['Launch Site'] == entered_site]
        fig = px.scatter(plot_data, x ='Payload Mass (kg)', y ='class', title = 'Site Success Rate by Booster', color='Booster Version Category')
        return fig

# Run the app
if __name__ == '__main__':
    app.run_server()
