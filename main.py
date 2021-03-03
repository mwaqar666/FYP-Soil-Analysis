



kaggle_data_inputs = kaggle_data[['pH', 'Temperature']]
print(kaggle_data_inputs.head())

adjusted_data_model = joblib.load('C:/Users/mwaqa/Desktop/FYP-Soil-Analysis/Models/EC - pH Adjusted Data Model.h5')
original_data_model = joblib.load('C:/Users/mwaqa/Desktop/FYP-Soil-Analysis/Models/EC - pH Original Data Model.h5')

adjusted_data_model_predicted_EC = adjusted_data_model.predict(kaggle_data_inputs)
original_data_model_predicted_EC = original_data_model.predict(kaggle_data_inputs)

kaggle_data['Adjusted Model EC'] = adjusted_data_model_predicted_EC
kaggle_data['Original Model EC'] = original_data_model_predicted_EC

print(kaggle_data.head())
