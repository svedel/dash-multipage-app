# dependencies for all pages
import dash_html_components as html
import plotly.graph_objs as go
import datetime
import numpy as np
import json
from dash.dependencies import Input, Output

from app import app
from layouts import df

# handle live-updating of time (relying on dcc.Interval component)
@app.callback(Output('live-update-text', 'children'),
	[Input('interval-component', 'n_intervals')])
def update_timing(n):
	style = {'padding': '5px', 'fontSize': '16px'}
	return_text = [
		html.Span('Last update of app data:', style=style),
		html.Span(str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")), style=style)
	]
	return return_text

# handle updating of figure
@app.callback(
	Output('graph-with-dropdown', 'figure'),
	[Input('graph-country-dropdown', 'value')])
def update_graph(country):
	df_temp = df
	df_temp.loc[df_temp.country == country,'life expectancy'] += np.random.rand(1)*10
	figure={
		'data': [  # notice how this is build as nested lists via list comprehension --- the looping is noteworthy
			go.Scatter(
				x=df_temp[df_temp['continent']==i]['gdp per capita'],
				y=df_temp[df_temp['continent']==i]['life expectancy'],
				text=df_temp[df_temp['continent']==i]['country'],
				mode='markers',
				opacity=0.8,
				marker={
					'size': 15,
					'line': {'width': 0.5, 'color': 'white'}
				},
				name=i,
			) for i in df_temp.continent.unique()
		],
		'layout': go.Layout(
			xaxis={'type': 'log', 'title': 'GDP Per Capita'},
			yaxis={'title': {'text': 'Life Expectancy'}},
			margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
			legend={'x': 0, 'y': 1},
			hovermode='closest',
			paper_bgcolor='rgba(0,0,0,0)',
			plot_bgcolor='rgba(0,0,0,0.1)'
			)
	}
	return figure


# handle updating of figure
@app.callback(
	Output('graph-with-dropdown-repeat', 'figure'),
	[Input('graph-country-dropdown-repeat', 'value')])
def update_graph(country):
	df_temp = df
	df_temp.loc[df_temp.country == country,'life expectancy'] += np.random.rand(1)*10
	figure={
		'data': [  # notice how this is build as nested lists via list comprehension --- the looping is noteworthy
			go.Scatter(
				x=df_temp[df_temp['continent']==i]['gdp per capita'],
				y=df_temp[df_temp['continent']==i]['life expectancy'],
				text=df_temp[df_temp['continent']==i]['country'],
				mode='markers',
				opacity=0.8,
				marker={
					'size': 15,
					'line': {'width': 0.5, 'color': 'white'}
				},
				name=i,
			) for i in df_temp.continent.unique()
		],
		'layout': go.Layout(
			xaxis={'type': 'log', 'title': 'GDP Per Capita'},
			yaxis={'title': {'text': 'Life Expectancy'}},
			margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
			legend={'x': 0, 'y': 1},
			hovermode='closest',
			clickmode='event+select',
			paper_bgcolor='rgba(0,0,0,0)',
			plot_bgcolor='rgba(0,0,0,0.1)'
			)
	}
	return figure

# handle callback from clicking graph
@app.callback(
	Output(component_id='selected-datapoint',component_property='children'),
	[Input(component_id='graph-with-dropdown-repeat',component_property='clickData')])
def display_click_data(clickData):
	
	#tmp = json.dumps(clickData, indent=2)
	tmp = clickData
	
	#return json.dumps(clickData, indent=2)
	return tmp['points'][0]['x']

# handle text-box interactivity (callback)
@app.callback(
	Output(component_id='my-div', component_property='children'),
	[Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
	return 'You\'ve entered "{}"'.format(input_value)

# handle navigation bar callbacks (handle by updating Location)
@app.callback(
	Output('url','pathname'),
	[Input('page-selector', 'value')])
def page_nav(dropdown_value):
	return dropdown_value
