from flask import Flask, jsonify, render_template
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load data on app start
final_student_marks_df = pd.read_csv('final_student_marks.csv')
difficulty_df = pd.read_csv('question_difficulty_mapping.csv')
chapter_df = pd.read_csv('question_chapter_mapping.csv')

# Convert difficulty and chapter for lookup
difficulty_map = difficulty_df.set_index('question_number')['difficulty'].to_dict()
chapter_map = chapter_df.set_index('question_number')['chapter_number'].to_dict()

@app.route('/api/students')
def students_api():
    records = final_student_marks_df.to_dict(orient='records')
    return jsonify(records)

@app.route('/api/difficulty')
def difficulty_api():
    return jsonify(difficulty_df.to_dict(orient='records'))

@app.route('/api/chapter')
def chapter_api():
    return jsonify(chapter_df.to_dict(orient='records'))

@app.route('/')
def index():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
