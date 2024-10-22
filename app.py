from flask import Flask, request, render_template, jsonify
from utils import SalaryPrediction, load_dataset
import config
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prediction', methods = ['POST'])
def prediction():
    data = request.form
    print(data)

    YearsExperience = float(data['YearsExperience'])

    sal_pred = SalaryPrediction()

    predicted_salary = sal_pred.get_salary(YearsExperience)

    print(f"Predicted salary : {predicted_salary}" ) 
    return jsonify({"predicted salary" : predicted_salary})


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = config.FLASK_PORT_NUMBER, debug=True)