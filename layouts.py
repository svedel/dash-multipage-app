# layouts of all pages
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

# some simple coloring
colors = {
	'header background': '#d3d3d3',
	'button': '1245A8'
}

styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}

# read data to be plotted
df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/' +
	'5d1ea79569ed194d432e56108a04d188/raw/' +
	'a9f9e8076b837d541398e999dcbac2b2826a81f8/'+
	'gdp-life-exp-2007.csv')

# create the frontend stuff
monitoring_page = html.Div([
	# part ofpage header, not in app navbar
	html.Div(children='Testing dash for a overview dashboard', style={'textAlign': 'left'},
			className = "twelve columns"),
		# an interactive text: creates a textbox and then display the supplied text back interactively
	dcc.Input(id='my-id', value='Dash App', type='text'),  # the dcc.Input is different from the Input (and Output) importerted from dash.dependencies
	html.Div(id='my-div'),

		#the graphics component: two graphs, one with a drop-down component
	html.Div([
		html.Div([
			# the first graph
			html.Div([
				html.Div(children='Dumb title 2', style={'textAlign': 'center'}),
				dcc.Graph(id='graph1',
					figure={
						'data': [
							{'x':[1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
							{'x':[1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
						],
						'layout': go.Layout(
							xaxis = {'title': {'text': 'something'}},
							paper_bgcolor='rgba(0,0,0,0)',
							plot_bgcolor='rgba(0,0,0,0.1)'
						)
							#{
							#'xaxis': {
							#	'title': 'something'
							#	}
						#}
					}), 
			], className = "five columns"),
				# the second graph (interactive, linked with dropdown)
			html.Div([
				html.Div(children='Dumb title 3', style={'textAlign': 'center'}),					
				dcc.Graph(id='graph-with-dropdown')
			],className = "five columns"),  
				# dropdown to select options for second graph
			dcc.Dropdown(  # takes options for dropdown as list of dicts, here created via list comprehension
				id='graph-country-dropdown',
				options = [
					{'label': i, 'value': i} for i in df.country.unique()
				],
				value = df.country.iloc[0],
				className = "two columns"
			),
		]),
	], className = "row"),
		# a simple footer
	html.Div(id='live-update-text', className = "twelve columns", style={'backgroundColor': colors['header background']}),
		# internal tool keeping track of time since app launch. Updates 'n_intervals' by +1 each time 'interval' passes (measured in ms)
	dcc.Interval(
		id='interval-component',
		interval=10*1000,  # update every 10 second
		n_intervals=0  # counter starting value
	)
])

index_page = html.Div([
	html.Div([
		dcc.Markdown('''
		# Markdown header
		We will fill out this text with some details.

		## Some math
		$$\int f(x) dx$$
		''')
		
	],
	className = "ten columns offset-by-one", 
	style={
		'backgroundColor': 'rgba(0,0,0,0.1)',
		'margin-top': 15
	}
	)],
	style={
		'height': '90vh'
	}
)

error_page = html.Div([
	html.Div([
		dcc.Markdown('''
			# 404
			## Something's not right...
			''')
		],
		className = "ten columns offset-by-one",
		style={
		'backgroundColor': 'rgba(0,0,0,0.1)',
		'margin-top': 20
		}
	)],
	style = {
		'height': '90vh'
	}
)

def annotate_page(start_country):
	
	# determine whether provided input is valid
	if start_country in list(df.country.unique()):
		start_value = start_country
	else:
		start_value = df.country.iloc[0]

	page = html.Div([
		html.Div([
			html.H3(children='Annotate data', style={'textAlign': 'left'},
				className = "ten columns"),
			html.Div([
				html.Div(children='Select a dot on the graph', style={'textAlign': 'center'}),					
				dcc.Graph(id='graph-with-dropdown-repeat')
			],className = "five columns"),  

			html.Div([
			
			# dropdown to select options for second graph
				dcc.Dropdown(  # takes options for dropdown as list of dicts, here created via list comprehension
					id='graph-country-dropdown-repeat',
					options = [
						{'label': i, 'value': i} for i in df.country.unique()
					],
					value = start_value,
					#className = "two columns"
				),

				html.Br(),

			# return readout from selection here
				html.Div([
					html.Div('Selected data (GDP per capita):'),#, className = "two columns"),
					html.Pre(id='selected-datapoint', style=styles['pre']),# className="two columns"),
					dcc.Input(placeholder='Enter name for column...', type='text', value=''),# className="two columns")
					],
					className="row"),
				],
				className = "five columns"),

			],
			className = "ten columns offset-by-one",
			style={
				'backgroundColor': 'rgba(0,0,0,0.1)',
				'margin-top': 20
				}
		)],
		#style = {
		#	'height': '90vh'
		#}
	)
	return page
