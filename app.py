from flask import Flask, request, render_template, jsonify
from utils import SalaryPrediction, load_dataset
import config
from flask_cors import CORS

df = load_dataset()

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prediction', methods=['POST'])
def prediction():
    data = request.form
    print(f"Received data: {data}")  # Debugging log

    try:
        YearsExperience = float(data['YearsExperience'])
        sal_pred = SalaryPrediction()
        predicted_salary = sal_pred.get_salary(YearsExperience)
        print(f"Predicted salary: {predicted_salary}")  # Debugging log
        return jsonify({"predicted salary": predicted_salary})
    except KeyError as e:
        print(f"KeyError: {str(e)}")  # Debugging log
        return jsonify({"error": "Missing data"}), 400
    except Exception as e:
        print(f"Error: {str(e)}")  # Debugging log
        return jsonify({"error": "An error occurred"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.FLASK_PORT_NUMBER, debug=True)
