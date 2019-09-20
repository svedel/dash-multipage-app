# create a multi-page app based on a flat file structure
# all pages, callbacks etc are placed across app pages
# /assets/ contain all assets 

import dash
import dash_bootstrap_components as dbc

external_stylesheets=[dbc.themes.BOOTSTRAP]

# initialize app and pick up bootstrap css from assets/bootstrap.css
#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app = dash.Dash(__name__)
server = app.server  # grab the underlying flask server for later usage
app.config.suppress_callback_exceptions = True  # required for callbacks across multi-page apps (dash checks need for all listed callbacks; if one is not used it'll throw an error)
