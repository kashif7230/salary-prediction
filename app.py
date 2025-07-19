from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load('model.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    predicted_salary = None

    if request.method == 'POST':
        try:
            # Fetch form data
            age = int(request.form['age'])
            gender = request.form['gender']
            education = request.form['education']
            job_title = request.form['job_title']
            experience = float(request.form['experience'])

            # Prepare the input in correct format
            user_input = pd.DataFrame([{
                "Age": age,
                "Gender": gender,
                "Education Level": education,
                "Job Title": job_title,
                "Years of Experience": experience
            }])

            # Predict salary
            predicted_salary = model.predict(user_input)[0]

        except Exception as e:
            print("Error during prediction:", e)

    return render_template('index.html', predicted_salary=predicted_salary)

if __name__ == '__main__':
    app.run(debug=True)
# app.py