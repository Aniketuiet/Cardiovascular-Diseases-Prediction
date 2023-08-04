import streamlit as st
import pickle
import sklearn
import numpy as np

# title

# load_model
loaded_model = pickle.load(open("C:/Users/anike/ML/Datascienceprojects/Cardiovascular-Diseases-Prediction/finalized_model1.sav", 'rb'))


def diseases_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return 'person is not suffering'
    else:
        return 'person is suffering'


def main():
    # giving a title
    st.title('Diseases Prediction Web App')
    # getting the input data from the user
    General_Health = st.text_input('Enter the General_Health')
    Checkup = st.text_input('Enter the Checkup')
    Exercise = st.text_input('Enter the Exercise')
    Skin_Cancer = st.text_input('Enter the Skin_Cancer')
    Other_Cancer = st.text_input('Enter the Other_Cancer')
    Depression = st.text_input('Enter the Depression')
    Diabetes = st.text_input('Enter the Diabetes')
    Arthritis = st.text_input('Enter the Arthritis')
    Sex = st.text_input('Enter the Sex')
    Age_Category = st.text_input('Enter the Age_Category')
    Height = st.text_input('Enter the Height_(cm)')
    Weight = st.text_input('Enter the Weight_(kg)')
    BMI = st.text_input('Enter the BMI')
    Smoking_History = st.text_input('Enter the Smoking_History')
    Alcohol_Consumption = st.text_input('Enter the Alcohol_Consumption')
    Fruit_Consumption = st.text_input('Enter the Fruit_Consumption')
    Green_Vegetables_Consumption = st.text_input('Enter the Green_Vegetables_Consumption')
    FriedPotato_Consumption = st.text_input('Enter the FriedPotato_Consumption')

    # code for Prediction
    diagnosis = ''

    # creating a button for Prediction

    if st.button('Diseases Test Result'):
        diagnosis = diseases_prediction([General_Health, Checkup, Exercise, Skin_Cancer, Other_Cancer, Depression, Diabetes, Arthritis, Sex, Age_Category, Height, Weight, BMI, Smoking_History, Alcohol_Consumption, Fruit_Consumption, Green_Vegetables_Consumption, FriedPotato_Consumption])

    st.success(diagnosis)


if __name__ == '__main__':
    main()