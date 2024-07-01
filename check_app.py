from flask import Flask, request, jsonify, render_template
from recommendation_engine import recommend_jobs 
import pandas as pd

app = Flask(__name__)

# Load your jobs data
jobs_df = pd.DataFrame({
    'job_id': [1, 2, 3, 4, 5],
    'title': ['Software Developer', 'Data Scientist', 'Project Manager', 'Graphic Designer', 'Systems Analyst'],
    'description': [
        'Develop enterprise software applications.',
        'Analyze data for business insights.',
        'Manage projects to ensure timely delivery.',
        'Create engaging designs for digital platforms.',
        'Maintain and optimize database and system performance.'
    ]
})



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def get_recommendation():
    user_prefs = request.json['preferences']
    recommendations = recommend_jobs(user_prefs, jobs_df)
    return jsonify(recommendations.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)

