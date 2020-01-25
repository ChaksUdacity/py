
# -*- coding: utf-8 -*-
# Import required libraries 
import base64
import pandas
import dash
import dash_auth
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

import pandas as pd

from dash.dependencies import Input, Output, State
from datetime import datetime as dt

app = dash.Dash(__name__)
app.css.config.serve_locally = False
app.scripts.config.serve_locally = False
server = app.server

dash_auth.BasicAuth (app, {'hello': 'Arcis'})

df = pandas.read_csv("DF_DeC5_RX2andLab_Data.csv", parse_dates = ['Date'], infer_datetime_format = True, low_memory = False)
df = df.sort_values(by='Date', ascending=True)



plotTypes = ["Scatter Plot", "Line Plot","Filled Area Plot"]
df1 = df[["Date", 'RPG', 'Recycle', 'RPGtoRecycle%']]

dfLab= df[["Date",'C5 wt%_x', 'Benzene wt%_x', 'Bromine Number g/100g_x', 'C4 wt%_x',
 'Styrene wt%_x', 'Toluene wt%_x', 'Xylenes wt%_x' ,'Indene\nwt%',
 'C6~C9 NA wt%_x', 'C10+ NA wt%_x' ,'C9 Aro wt%_x', 'C10 Aro wt%_x',
 'DV g/100g_y' ,'EB wt%_x', '2-Methylindene wt%']]
features = dfLab.columns

df2 = df[["Date", 'H2_Nm3', 'H2toRPG', 'H2toRecycle', 'H2toHC']]
df3 = df[["Date",'I/LFlow_Rx1', 'I/LTemp_Rx1']]
df4 = df[["Date", 'Duty', 'LMTD', 'UA']]

df5 = df[["Date",'DeC5_I/L_Temp', 'DeC5_l/L_Flow', 'DeC5_O/H_Temp.', 'DeC5_O/H_Press','DeC5_O/H_Flow', 'C5_BTM_Flow', 'DeC5_BTM_Flow' ,'DeC5_BTM_Temp']]
df6 = df[["Date", 'C5 wt%_x', 'Benzene wt%_x']]

df7 = df[["Date",'C5 wt%_y', 'Benzene wt%_y', 'Bromine Number g/100g_y', 'C4 wt%_y', 'Styrene wt%_y', 'Toluene wt%_y', 'Xylenes wt%_y',
 'C6~C9 NA wt%_y', 'C10+ NA wt%_y', 'C9 Aro wt%_y', 'C10 Aro wt%_y', 'DV g/100g', 'EB wt%_y'   ]]

df8 = df[["Date", 'Rx2_RPG_temp', 'Rx2_H2_temp', 'Rx2_H2_Flow', 'Rx2_Feed_Temp', 'Rx2_1st_bed_△P', 'Rx2_2_3_bed_△P', 'RX2_1st_bed_O/L_T', 
'RX2_1st_bed_I/L_T', 'Rx2_1st_bed_△T', 'Rx2_2nd_O/L_T', 'Rx2_2nd_I/L_T','Rx2_2nd_bed_△T'  ]]

print(df.columns.values)
#quit()

df_graph = pd.read_csv("df_graph.csv")

with open('PyGas.svg','r', encoding='utf-8') as s:
	svg1 = s.read().replace('#', '%23')
svg = f'data:image/svg+xml;unicode,{svg1}'


image_filename = 'Profitability.png' # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

with open('PyGas_Troubleshoot.svg','r', encoding='utf-8') as s:
	svg2 = s.read().replace('#', '%23')
PyGas_Troubleshoot = f'data:image/svg+xml;unicode,{svg2}'

image_filename_2 = 'Business_Case.png' # replace with your own image
encoded_image_2 = base64.b64encode(open(image_filename_2, 'rb').read())

image_filename_3 = 'Predictive.png' # replace with your own image
encoded_image_3 = base64.b64encode(open(image_filename_3, 'rb').read())

now     = dt.now()
year    = dt.today().year
month   = dt.today().month
day     = dt.today().day
labels1 = df['G_B']

values1 = df['RPG']
colors  = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen','Salmon', 'SkyBlue']

app.layout = html.Div([
	html.Div([ #SGK091719 - Page title container
		html.Div([ #SGK091719 - Page title container
			html.P ('Digital Oil & Gas - Data to Decisons : Pyrolysis Gasoline Hydrogenation Unit')
			], className='page_title' )
		], className='page_title_container' ),
	dcc.Tabs (id = "tabs", children = [



		dcc.Tab (label = 'Business Case', children = [
			html.Div([ #SGK092319 Business Case
				html.H1("Digital Petrochemials", className='writeup_title'),
				html.Div([
					html.P("""Improve Petrochemicals business profitability utilising a wide range of Digital
						tools and technologies ranging from Data Analytics, Artificial Intelligence,
						Visualisation, Industrial Internet of Things(IIOT), Real time Monitoring,
						Cloud computing and a host of  other Digital technologies"""),
					html.Br([]),
					html.Strong("Process Unit: Pyrolysis Gasoline Hydrogenation"),

					html.Br([]),
					html.Strong("Business Case"),
					html.P("""Assess the reasons for coke deposition in the 2nd stage reactor inlet line of the PyGas Hydrogenation Unit"""),
					html.Br([]),
					html.Strong("Brief:"),
					html.P("""Pyolysis Gasoline (feed stock) are cracked Gasoline that contains high amount of Poly Unsaturated compounds (Diolefins and Alkenyl-Aromatics) suitable for Aromatics production.
						 However  Dienes saturation and Sulphur removal are needed before the feed stock become suitable either for Aromatics Production (BTX) or for Gasoline blending """),
					html.P("""PyGas Hydrogenation Unit (PHU) is a two stage reactor unit with the 1st stage reactor is predominantly for Dienes Saturation (Poly Unsaturated compounds) in order to improve Gasoline stability.
						 The 1st stage reactor is typically loaded with CO-MO Catalysts aiding hydrogenation reaction."""),
					html.P(""" The top bed of 2nd stage reactor is designed for Hydrogenation of Olefins loaded with Ni-MO catalyst resulting in lowering of Bromine numbers. The lower beds are loaded 
						 CO-MO catalyst ensuring hydrodesulphurisation of Cracked gasoline feed stock """),
					html.P(""" The first stage outlet which passes through a depentaniser to remove C5- components and the resultant depentanised gasoline is passed through the vaporiser to ensure the feed enters the 2nd stage reactor is above the dew point. This helps in avoiding coke formation """),
					html.Br([]),

					html.Strong(["Source of Coking:"], className="subtitle"),
					html.P("Coke deposition results from a variety of reasons right from the"),
					html.Ol([
						html.Li("Quality of Feedstock and their associated properties. Pygas is derived from steam cracking of various hydrocarbon feedstocks in olefin plants. Any upstream problem could affect downstream unit"),
						html.Li("Process Thruput : Fressh Feed versus Recycle. Higher Fresh feed needing higher hydrogen consumption. Non availability of adequate Hydrogen could limit fresh feed. Reaction is exothermic"),
						html.Li("Hydrogen Availability : Inadequate Hydrogen availability leading to catalyst deactivation and resultant coke formation"),
						html.Li("Process Parameters: Non Optimised Pressure,Tempearture and Feed rates resulting in increased Delta P in the reactor and coking in the pipelines,"),
						html.Li("Feed from Tanks: In adequate tank blanketting with Nitrogen leading to gum formation in feed stock"),
						html.Li("Dienes: Unsaturation of Dienes laeding to Polymerisation and Coke formation"),

						html.Li("Catalyst activity : Deactivation of catalyst leading to incomplete saturation of Dienes"),
						html.Li("Suitability of Chemical Injection and their dosage rates")
						]),

					html.Br([]),
					html.Strong("Setting:"),
					html.P("""Petrochemicals process are operated over varied temperature, pressure, flow rate on Catalyst surface
						over a period of time. Any process upset could result in the possibility of coking. To over come the problem Anti coking / gum formation, chemicals are added 
						depending on the processe need (quantity / dosing rate) at the depenaniser inlet"""),

					html.Br([]),
					html.Strong("Digital solutions:"),
					html.P("""Bringing the deep subject matter expertise in understanding the specific Petrochemicals Process Unit problem and applying Digital analytics, Artificial
						Intelligence (AI) and appropriate visualisation techniques we are able to identify """),
					html.Ol([
						html.Li(" Reasons for coking on the overhead pipelines at the inlet of 2nd stage reactor "),
						html.Li(" Pyrolysis Gasoline feed quality and its impact on process unit?"),
						html.Li(" Does Chemical dosing help in reducing the coke formation in the unit?"),
						html.Li(" $Benefits: Process parameters and their impact on Coking and ways to improve"),
						html.Ul([
							html.Li("how much t'put can be restored and the resulting benefits in Millions of Dollars"),
							html.Li("Avoid unplanned shutdown for the catalyst replacement resulting in increased run length gain for the process unit"),
							html.Li("Reduction in OPEX from reduced energy consumption and unplanned shutdown costs "),
							]),
						html.Li("$Visualise and pin point -"),
						html.Ul([
							html.Li("Reasons for coking"),
							html.Li("Which parameters need optimisation and why?"),
							]),
						html.Li("Proactive Technical monitoring to identify problems ahead of time and act in time to avoid unpleasant events")
						]),
					], className='writeup_body'),
				], className='six columns writeup_container' ),

		


					html.Div([ # Top row - Writeup & SVG
							html.Div([
								html.Img(
#									src=encoded_image_2,
									src='data:image/png;base64,{}'.format(encoded_image_2.decode()),
									style={
										'padding-left' : 0,
										'padding-right' : 0,
										'height':'100%',
										'width' :'100%'
										}
									)
								], className='crude-svg-file' )
							], className='row'  ),





			], className='custom-tab', selected_className='custom-tab--selected'),





		dcc.Tab (label = 'Data Analytics & Insights', children = [
					html.Div([ # Top row - Writeup & SVG
							html.Div([
								html.Img(
									src=PyGas_Troubleshoot,
#									src='data:image/png;base64,{}'.format(encoded_image_2.decode()),
									style={
										'padding-left' : 0,
										'padding-right' : 0,
										'height':'100%',
										'width' :'100%'
										}
									)
								], className='crude-svg-file' )
							], className='row'  ),



			], className='custom-tab', selected_className='custom-tab--selected'),











		dcc.Tab (label = 'Visualisation', children = [
			html.Div([
				html.Div([ # Top row - Writeup & SVG
					html.Div([ # Writeup
						html.H1(
							"Trouble shoot to improve Business Profitability!",
							className='writeup_title'),

						html.Div([

							html.P("""Coke deposition in the 2nd stage reactor inlet line of the PyGas Hydrogenation
							 Unit is the manifestation of non optimised process operation resulting increased in OPEX.
								Major areas to optimise are Process parameters, catalyst run length and chemicals consumption. """),

					    html.P(""" Data Analytics,Artificial Intelligence such as Machine learning, Deep learning, Tensor algorithms
								can quickly understand the system behaviour from past data using complex algorithms,
								to diagnoise Process Unit thereby,"""),	

							html.Ol([
								html.Li("Identify the source of Coke deposition"),
								html.Li("Predict Pressure drop across reactor"),
								html.Li("Optimise fuel (Steam, Power, FO/FG) consumption"),
								html.Li("Increase Catalyst run length"),
								html.Li("Plan shutdown / Catalyst replacement in advance"),
								html.Li("Operate Process unit efficiently"),
								html.Li("Reduce the OPEX"),
								html.Li("Increase PyGas T’put"),
								]),
							html.P("WoW ! We started small the benefits are multifold!")

							], className='writeup_body'),
						html.P("Potential Benefits* - US $ 25 Million ", className="writeup_footer")	


						], className='four columns writeup_container' ),
					

					html.Div([ # SVG File and Date Picker
						html.Div([ # - Title
							html.P("Pyrolysis Gasoline Hydrogenation Unit")
							], className='title_text' ),					
						html.Br([]),
						html.Div([ # SVG File
							html.Div([
								html.Img(
									src=svg,
									style={
										'padding-left' : 0,
										'padding-right' : 0,
										'height':'100%',
										'width' :'100%'
										}
									)
								], className='crude-svg-file' )
							], className='row' ),
						], className='eight columns pretty_container crude-svg-file' )
					], className='row chartRow0' ),




				html.Div([ # Second Row - Interactive & scatter plots
					html.Div([ # - Interactive plot
						html.Div([ # - Title
							html.P("PyGas Process Parameter: RPG to Recycle")
							], className='title_text' ),
						html.Div([ # - Filter criteria and Graph
							html.Div([ # - Filter criteria 
								html.Div([ # Filter - Type of Plot
									html.P("Type Of Plot", className="control_label"),
									dcc.Dropdown( # Dropdown - Type of Plot
										id='plot-selected1',
										options=[{"label": i, 'value': i} for i in plotTypes],
										value="Scatter Plot"
										)
									], className=' four columns type-of-plot' ),
								html.Div([ # Filter - X-Axis
									html.P("X-Axis", className="control_label"),
									dcc.Dropdown( # Dropdown - X-Axis
										id='xaxis-selected1',
										options=[{"label": i, 'value': i} for i in df1.columns[0:4]],
										value="Date"
										)
									], className=' four columns x-axis' ),
								html.Div([ # Filter - Y-Axis
									html.P("Y-Axis", className="control_label"),
									dcc.Dropdown( # Dropdown - Y-Axis
										id='yaxis-selected1',
										options=[{"label": i, 'value': i} for i in df1.columns[0:4]],
										value="RPGtoRecycle%"
										)
									], className=' four columns y-axis' )
								], className='row' ),

							html.Div([ # - Graph container
								html.Div([ # - Graph
									dcc.Graph(id="my-graph1",config={'displaylogo':False})
									], className='twelve columns', style={'margin-top':'5px'} )
								], className='row' )
							])
						], className='six pretty_container columns trial-four' ),
	

					html.Div([ # - Scatter plot
						html.Div([html.P('Ist Stage Reactor Outlet: Lab Results')], className='title_text' ),
						html.Div([ # - Filter criteria and Graph
							html.Div([ # - Filter criteria 
								html.Div([ # Filter - X-Axis
									html.P("X-Axis", className="control_label"),
									dcc.Dropdown(
										id='xaxis',
										options=[{'label': i.title(), 'value': i} for i in features],
										value='Date'
										),
									], className=" six columns x-axis" ),
								html.Div([ # Filter - Y-Axis
									html.P("Y-Axis", className="control_label"),
									dcc.Dropdown(
										id='yaxis',
										options=[{'label': i.title(), 'value': i} for i in features],
										value='Benzene wt%_x'
										)
									], className=" six columns y-axis" )
								], className='row afi_dropdown-menu' ),

							html.Div([ # - Graph container
								html.Div([ # - Graph
									dcc.Graph(id='feature-graphic',config={'displaylogo':False},)
									], className='twelve columns', style={'margin-top':'5px'} )
								], className='row ' )
							])
						], className='six columns pretty_container afi_dropdown_scatter' )
					], className='row chartRow1' ),



				
				html.Div([ # Second Row - Interactive & scatter plots
					html.Div([ # - Interactive plot
						html.Div([ # - Title
							html.P("PyGas Process Parameter: H2 to RPG")
							], className='title_text' ),
						html.Div([ # - Filter criteria and Graph
							html.Div([ # - Filter criteria 
								html.Div([ # Filter - Type of Plot
									html.P("Type Of Plot", className="control_label"),
									dcc.Dropdown( # Dropdown - Type of Plot
										id='plot-selected2',
										options=[{"label": i, 'value': i} for i in plotTypes],
										value="Line Plot"
										)
									], className=' four columns type-of-plot' ),
								html.Div([ # Filter - X-Axis
									html.P("X-Axis", className="control_label"),
									dcc.Dropdown( # Dropdown - X-Axis
										id='xaxis-selected2',
										options=[{"label": i, 'value': i} for i in df2.columns[0:5]],
										value="Date"
										)
									], className=' four columns x-axis' ),

								html.Div([ # Filter - Y-Axis
									html.P("Y-Axis", className="control_label"),
									dcc.Dropdown( # Dropdown - Y-Axis
										id='yaxis-selected2',
										options=[{"label": i, 'value': i} for i in df2.columns[0:5]],
										value="H2toRPG"
										)
									], className=' four columns y-axis' )
								], className='row' ),

							html.Div([ # - Graph container
								html.Div([ # - Graph
									dcc.Graph(id="my-graph2",config={'displaylogo':False})
									], className='twelve columns', style={'margin-top':'5px'} )
								], className='row' )
							])
						], className='six pretty_container columns trial-four' ),



				html.Div([ # Second Row - Interactive & scatter plots
						html.Div([ # - Title
							html.P("PyGas Process Parameter: 1St Reactor")
							], className='title_text' ),
						html.Div([ # - Filter criteria and Graph
							html.Div([ # - Filter criteria 
								html.Div([ # Filter - Type of Plot
									html.P("Type Of Plot", className="control_label"),
									dcc.Dropdown( # Dropdown - Type of Plot
										id='plot-selected3',
										options=[{"label": i, 'value': i} for i in plotTypes],
										value="Line Plot"
										)
									], className=' four columns type-of-plot' ),
								html.Div([ # Filter - X-Axis
									html.P("X-Axis", className="control_label"),
									dcc.Dropdown( # Dropdown - X-Axis
										id='xaxis-selected3',
										options=[{"label": i, 'value': i} for i in df3.columns[0:3]],
										value="Date"
										)
									], className=' four columns x-axis' ),

								html.Div([ # Filter - Y-Axis
									html.P("Y-Axis", className="control_label"),
									dcc.Dropdown( # Dropdown - Y-Axis
										id='yaxis-selected3',
										options=[{"label": i, 'value': i} for i in df3.columns[0:3]],
										value="I/LTemp_Rx1"
										)
									], className=' four columns y-axis' )
								], className='row' ),

							html.Div([ # - Graph container
								html.Div([ # - Graph
									dcc.Graph(id="my-graph3",config={'displaylogo':False})
									], className='twelve columns', style={'margin-top':'5px'} )
								], className='row ' )
							])
						], className='six pretty_container columns trial-four' )
					], className='row chartRow2' ),



				html.Div([ # Second Row - Interactive & scatter plots
					html.Div([ # - Interactive plot
						html.Div([ # - Title
							html.P("PyGas Process Parameter: Reboiler")
							], className='title_text' ),
						html.Div([ # - Filter criteria and Graph
							html.Div([ # - Filter criteria 
								html.Div([ # Filter - Type of Plot
									html.P("Type Of Plot", className="control_label"),
									dcc.Dropdown( # Dropdown - Type of Plot
										id='plot-selected4',
										options=[{"label": i, 'value': i} for i in plotTypes],
										value="Scatter Plot"
										)
									], className=' four columns type-of-plot' ),
								html.Div([ # Filter - X-Axis
									html.P("X-Axis", className="control_label"),
									dcc.Dropdown( # Dropdown - X-Axis
										id='xaxis-selected4',
										options=[{"label": i, 'value': i} for i in df4.columns[0:4]],
										value="Date"
										)
									], className=' four columns x-axis' ),

								html.Div([ # Filter - Y-Axis
									html.P("Y-Axis", className="control_label"),
									dcc.Dropdown( # Dropdown - Y-Axis
										id='yaxis-selected4',
										options=[{"label": i, 'value': i} for i in df4.columns[0:4]],
										value="Duty"
										)
									], className=' four columns y-axis' )
								], className='row' ),

							html.Div([ # - Graph container
								html.Div([ # - Graph
									dcc.Graph(id="my-graph4",config={'displaylogo':False})
									], className='twelve columns', style={'margin-top':'5px'} )
								], className='row' )
							])
						], className='six pretty_container columns trial-four' ),




				html.Div([ # Second Row - Interactive & scatter plots
						html.Div([ # - Title
							html.P("PyGas Process Parameter: DePentaniser")
							], className='title_text' ),
						html.Div([ # - Filter criteria and Graph
							html.Div([ # - Filter criteria 
								html.Div([ # Filter - Type of Plot
									html.P("Type Of Plot", className="control_label"),
									dcc.Dropdown( # Dropdown - Type of Plot
										id='plot-selected5',
										options=[{"label": i, 'value': i} for i in plotTypes],
										value="Scatter Plot"
										)
									], className=' four columns type-of-plot' ),
								html.Div([ # Filter - X-Axis
									html.P("X-Axis", className="control_label"),
									dcc.Dropdown( # Dropdown - X-Axis
										id='xaxis-selected5',
										options=[{"label": i, 'value': i} for i in df5.columns[0:9]],
										value="Date"
										)
									], className=' four columns x-axis' ),

								html.Div([ # Filter - Y-Axis
									html.P("Y-Axis", className="control_label"),
									dcc.Dropdown( # Dropdown - Y-Axis
										id='yaxis-selected5',
										options=[{"label": i, 'value': i} for i in df5.columns[0:9]],
										value="DeC5_BTM_Temp"
										)
									], className=' four columns y-axis' )
								], className='row' ),

							html.Div([ # - Graph container
								html.Div([ # - Graph
									dcc.Graph(id="my-graph5",config={'displaylogo':False})
									], className='twelve columns', style={'margin-top':'5px'} )
								], className='row ' )
							])
						], className='six pretty_container columns trial-four' )
					], className='row chartRow2' ),






				html.Div([ # Second Row - Interactive & scatter plots
					html.Div([ # - Interactive plot
						html.Div([ # - Title
							html.P("PyGas Process Parameter - Lab Results for 1st Reactor : C5 wt%")
							], className='title_text' ),
						html.Div([ # - Filter criteria and Graph
							html.Div([ # - Filter criteria 
								html.Div([ # Filter - Type of Plot
									html.P("Type Of Plot", className="control_label"),
									dcc.Dropdown( # Dropdown - Type of Plot
										id='plot-selected6',
										options=[{"label": i, 'value': i} for i in plotTypes],
										value="Scatter Plot"
										)
									], className=' four columns type-of-plot' ),
								html.Div([ # Filter - X-Axis
									html.P("X-Axis", className="control_label"),
									dcc.Dropdown( # Dropdown - X-Axis
										id='xaxis-selected6',
										options=[{"label": i, 'value': i} for i in df6.columns[0:3]],
										value="Date"
										)
									], className=' four columns x-axis' ),

								html.Div([ # Filter - Y-Axis
									html.P("Y-Axis", className="control_label"),
									dcc.Dropdown( # Dropdown - Y-Axis
										id='yaxis-selected6',
										options=[{"label": i, 'value': i} for i in df6.columns[0:3]],
										value="C5 wt%_x"
										)
									], className=' four columns y-axis' )
								], className='row' ),

							html.Div([ # - Graph container
								html.Div([ # - Graph
									dcc.Graph(id="my-graph6",config={'displaylogo':False})
									], className='twelve columns', style={'margin-top':'5px'} )
								], className='row' )
							])
						], className='six pretty_container columns trial-four' ),




				html.Div([ # Second Row - Interactive & scatter plots
						html.Div([ # - Title
							html.P("PyGas Process Parameter - Lab Results for 2nd Reactor : C5 wt%" )
							], className='title_text' ),
						html.Div([ # - Filter criteria and Graph
							html.Div([ # - Filter criteria 
								html.Div([ # Filter - Type of Plot
									html.P("Type Of Plot", className="control_label"),
									dcc.Dropdown( # Dropdown - Type of Plot
										id='plot-selected7',
										options=[{"label": i, 'value': i} for i in plotTypes],
										value="Scatter Plot"
										)
									], className=' four columns type-of-plot' ),
								html.Div([ # Filter - X-Axis
									html.P("X-Axis", className="control_label"),
									dcc.Dropdown( # Dropdown - X-Axis
										id='xaxis-selected7',
										options=[{"label": i, 'value': i} for i in df7.columns[0:15]],
										value="Date"
										)
									], className=' four columns x-axis' ),

								html.Div([ # Filter - Y-Axis
									html.P("Y-Axis", className="control_label"),
									dcc.Dropdown( # Dropdown - Y-Axis
										id='yaxis-selected7',
										options=[{"label": i, 'value': i} for i in df7.columns[0:15]],
										value="C5 wt%_y"
										)
									], className=' four columns y-axis' )
								], className='row' ),

							html.Div([ # - Graph container
								html.Div([ # - Graph
									dcc.Graph(id="my-graph7",config={'displaylogo':False})
									], className='twelve columns', style={'margin-top':'5px'} )
								], className='row ' )
							])
						], className='six pretty_container columns trial-four' )
					], className='row chartRow2' ),



















				html.Div([ # THIRD Row - Interactive & scatter plots
					html.Div([ # - Interactive plot
						html.Div([ # - Title
							html.P("PyGas Process Parameter for 2nd Reactor : 2nd Bed △P ")
							], className='title_text' ),
						html.Div([ # - Filter criteria and Graph
							html.Div([ # - Filter criteria 
								html.Div([ # Filter - Type of Plot
									html.P("Type Of Plot", className="control_label"),
									dcc.Dropdown( # Dropdown - Type of Plot
										id='plot-selected8',
										options=[{"label": i, 'value': i} for i in plotTypes],
										value="Scatter Plot"
										)
									], className=' four columns type-of-plot' ),
								html.Div([ # Filter - X-Axis
									html.P("X-Axis", className="control_label"),
									dcc.Dropdown( # Dropdown - X-Axis
										id='xaxis-selected8',
										options=[{"label": i, 'value': i} for i in df8.columns[0:15]],
										value="Date"
										)
									], className=' four columns x-axis' ),
								html.Div([ # Filter - Y-Axis
									html.P("Y-Axis", className="control_label"),
									dcc.Dropdown( # Dropdown - Y-Axis
										id='yaxis-selected8',
										options=[{"label": i, 'value': i} for i in df8.columns[0:15]],
										value="Rx2_2_3_bed_△P"
										)
									], className=' four columns y-axis' )
								], className='row' ),
							html.Div([ # - Graph container
								html.Div([ # - Graph
									dcc.Graph(id="my-graph8",config={'displaylogo':False}),
									],
									 className='twelve columns', style={'margin-top':'5px'} )

								], className='row' ),
							]),
						], className='six pretty_container columns trial-four' ),









					html.Div([ # - Piechart
						html.Div([
							html.P('Coke formation and Increased reactor △P: Reasons behind - Cyclopentadienes')
							], className='title_text' ),

 						html.Div([

							html.P("""Coke deposition in the 2nd stage reactor inlet line is the manifestation of non optimised 
								process operation resulting in increased  reactor △P across the 2nd and 3rd bed of the 2nd stage reactor.
								Both of these are due to Thermal and Catalytic polymerisation of unstable compounds particularly due to dienes.
								The resuts are polymer deposits on the pipelines as well as on the surface of the catalyst 
								 reducing both activity and cycle length"""),

					    html.P(""" The cracked Gasoline feedstock contains significant quantity of C5 of about 10-23%. 
					    	       A large percentage of these C5 are Cyclopentadiene in nature. Significant portions 
					    	        of these are hydrosaturated in the 1st stage reactor but not all of them. 
					    	        The stream then passes through Depentaniser where most of C5 are recived in the
					    	         overhead while a small quantity received at the bottom of the Depentaniser,
					    	          pass through second stage reactor where they get hydrosaturated in the lower CO-MO bed. """),	

					    html.Strong("""CycloPentadiene """),
					    html.P(""" In case of cracked gasoline, thermal polymerisation can not be completely avoided. 
					    			Cyclopentadiene (CP) polymerises as well copolymerises with dienes espially MethylCycloPentadiene (MCP).
					    			 """),	

					    html.P(""" With the increased feed rate (RPG + Recycle), Since late 2016 steam reboiler duty was drastically increased to match
					     the feed thru'put, however since the RPG percentage in fresh feed was drastically reduced the resultant product 
					     from the 1st Stage reactor had significantly less C5 components. The result, C5 components in the Depentaniser 
					     was over heated and on top of that the over head withdrawl rate is reduced leading to more C5 components
					      are dropped into Depentaniser bottom ( Refer chart). Thus leading to lower temperature of Depentaniser bottom too """),

					    html.P(""" The result, C5 components of the Depentaniser are thermally polymerised resulting in coke deposition 
					    	on the over headline to the inlet of the 2nd stage reactor. Further C5 components are already polymerised , 
					    	leading to deposition on the lower CO-MO catalyst surface . The above Cyclopentadiene polymerisation started 
					    	from 2016 and accelerated into 2017 whose effects are noticable in the charts for C5 wt% of 2nd stage outlet
					    	  as well in the in loer bed △P .""")

							], className='writeup_body'),
						html.P("Potential Benefits* - US $ 25 Million ", className="writeup_footer")	

						], className='pretty_container six columns crude-process-histogram' )
					], className='row chartRow2' )   
				], id="mainContainer" )
			], className='custom-tab', selected_className='custom-tab--selected'),











		dcc.Tab (label = 'Artificial Inelligence', children = [
			html.Div([ #SGK092319 Business Case
				html.H1("Artificial Intelligence : Predictive - Work in Progress ", className='writeup_title'),

				html.Div([
					 html.Div([ #SC03102019 - Title
                        html.Strong('C5  as a Proxy for △P :  Chemical Injection impact on Coke formation & 2nd Reactor 2_3_bed_△P'),
                            ],),
                        dcc.Graph(
                            id="graph-4",
                            figure={
                                "data": [
                                    go.Scatter(
                                        x=df_graph["Date"],
                                        y=df_graph["After AI"],
                                        line={"color": "#97151c"},
                                        mode="lines",
                                        name="With Dosing",
                                    ),
                                    go.Scatter(
                                        x=df_graph["Date"],
                                        y=df_graph[
                                            "Before AI"
                                        ],
                                        line={"color": "#b5b5b5"},
                                        mode="lines",
                                        name="Without Dosing",
                                    ),
                                ],
            	
                                           "layout": go.Layout(
                                                autosize=True,
                                                width=1000,
                                                height=280,
                                                font={"family": "Raleway", "size": 10},
                                                margin={
                                                    "r": 60,
                                                    "t": 60,
                                                    "b": 30,
                                                    "l": 60,
                                                },
                                                showlegend=True,
                                                titlefont={
                                                    "family": "Raleway",
                                                    "size": 10,
                                                },
                                                xaxis={
                                                    "autorange": True,
                                                    "range": [
                                                        "2014-12-31",
                                                        "2019-01-01",
                                                    ],
                                                    "rangeselector": {
                                                        "buttons": [
                                                            {
                                                                "count": 1,
                                                                "label": "1Y",
                                                                "step": "year",
                                                                "stepmode": "backward",
                                                            },
                                                            {
                                                                "count": 2,
                                                                "label": "2Y",
                                                                "step": "year",
                                                                "stepmode": "backward",
                                                            },
                                                            {
                                                                "count": 3,
                                                                "label": "3Y",
                                                                "step": "year",
                                                            },
                                                            {
                                                                "count": 5,
                                                                "label": "5Y",
                                                                "step": "year",
                                                                "stepmode": "backward",
                                                            },
                                                            {
                                                                "label": "All",
                                                                "step": "all",
                                                            },
                                                        ]
                                                    },
                                                    "showline": True,
                                                    "type": "date",
                                                    "zeroline": False,
                                                },
                                                yaxis={
                                                    "autorange": True,
                                                    "range": [
                                                        180,
                                                        280,
                                                    ],
                                                    "showline": True,
                                                    #"type": "linear",
                                                    "zeroline": False,
                                                },
                                            ),
                                        },
                                        config={"displayModeBar": False},
                                    ),
                                ],
                                className="pretty_container twelve columns"),

				
				html.Div([
					html.P("""By applying a range of Artificial Intelligence (AI) techniques, we are able to identify the impact of Antifoulant on the Coil Inlet Tempartaure """),
         					], className='writeup_body'),






				html.Div([ #SC03102019 First row - Scatter plots - With & Without AI
				    html.H1('Data Analytics: Insights', className='writeup_title'),
				            
				    html.Div([
				        html.Div([
				            html.Strong([ ' 2nd Reactor Performance - With and Without Dosing: (1) Thruput impact '],),

				                    dcc.Graph(
                                        id="graph-6",
                                        figure={
                                            "data": [
                                                go.Bar(
                                                    x=["With Injection", "Without Injection"],
                                                    y=["340", "325"],
                                                    marker={"color": "#97151c"},
                                                    name="A",
                                                ),
                                                go.Bar(
                                                    x=["Without Injection"],
                                                    y=["15"],
                                                    marker={"color": " #dddddd"},
                                                    name="B",
                                                ),
                                            ],
                                            "layout": go.Layout(
                                                annotations=[
                                                    {
                                                        "x": -0.0111111111111,
                                                        "y": 341,
                                                        "font": {
                                                            "color": "#7a7a7a",
                                                            "family": "Arial sans serif",
                                                            "size": 10,
                                                        },
                                                        "showarrow": False,
                                                        "text": "340 days T'put",
                                                        "xref": "x",
                                                        "yref": "y",
                                                    },
                                                    {
                                                        "x": 0.995555555556,
                                                        "y": 326,
                                                        "font": {
                                                            "color": "#7a7a7a",
                                                            "family": "Arial sans serif",
                                                            "size": 10,
                                                        },
                                                        "showarrow": False,
                                                        "text": "325 days T'put",
                                                        "xref": "x",
                                                        "yref": "y",
                                                    },
                                                    {
                                                        "x": 0.995555555556,
                                                        "y": 340,
                                                        "font": {
                                                            "color": "#7a7a7a",
                                                            "family": "Arial sans serif",
                                                            "size": 10,
                                                        },
                                                        "showarrow": False,
                                                        "text": "Fouling loss<br><b>15 days</b> T'put",
                                                        "xref": "x",
                                                        "yref": "y",
                                                    },
                                                ],
                                                autosize=False,
                                                height=260,
                                                width=320,
                                                bargap=0.4,
                                                barmode="stack",
                                                hovermode="closest",
                                                margin={
                                                    "r": 40,
                                                    "t": 20,
                                                    "b": 20,
                                                    "l": 40,
                                                },
                                                showlegend=False,
                                                title="",
                                                xaxis={
                                                    "autorange": True,
                                                    "range": [-0.5, 1.5],
                                                    "showline": True,
                                                    "tickfont": {
                                                        "family": "Arial sans serif",
                                                        "size": 10,
                                                    },
                                                    "title": "",
                                                    "type": "category",
                                                    "zeroline": False,
                                                },
                                                yaxis={
                                                    "autorange": False,
                                                    "mirror": False,
                                                    "nticks": 4,
                                                    "range": [305, 345],
                                                    "showgrid": True,
                                                    "showline": True,
                                                    "tickfont": {
                                                        "family": "Arial sans serif",
                                                        "size": 10,
                                                    },
                                                    "ticksuffix": " ",
                                                    "title": "",
                                                    "type": "linear",
                                                    "zeroline": False,
                                                },
                                            ),
                                        },
                                        config={"displayModeBar": False},
                                    ),
                        ],
                        className="seven columns ",),




                html.Div([ 				           
                 html.Strong([ '(2) Gross Margin impact due to slow down'],),
                 dcc.Graph(
                                        id="graph-7",
                                        figure={
                                            "data": [
                                                go.Bar(
                                                    x=["With Injection", "Without Injection"],
                                                    y=["340", "325"],
                                                    marker={"color": "#97151c"},
                                                    name="A",
                                                ),
                                                go.Bar(
                                                    x=["Without Injection"],
                                                    y=["15"],
                                                    marker={"color": " #dddddd"},
                                                    name="B",
                                                ),
                                            ],
                                            "layout": go.Layout(
                                                annotations=[
                                                    {
                                                        "x": -0.0111111111111,
                                                        "y": 341,
                                                        "font": {
                                                            "color": "#7a7a7a",
                                                            "family": "Arial sans serif",
                                                            "size": 8,
                                                        },
                                                        "showarrow": False,
                                                        "text": "$M 255",
                                                        "xref": "x",
                                                        "yref": "y",
                                                    },
                                                    {
                                                        "x": 0.995555555556,
                                                        "y": 326,
                                                        "font": {
                                                            "color": "#7a7a7a",
                                                            "family": "Arial sans serif",
                                                            "size": 8,
                                                        },
                                                        "showarrow": False,
                                                        "text": "$ M 244",
                                                        "xref": "x",
                                                        "yref": "y",
                                                    },
                                                    {
                                                        "x": 0.995551020408,
                                                        "y": 340,
                                                        "font": {
                                                            "color": "#7a7a7a",
                                                            "family": "Arial sans serif",
                                                            "size": 8,
                                                        },
                                                        "showarrow": False,
                                                        "text": "Loss <br><b>$M 11</b>",
                                                        "xref": "x",
                                                        "yref": "y",
                                                    },
                                                ],
                                                autosize=False,
                                                height=260,
                                                width=320,
                                                bargap=0.4,
                                                barmode="stack",
                                                hovermode="closest",
                                                margin={
                                                    "r": 40,
                                                    "t": 20,
                                                    "b": 20,
                                                    "l": 40,
                                                },
                                                showlegend=False,
                                                title="",
                                                xaxis={
                                                    "autorange": True,
                                                    "range": [-0.5, 1.5],
                                                    "showline": True,
                                                    "tickfont": {
                                                        "family": "Arial sans serif",
                                                        "size": 8,
                                                    },
                                                    "title": "",
                                                    "type": "category",
                                                    "zeroline": False,
                                                },
                                                yaxis={
                                                    "autorange": False,
                                                    "mirror": False,
                                                    "nticks": 4,
                                                    "range": [305, 345],
                                                    "showgrid": True,
                                                    "showline": True,
                                                    "tickfont": {
                                                        "family": "Arial sans serif",
                                                        "size": 10,
                                                    },
                                                    "tickprefix": "$ M",
                                                    "title": "",
                                                    "type": "linear",
                                                    "zeroline": False,
                                                },
                                            ),
                                        },
                                        config={"displayModeBar": False},
                                    ),
                        ],
                        className=" four columns ",),

                        ],
                        className="pretty_container twelve columns" ,),

                        ],
                        className="rows",
                    ),



				
				html.Div([
					html.P("""Digital analytics and  Visualisation techniques aid in highlighting the exchanger performance and the quantifies economic loss on the refinery margin due to shutdown days   """),
						 ], className='writeup_body'),

				], className='six columns writeup_container' ),

				
					html.Div([ # Top row - Writeup & SVG

							html.Div([
								html.Br([]),
								html.Img(
									src='data:image/png;base64,{}'.format(encoded_image_3.decode()),
									style={
										'padding-left' : 0,
										'padding-right': 0,
										'height':'100%',
										'width' :'100%'
										}
									)
								], className='crude-svg-file' )
							], className='row'  ),

			], className='custom-tab', selected_className='custom-tab--selected'),




		dcc.Tab (label = ' Performance Improvement & Business Profitability', children = [
			html.Div ([ #SC23092019 Business Profitability
				html.H2 ('Improved Performance and Business Profitability', className='writeup_title'),
				html.Div([
					html.P("""Applications of range of Digital technologies provided deep insights in 
					 understanding the reason behind coke formation in the reactor overhead line and 
					 Increased Delta P across Lower bed of the 2nd stage reactor.
					 Optimising process parameters enhances the
				     business profitability  in the following areas: """),
					
					html.H4("Operating Expenses (Opex):"),
					html.Ol([
						html.Li("The current increase in △P in the 2nd stage Lower CO-MO beds impacting T'put as well as Catalyst life of all the catalyst loaded in the reactor. Since with one man way, Reactor entry will need removal of all catalyst in the 2nd reactor. Any improvement on the 2nd stage reactor △P will increase the life and postpone shutdown(s/d).thereby"),
						html.Ul([
							html.Li("Improvement in catalyst life could improve  Opex Cost : US$ 1,000,000"),
							]),
						html.Li("Reduction in the Steam, Fuel oil / Fuel gas consumption in the furnace, leading to"),
						html.Ul([
							html.Li(" Savings in energy cost : US$ 150,000"),
							]),
						]),
					
					html.H4(" Margin Benefits"),
					html.Ol([
						html.Li(" Increased Thruput  (which was limiting due to increased Delta P due in lower bed of 2nd stage reactor) resulting in extra Gasoline processing. Therefore an increase of about 15 M3/hr of gasoline , considering a price differential between Benzene & PyGasoline of US$ 215/ton for 340 days in a year translates into US $ 22.5 Million per annum "),
						html.Ul([
							html.Li("Increase T'put benefits : US$ 22,500,000"),
							]),
						]),
					
					html.H4("Gain in Operating days:"),
					html.Ol([
						html.Li("Inceased run lenth results in more no of days of Gasoline processing of about one week resulting in"),
						html.Ul([
							html.Li("Increased days of Feedstock processing worth : US $ 2,800,000"),
							]),
						]),

					html.H4(" Expect Overall Performance Improvement in Benchmarking:"),
					html.P("""Significant performance improvement in the following areas """),					
					html.Ol([
						html.Li(" Operating Expenses ranking improvement resulting from reduced Maintanance cost"),
						html.Li(" Energy Index ranking improvement resulting from reduced fuel consumption"),
						html.Li(" Gross Margin ranking improvement resulting from Process Unit Utilisation"),
						html.Li(" Sum of all the above benefits resulting in overall Petrochemical ranking"),
						]),
					], className='writeup_body')
				], className='six columns writeup_container' ),

				
					html.Div([ # Top row - Writeup & SVG
							html.Div([
								html.Img(
									src='data:image/png;base64,{}'.format(encoded_image.decode()),
									style={
										'padding-left' : 0,
										'padding-right' : 0,
										'height':'100%',
										'width' :'100%'
										}
									)
								], className='crude-svg-file' )
							], className='row'  ),



			], className='custom-tab', selected_className='custom-tab--selected'),
		], className='custom-tabs-container')
	])


@app.callback(
	Output('feature-graphic', 'figure'),
	[Input('xaxis', 'value'),
	 Input('yaxis', 'value')])

def update_feature_graph(xaxis_name, yaxis_name):
	return {
		'data': [go.Scatter(
			x=dfLab[xaxis_name],
			y=dfLab[yaxis_name],
			text=dfLab['Date'],
			mode='markers',
			marker={
				'size': 15,
				'opacity': 0.5,
				'line': {'width': 0.5, 'color': 'white'}
			}
		)],

		'layout': go.Layout(
			xaxis={'title': xaxis_name.title()},
			yaxis={'title': yaxis_name.title()},
			margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
			hovermode='closest'
		)
	}


@app.callback(
	Output("my-graph1", "figure"),
	[Input("xaxis-selected1", "value"),Input("yaxis-selected1", "value"),Input("plot-selected1", "value")]
)

def update_my_graph(x_axis, y_axis, plot):
    text = {"Date":"Date", 'RPG':'RPG', 'Recycle':'Recycle', 'RPGtoRecycle%':'RPGtoRecycle%'}

	#Data for Layout1 
    trace1 = go.Scatter(x=df1[x_axis],y=df1[y_axis],mode="markers",marker={"color": "#FF5757","opacity": 0.7,'size': 7,},)
    layout1 = go.Layout(title=f"{plot}",xaxis={"title": f"{text[x_axis]}"},yaxis={"title": f"{text[y_axis]}"})
    
    trace2 = go.Scatter(x=df1["Date"].sort_values(ascending=True),y=df1[y_axis],mode="lines",
                        marker={"color": "#0B660B","opacity": 0.7,'size': 5,'line': {'width': 0.5, 'color': 'white'}},)
    layout2 = go.Layout(title=f"{plot}",xaxis={"title": "Date"},yaxis={"title": f"{text[y_axis]}"})

    trace4 = go.Scatter(x=df1["Date"].sort_values(ascending=True),y=df1[y_axis],marker={"color": "#EF2D9B"},fill='tozeroy',
                        fillcolor="#FF6BBF")
    layout4 = go.Layout(title=f"{plot}",xaxis={"title": "Date  (Note: X-axis fixed)"},yaxis={"title": f"{text[y_axis]}"})


    if plot == "Scatter Plot":
        return {"data": [trace1],"layout": layout1}
    elif plot == "Line Plot":
        return {"data": [trace2],"layout": layout2}    
    else:
        return {"data": [trace4],"layout": layout4}



@app.callback(
	Output("my-graph2", "figure"),
	[Input("xaxis-selected2", "value"),Input("yaxis-selected2", "value"),Input("plot-selected2", "value")]
)

def update_my_graph(x_axis, y_axis, plot):
    text = {"Date":"Date",  'H2_Nm3':'H2_Nm3', 'H2toRPG':'H2toRPG', 'H2toRecycle':'H2toRecycle', 'H2toHC':'H2toHC'}

	#Data for Layout1 
    trace1 = go.Scatter(x=df2[x_axis],y=df2[y_axis],mode="markers",marker={"color": "#FF5757","opacity": 0.7,'size': 7,},)
    layout1 = go.Layout(title=f"{plot}",xaxis={"title": f"{text[x_axis]}"},yaxis={"title": f"{text[y_axis]}"})
    
    trace2 = go.Scatter(x=df2["Date"].sort_values(ascending=True),y=df2[y_axis],mode="lines",
                        marker={"color": "#0B660B","opacity": 0.7,'size': 5,'line': {'width': 0.5, 'color': 'white'}},)
    layout3 = go.Layout(title=f"{plot}",xaxis={"title": "Date"},yaxis={"title": f"{text[y_axis]}"})

    trace4 = go.Scatter(x=df2["Date"].sort_values(ascending=True),y=df2[y_axis],marker={"color": "#EF2D9B"},fill='tozeroy',
                        fillcolor="#FF6BBF")
    layout4 = go.Layout(title=f"{plot}",xaxis={"title": "Date  (Note: X-axis fixed)"},yaxis={"title": f"{text[y_axis]}"})


    if plot == "Scatter Plot":
        return {"data": [trace1],"layout": layout1}
    elif plot == "Line Plot":
        return {"data": [trace2],"layout": layout3}    
    else:
        return {"data": [trace4],"layout": layout4}


@app.callback(
	Output("my-graph3", "figure"),
	[Input("xaxis-selected3", "value"),Input("yaxis-selected3", "value"),Input("plot-selected3", "value")]
)

def update_my_graph(x_axis, y_axis, plot):
    text = {"Date":"Date",  'I/LFlow_Rx1':'I/LFlow_Rx1', 'I/LTemp_Rx1':'I/LTemp_Rx1'}

	#Data for Layout1 
    trace1 = go.Scatter(x=df3[x_axis],y=df3[y_axis],mode="markers",marker={"color": "#FF5757","opacity": 0.7,'size': 7,},)
    layout1 = go.Layout(title=f"{plot}",xaxis={"title": f"{text[x_axis]}"},yaxis={"title": f"{text[y_axis]}"})
    
    trace2 = go.Scatter(x=df3["Date"].sort_values(ascending=True),y=df3[y_axis],mode="lines",
                        marker={"color": "#0B660B","opacity": 0.7,'size': 5,'line': {'width': 0.5, 'color': 'white'}},)
    layout3 = go.Layout(title=f"{plot}",xaxis={"title": "Date"},yaxis={"title": f"{text[y_axis]}"})

    trace4 = go.Scatter(x=df3["Date"].sort_values(ascending=True),y=df3[y_axis],marker={"color": "#EF2D9B"},fill='tozeroy',
                        fillcolor="#FF6BBF")
    layout4 = go.Layout(title=f"{plot}",xaxis={"title": "Date  (Note: X-axis fixed)"},yaxis={"title": f"{text[y_axis]}"})


    if plot == "Scatter Plot":
        return {"data": [trace1],"layout": layout1}
    elif plot == "Line Plot":
        return {"data": [trace2],"layout": layout3}    
    else:
        return {"data": [trace4],"layout": layout4}





@app.callback(
	Output("my-graph4", "figure"),
	[Input("xaxis-selected4", "value"),Input("yaxis-selected4", "value"),Input("plot-selected4", "value")]
)

def update_my_graph(x_axis, y_axis, plot):
    text = {"Date":"Date",  'Duty':'Duty', 'LMTD':'LMTD', 'UA':'UA'}

	#Data for Layout1 
    trace1 = go.Scatter(x=df4[x_axis],y=df4[y_axis],mode="markers",marker={"color": "#FF5757","opacity": 0.7,'size': 7,},)
    layout1 = go.Layout(title=f"{plot}",xaxis={"title": f"{text[x_axis]}"},yaxis={"title": f"{text[y_axis]}"})
    
    trace2 = go.Scatter(x=df4["Date"].sort_values(ascending=True),y=df4[y_axis],mode="lines",
                        marker={"color": "#0B660B","opacity": 0.7,'size': 5,'line': {'width': 0.5, 'color': 'white'}},)
    layout3 = go.Layout(title=f"{plot}",xaxis={"title": "Date"},yaxis={"title": f"{text[y_axis]}"})

    trace4 = go.Scatter(x=df4["Date"].sort_values(ascending=True),y=df4[y_axis],marker={"color": "#EF2D9B"},fill='tozeroy',
                        fillcolor="#FF6BBF")
    layout4 = go.Layout(title=f"{plot}",xaxis={"title": "Date  (Note: X-axis fixed)"},yaxis={"title": f"{text[y_axis]}"})


    if plot == "Scatter Plot":
        return {"data": [trace1],"layout": layout1}
    elif plot == "Line Plot":
        return {"data": [trace2],"layout": layout3}    
    else:
        return {"data": [trace4],"layout": layout4}

     
@app.callback(
	Output("my-graph5", "figure"),
	[Input("xaxis-selected5", "value"),Input("yaxis-selected5", "value"),Input("plot-selected5", "value")]
)


def update_my_graph(x_axis, y_axis, plot):
    text = {"Date":"Date", 'DeC5_I/L_Temp':'DeC5_I/L_Temp', 'DeC5_l/L_Flow':'DeC5_l/L_Flow', 'DeC5_O/H_Temp.':'DeC5_O/H_Temp.', 'DeC5_O/H_Press':'DeC5_O/H_Press','DeC5_O/H_Flow':'DeC5_O/H_Flow', 'C5_BTM_Flow':'C5_BTM_Flow', 'DeC5_BTM_Flow': 'DeC5_BTM_Flow','DeC5_BTM_Temp':'DeC5_BTM_Temp'}

	#Data for Layout1 
    trace1 = go.Scatter(x=df5[x_axis],y=df5[y_axis],mode="markers",marker={"color": "#FF5757","opacity": 0.7,'size': 7,},)
    layout1 = go.Layout(title=f"{plot}",xaxis={"title": f"{text[x_axis]}"},yaxis={"title": f"{text[y_axis]}"})
    
    trace2 = go.Scatter(x=df5["Date"].sort_values(ascending=True),y=df5[y_axis],mode="lines",
                        marker={"color": "#0B660B","opacity": 0.7,'size': 5,'line': {'width': 0.5, 'color': 'white'}},)
    layout3 = go.Layout(title=f"{plot}",xaxis={"title": "Date"},yaxis={"title": f"{text[y_axis]}"})

    trace4 = go.Scatter(x=df5["Date"].sort_values(ascending=True),y=df5[y_axis],marker={"color": "#EF2D9B"},fill='tozeroy',
                        fillcolor="#FF6BBF")
    layout4 = go.Layout(title=f"{plot}",xaxis={"title": "Date  (Note: X-axis fixed)"},yaxis={"title": f"{text[y_axis]}"})


    if plot == "Scatter Plot":
        return {"data": [trace1],"layout": layout1}
    elif plot == "Line Plot":
        return {"data": [trace2],"layout": layout3}    
    else:
        return {"data": [trace4],"layout": layout4}




@app.callback(
	Output("my-graph6", "figure"),
	[Input("xaxis-selected6", "value"),Input("yaxis-selected6", "value"),Input("plot-selected6", "value")]
)

def update_my_graph(x_axis, y_axis, plot):
    text = {"Date":"Date", 'C5 wt%_x':'C5 wt%_x', 'Benzene wt%_x':'Benzene wt%_x'}

	#Data for Layout1 
    trace1 = go.Scatter(x=df6[x_axis],y=df6[y_axis],mode="markers",marker={"color": "#FF5757","opacity": 0.7,'size': 7,},)
    layout1 = go.Layout(title=f"{plot}",xaxis={"title": f"{text[x_axis]}"},yaxis={"title": f"{text[y_axis]}"})
    
    trace2 = go.Scatter(x=df6["Date"].sort_values(ascending=True),y=df6[y_axis],mode="lines",
                        marker={"color": "#0B660B","opacity": 0.7,'size': 5,'line': {'width': 0.5, 'color': 'white'}},)
    layout3 = go.Layout(title=f"{plot}",xaxis={"title": "Date"},yaxis={"title": f"{text[y_axis]}"})

    trace4 = go.Scatter(x=df6["Date"].sort_values(ascending=True),y=df6[y_axis],marker={"color": "#EF2D9B"},fill='tozeroy',
                        fillcolor="#FF6BBF")
    layout4 = go.Layout(title=f"{plot}",xaxis={"title": "Date  (Note: X-axis fixed)"},yaxis={"title": f"{text[y_axis]}"})


    if plot == "Scatter Plot":
        return {"data": [trace1],"layout": layout1}
    elif plot == "Line Plot":
        return {"data": [trace2],"layout": layout3}    
    else:
        return {"data": [trace4],"layout": layout4}


@app.callback(
	Output("my-graph7", "figure"),
	[Input("xaxis-selected7", "value"),Input("yaxis-selected7", "value"),Input("plot-selected7", "value")]
)

def update_my_graph(x_axis, y_axis, plot):
    text = {"Date":"Date", 'C5 wt%_y':'C5 wt%_y', 'Benzene wt%_y':'Benzene wt%_y', 'Bromine Number g/100g_y':'Bromine Number g/100g_y', 'C4 wt%_y':'C4 wt%_y', 'Styrene wt%_y':'Styrene wt%_y', 'Toluene wt%_y':'Toluene wt%_y', 'Xylenes wt%_y':'Xylenes wt%_y',
 'C6~C9 NA wt%_y':'C6~C9 NA wt%_y', 'C10+ NA wt%_y':'C10+ NA wt%_y', 'C9 Aro wt%_y':'C9 Aro wt%_y', 'C10 Aro wt%_y':'C10 Aro wt%_y', 'DV g/100g':'DV g/100g', 'EB wt%_y':'EB wt%_y' }

	#Data for Layout1 
    trace1 = go.Scatter(x=df7[x_axis],y=df7[y_axis],mode="markers",marker={"color": "#FF5757","opacity": 0.7,'size': 7,},)
    layout1 = go.Layout(title=f"{plot}",xaxis={"title": f"{text[x_axis]}"},yaxis={"title": f"{text[y_axis]}"})
    
    trace2 = go.Scatter(x=df7["Date"].sort_values(ascending=True),y=df7[y_axis],mode="lines",
                        marker={"color": "#0B660B","opacity": 0.7,'size': 5,'line': {'width': 0.5, 'color': 'white'}},)
    layout3 = go.Layout(title=f"{plot}",xaxis={"title": "Date"},yaxis={"title": f"{text[y_axis]}"})

    trace4 = go.Scatter(x=df7["Date"].sort_values(ascending=True),y=df7[y_axis],marker={"color": "#EF2D9B"},fill='tozeroy',
                        fillcolor="#FF6BBF")
    layout4 = go.Layout(title=f"{plot}",xaxis={"title": "Date  (Note: X-axis fixed)"},yaxis={"title": f"{text[y_axis]}"})


    if plot == "Scatter Plot":
        return {"data": [trace1],"layout": layout1}
    elif plot == "Line Plot":
        return {"data": [trace2],"layout": layout3}    
    else:
        return {"data": [trace4],"layout": layout4}


@app.callback(
	Output("my-graph8", "figure"),
	[Input("xaxis-selected8", "value"),Input("yaxis-selected8", "value"),Input("plot-selected8", "value")]
)

def update_my_graph(x_axis, y_axis, plot):
    text = {"Date":"Date", 'Rx2_RPG_temp':'Rx2_RPG_temp', 'Rx2_H2_temp':'Rx2_H2_temp', 'Rx2_H2_Flow':'Rx2_H2_Flow', 'Rx2_Feed_Temp':'Rx2_Feed_Temp', 'Rx2_1st_bed_△P':'Rx2_1st_bed_△P', 'Rx2_2_3_bed_△P':'Rx2_2_3_bed_△P', 'RX2_1st_bed_O/L_T':'RX2_1st_bed_O/L_T', 
'RX2_1st_bed_I/L_T':'RX2_1st_bed_I/L_T', 'Rx2_1st_bed_△T':'Rx2_1st_bed_△T', 'Rx2_2nd_O/L_T':'Rx2_2nd_O/L_T', 'Rx2_2nd_I/L_T':'Rx2_2nd_I/L_T','Rx2_2nd_bed_△T':'Rx2_2nd_bed_△T'}

	#Data for Layout1 
    trace1 = go.Scatter(x=df8[x_axis],y=df8[y_axis],mode="markers",marker={"color": "#FF5757","opacity": 0.7,'size': 7,},)
    layout1 = go.Layout(title=f"{plot}",xaxis={"title": f"{text[x_axis]}"},yaxis={"title": f"{text[y_axis]}"})
    
    trace2 = go.Scatter(x=df8["Date"].sort_values(ascending=True),y=df8[y_axis],mode="lines",
                        marker={"color": "#0B660B","opacity": 0.7,'size': 5,'line': {'width': 0.5, 'color': 'white'}},)
    layout3 = go.Layout(title=f"{plot}",xaxis={"title": "Date"},yaxis={"title": f"{text[y_axis]}"})

    trace4 = go.Scatter(x=df8["Date"].sort_values(ascending=True),y=df8[y_axis],marker={"color": "#EF2D9B"},fill='tozeroy',
                        fillcolor="#FF6BBF")
    layout4 = go.Layout(title=f"{plot}",xaxis={"title": "Date  (Note: X-axis fixed)"},yaxis={"title": f"{text[y_axis]}"})


    if plot == "Scatter Plot":
        return {"data": [trace1],"layout": layout1}
    elif plot == "Line Plot":
        return {"data": [trace2],"layout": layout3}    
    else:
        return {"data": [trace4],"layout": layout4}      




# Main
if __name__ == '__main__':
	app.server.run(debug=True, threaded=True)
