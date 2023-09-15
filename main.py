import pandas as pd 
import numpy as np
import pickle 
import streamlit as st 

pickle_in = open('Heart Disease Prediction.pkl', 'rb')
model = pickle.load(pickle_in, encoding='latin1')

def prediction(BMI, Smoking, AlcoholDrinking, Stroke, PhysicalHealth, MentalHealth, DiffWalking, Sex, Age, Race, Diabetic, PhysicalActivity, GenHealth, SleepTime, Asthma, KidneyDisease, SkinCancer):
    if Smoking == "No":
        Smoking = 0
    else:
        Smoking = 1

    if AlcoholDrinking == "No":
        AlcoholDrinking = 0
    else:
        AlcoholDrinking = 1
    
    if Stroke == "No":
        Stroke = 0
    else:
        Stroke = 1

    if DiffWalking == "No":
        DiffWalking = 0
    else:
        DiffWalking = 1
    
    if Sex == "Female":
        Sex = 0
    else:
        Sex = 1
    
    if Race == "White":
        Race = 5
    elif Race == "Black":
        Race = 2
    elif Race == "Asian":
        Race = 1
    elif Race == "American Indian/Alaskan Native":
        Race = 0
    elif Race == "Other":
        Race = 4
    else: 
        Race = 3
    
    if Diabetic == "Yes":
        Diabetic = 2
    elif Diabetic == "No":
        Diabetic = 0
    elif Diabetic == "No, borderline diabetes":
        Diabetic = 1
    else: 
        Diabetic = 3

    if PhysicalActivity == "Yes":
        PhysicalActivity = 1
    else:
        PhysicalActivity = 0
    
    if GenHealth == "Very Good":
        GenHealth = 4
    elif GenHealth == "Fair":
        GenHealth = 1
    elif GenHealth == "Good":
        GenHealth = 2
    elif GenHealth == "Poor":
        GenHealth = 3
    else: 
        GenHealth = 0
    
    if Asthma == "Yes":
        Asthma = 1
    else:
        Asthma = 0
    
    if KidneyDisease == "Yes":
        KidneyDisease = 1
    else:
        KidneyDisease = 0
    
    if SkinCancer == "Yes":
        SkinCancer = 1
    else:
        SkinCancer = 0

    # Convert the following variables to floats
    BMI = float(BMI)
    PhysicalHealth = float(PhysicalHealth)
    MentalHealth = float(MentalHealth)
    Age = float(Age)
    SleepTime = float(SleepTime)

    prediction = model.predict([[BMI, Smoking, AlcoholDrinking, Stroke, PhysicalHealth, MentalHealth, DiffWalking, Sex, Age, Race, Diabetic, PhysicalActivity, GenHealth, SleepTime, Asthma, KidneyDisease, SkinCancer]])
    if prediction == 0:
        pred = 'You dont have Heart Disease '
    else:
        pred = "You have Heart Disease"
    return pred

def main():

    html_temp =  """ 
        <div style ="background-color:green;padding:15px"> 
        <h1 style ="color:black;text-align:center;">Automatic Heart Disease Prediction System</h1> 
        </div> 
        
        """
    
    st.markdown(html_temp, unsafe_allow_html= True)

  
    BMI = st.number_input("Whats your BMI")
    Smoking = st.selectbox('Do you Smoke', ('No', 'Yes'))
    AlcoholDrinking =st.selectbox('Do you drink Alcohol', ('No', 'Yes'))
    Stroke=st.selectbox('Do you get Stroke', ('No', 'Yes'))
    PhysicalHealth=st.text_input("Whats your Physical Health (Between 1 to 30)")  # Use text_input to accept string values
    MentalHealth=st.number_input("Whats your Mental Health (Between 1 to 30)")
    DiffWalking=st.selectbox('Do you have diffculty in Walking', ('No', 'Yes'))
    Sex=st.selectbox('Whats your Gender', ('Female', 'Male'))
    Age=st.number_input("Whats your Age")
    Race=st.selectbox('Whats Your Race', ('White','Black', 'Asian', 'American Indian/Alaskan Native', 'other'))
    Diabetic=st.selectbox('Do you have Diabetes', ('Yes','No', 'No, borderline diabetes', 'Yes (during pregnancy)'))
    PhysicalActivity=st.selectbox('Do you do Physical Activities', ('Yes', 'No'))
    GenHealth=st.selectbox('Whats your health condition', ('Excellent','Very Good','Fair', 'Good', 'Poor'))
    SleepTime=st.text_input("How many hours do you Sleep")  # Use text_input to accept string values
    Asthma=st.selectbox('Do you have Asthma', ('No', 'Yes'))
    KidneyDisease=st.selectbox('Do you have Kidney Disease', ('No', 'Yes'))
    SkinCancer=st.selectbox('Do you have Skin Cancer', ('No', 'Yes'))
    result = ''
    if st.button("Predict"):
        result = prediction(BMI, Smoking, AlcoholDrinking, Stroke, PhysicalHealth, MentalHealth, DiffWalking, Sex, Age, Race, Diabetic, PhysicalActivity, GenHealth, SleepTime, Asthma, KidneyDisease, SkinCancer)
        st.success(result)

if __name__ == '__main__':
    main()
