import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='job-market-trends'),
    dcc.Interval(
        id='interval-component',
        interval=1*86400000,  # in milliseconds
        n_intervals=0
    )
])

@app.callback(
    dash.dependencies.Output('job-market-trends', 'figure'),
    [dash.dependencies.Input('interval-component', 'n_intervals')]
)
def update_graph(n):
    try:
        # Refresh data
        data = pd.read_csv('Cleaned_data.csv')
        
        # Preprocess data
        data['month_year'] = pd.to_datetime(data['month_year'])
        job_postings_per_month = data.groupby('month_year').size().reset_index(name='Number of Job Postings')
        
        # Create a plot
        fig = px.line(job_postings_per_month, x='month_year', y='Number of Job Postings', title='Job Market Trends Over Time')
        
        # Update layout for better visualization
        fig.update_layout(
            xaxis_title='Date',
            yaxis_title='Number of Job Postings',
            xaxis=dict(
                tickformat='%b %Y',
                dtick='M1'  # Show every month
            )
        )
        return fig
    except Exception as e:
        print(f"Error: {e}")
        return {}

if __name__ == '__main__':
    app.run_server(debug=True)


