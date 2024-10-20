from flask import Flask, request, render_template, jsonify
from utils import SalaryPrediction, load_dataset  # Ensure this is correctly defined
import config
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prediction', methods=['POST'])
def prediction():
    data = request.get_json()  # Get JSON data from the request
    print(data)  # Debugging log

    # Check if the expected key exists in the received data
    if 'YearsExperience' not in data:
        return jsonify({"error": "Missing key 'YearsExperience'"}), 400

    try:
        YearsExperience = float(data['YearsExperience'])  # Extract and convert to float

        sal_pred = SalaryPrediction()  # Initialize your prediction class
        predicted_salary = sal_pred.get_salary(YearsExperience)  # Get predicted salary

        print(f"Predicted salary: {predicted_salary}")  # Debugging log
        return jsonify({"predicted salary": predicted_salary})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.FLASK_PORT_NUMBER, debug=True)
