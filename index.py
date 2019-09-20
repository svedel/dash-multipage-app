import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from layouts import monitoring_page, index_page, error_page, annotate_page, colors
import callbacks

# define app title
app.title = "My test app"


# defines the page layout
app.layout = html.Div([
	# navbar
	# dashboard header
	html.Div(style={'backgroundColor': colors['header background'], 'vertical-align': 'middle'}, children=[
		html.Div([
			html.Img(
				src='/assets/sample_logo.png',
				#className = "three columns",
				style={
					'height': '3%',  # using percentages makes this a responsive app
					'width': '3%',
					'float': 'left',
					'position': 'relative',
					'margin-top': 5,  # unit of pixel
					'margin-right': 5,
					'margin-bottom': 5,
					'margin-left': 5
				},
			),
			html.H3(
				children='Simple Dash testing app',
				style={
					'textAlign': 'left'
				},
				className = "five columns"),
			# buttons for pages
			html.Div([			
				html.A(
					html.Button('Details',
					style = {
						'margin-right': 5, # unit of pixel
						'margin-left': 5,
					}),
					href='/'),
				html.A(
					html.Button('Monitoring', dir='ltr',
					style = {
						'background-color': colors['button'],
						'margin-right': 5, # unit of pixel
						'margin-left': 5,
					}),
					href='/monitoring'),
				html.A(
					html.Button('Annotate', dir='ltr',
					style = {
						'margin-right': 5, # unit of pixel
						'margin-left': 5,
					}),
					href='/annotate'),
				],
				className="four columns offset-by-two",
				style={'margin-top': 15}),
			##dbc.DropdownMenu(
            		##	children=[
                	##		dbc.DropdownMenuItem("More pages", header=True),
                	##		dbc.DropdownMenuItem("Page 2", href="#"),
                	##		dbc.DropdownMenuItem("Page 3", href="#"),
            		##	],
            		##	nav=True,
            		##	#in_navbar=True,
            		##	label="Pages",
			##	className = "one column",
        		##),
			#html.Div([dcc.Dropdown(
			#	id='page-selector',
			#	options = [{'value': 'monitoring', 'label': 'Monitoring page'}, {'value': '', 'label': 'Index page'}],
			#	placeholder='Pages',
			#	)
			#],
			#className="one column",
			#style = {
			#	'margin-top': 10,  # unit of pixel
			#	'margin-right': 5,
			#	'margin-bottom': 5,
			#	'margin-left': 5,
			#}
			#),
		]),
	], className = "row"),	


	# handles multi-page stuff
	dcc.Location(id='url', refresh = False),
	html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
	pathname_str = str(pathname)
	if pathname_str == '/':
		return index_page
	elif pathname_str == '/monitoring':
		return monitoring_page
	elif pathname_str.startswith('/annotate'):

		# handle case where input provided via url (single element): input provided as /annotate/country=X (where X is country of interest)
		if pathname_str.startswith('/annotate/'):
			tmp_str = pathname_str.split('/')[-1]
			start_country = tmp_str.split('=')[-1]
		else:
			start_country = 'no country'

		return annotate_page(start_country = start_country)
	else:
		return error_page

if __name__ == '__main__':
	app.run_server(host='0.0.0.0')#,debug=True, port=8050)
