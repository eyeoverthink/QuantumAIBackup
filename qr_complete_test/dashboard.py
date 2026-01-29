import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import requests

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("🚀 Tachyon Brain Dashboard"),
    
    html.H3("📡 Communicate with Tachyon Brain"),
    dcc.Input(id='input-message', type='text', placeholder="Type a message..."),
    html.Button('Send', id='send-button', n_clicks=0),
    html.Div(id='response-output'),

    html.H3("⚡ Process Data"),
    dcc.Input(id='input-data', type='text', placeholder="Enter data (comma-separated)..."),
    html.Button('Process', id='process-button', n_clicks=0),
    html.Div(id='processed-output'),

    html.H3("🔮 Make a Decision"),
    dcc.Input(id='decision-options', type='text', placeholder="Options (comma-separated)..."),
    html.Button('Decide', id='decision-button', n_clicks=0),
    html.Div(id='decision-output'),

    html.H3("🌀 Aggregate Data"),
    html.Button('Get Aggregated Data', id='aggregate-button', n_clicks=0),
    html.Div(id='aggregate-output'),
])

# Callbacks for the dashboard
@app.callback(
    Output('response-output', 'children'),
    Input('send-button', 'n_clicks'),
    Input('input-message', 'value')
)
def update_communication(n_clicks, message):
    if n_clicks > 0:
        print(f"Sending message: {message}")  # Debugging output
        try:
            response = requests.post("http://localhost:5051/communicate", json={"message": message})
            response.raise_for_status()
            print(f"Response: {response.json()}")  # Debugging output
            return response.json().get('response', 'No response received.')
        except requests.exceptions.RequestException as e:
            print(f"Error communicating with API: {str(e)}")  # Debugging output
            return f"Error communicating with API: {str(e)}"

@app.callback(
    Output('processed-output', 'children'),
    Input('process-button', 'n_clicks'),
    Input('input-data', 'value')
)
def update_processing(n_clicks, data):
    if n_clicks > 0 and data:
        try:
            data_list = [float(x.strip()) for x in data.split(',')]
            response = requests.post("http://localhost:5051/process", json={"data": data_list})
            response.raise_for_status()
            return f"Processed Data: {response.json().get('processed_data', 'No data returned.')}"
        except ValueError:
            return "Invalid input data format. Please enter numbers separated by commas."
        except requests.exceptions.RequestException as e:
            return f"Error processing data: {str(e)}"

@app.callback(
    Output('decision-output', 'children'),
    Input('decision-button', 'n_clicks'),
    Input('decision-options', 'value')
)
def update_decision(n_clicks, options):
    if n_clicks > 0 and options:
        try:
            options_list = options.split(',')
            response = requests.post("http://localhost:5051/decision", json={"options": options_list})
            response.raise_for_status()
            return f"Tachyon Brain chose: {response.json().get('decision', 'No decision made.')}"
        except requests.exceptions.RequestException as e:
            return f"Error making decision: {str(e)}"

@app.callback(
    Output('aggregate-output', 'children'),
    Input('aggregate-button', 'n_clicks')
)
def update_aggregation(n_clicks):
    if n_clicks > 0:
        try:
            response = requests.get("http://localhost:5051/aggregate")
            response.raise_for_status()
            return f"Aggregated Data: {response.json().get('aggregated_data', 'No data returned.')}"
        except requests.exceptions.RequestException as e:
            return f"Error retrieving aggregated data: {str(e)}"

if __name__ == '__main__':
    app.run_server(debug=True)