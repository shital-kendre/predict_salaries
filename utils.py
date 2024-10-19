import pickle
# import json
import numpy as np
import config
import warnings
import pandas as pd
warnings.filterwarnings('ignore')

class SalaryPrediction():
    def __init__(self):
        pass

    def __load_data(self):
        with open(config.MODEL_FILE_NAME, 'rb') as f:
            self.model = pickle.load(f)

    def get_salary(self, YearsExperience):
    
        self.__load_data()
        # features_count = 1
        # test_array = np.zeros((1,features_count))
        test_array = np.array([[YearsExperience]])
        predicted_salary = np.around(self.model.predict(test_array)[0],3)
        print("predicted salary :", predicted_salary )
        
        return predicted_salary
    
def load_dataset():
    df = pd.read_csv(config.CSV_FILE_NAME)
    return df