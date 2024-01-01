from flask import Flask, render_template, request, redirect, url_for, session, flash
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Load questions from JSON file
with open('questions.json', 'r') as file:
    questions = json.load(file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        # Handle form submission
        answers = request.form.to_dict()
        score = calculate_score(answers)
        flash(f'Your score: {score}/{len(questions)}', 'success')
        return redirect(url_for('index'))
    return render_template('quiz.html', questions=questions)

def calculate_score(answers):
    score = 0
    for question_id, answer in answers.items():
        if answer == questions[int(question_id)]['correct_answer']:
            score += 1
    return score

if __name__ == '__main__':
    app.run(debug=True)
