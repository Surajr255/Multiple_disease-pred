# -*- coding: utf-8 -*-
"""MDP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GarrRqepIGy1zABN9qeyHDJBG2bGnZPe
"""

# -*- coding: utf-8 -*-


import pickle
import streamlit as st
from streamlit_option_menu import option_menu



# loading the saved models

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))




# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction','About'],
                          icons=['activity','heart','person','fullscreen'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)

if (selected == "About"):
    
    # page title
    st.title("About the project")
    st.write('''Welcome to "Multiple Disease Prediction Using Machine Learning"! Our platform is designed to help you predict the likelihood of various diseases based on your symptoms.

With the increasing number of diseases and complex symptoms, it can be challenging to identify the correct illness accurately. However, our platform uses machine learning algorithms to analyze your symptoms and provide an accurate prediction of the diseases you might be suffering from.

We have incorporated a wide range of diseases into our platform, including diabetes, heart disease, breast cancer, and Parkinson's disease. Our team, consisting of Suraj Chaudhary 11909171 and Bharath Reddy 11909164, has extensively researched and identified the most common symptoms of these diseases and created a reliable model to predict the likelihood of each one.''')

st.sidebar.title("Disease Information")

# Parkinson's Disease
st.sidebar.subheader("Parkinson's Disease")
parkinsons_info = """
Parkinson's disease is a degenerative disorder of the nervous system that mainly affects the motor system. The cause of Parkinson's disease is not known, but it is believed to involve both genetic and environmental factors. Symptoms of Parkinson's disease may include tremors, slow movements, rigid muscles, impaired posture and balance, and speech changes. Treatment for Parkinson's disease may include medications, surgery, and lifestyle modifications.
"""
st.sidebar.markdown(parkinsons_info)

# Heart Disease
st.sidebar.subheader("Heart Disease")
heart_disease_info = """
Heart disease is a term used to describe a range of conditions that affect the heart. These conditions include coronary artery disease, heart failure, and arrhythmias. The risk factors for heart disease include age, family history, high blood pressure, high cholesterol, smoking, and diabetes. Symptoms of heart disease may include chest pain, shortness of breath, and fatigue. Treatment for heart disease may include medications, surgery, and lifestyle modifications.
"""
st.sidebar.markdown(heart_disease_info)

# Breast Cancer
st.sidebar.subheader("Breast Cancer")
breast_cancer_info = """
Breast cancer is a type of cancer that develops in the breast tissue. It is the most common cancer among women worldwide. The risk factors for breast cancer include age, family history, certain gene mutations, and exposure to estrogen. Symptoms of breast cancer may include a lump in the breast, changes in breast shape, and nipple discharge. Early detection is important for successful treatment. Mammography and breast self-exams can help with early detection. Treatment for breast cancer may include surgery, radiation therapy, chemotherapy, and hormone therapy.
"""
st.sidebar.markdown(breast_cancer_info)

# Diabetes
st.sidebar.subheader("Diabetes")
diabetes_info = """
Diabetes is a chronic condition that affects how the body processes blood sugar. There are two main types of diabetes: type 1 and type 2. Type 1 diabetes is an autoimmune disease that occurs when the body's immune system attacks and destroys the insulin-producing cells in the pancreas. Type 2 diabetes occurs when the body becomes resistant to insulin or does not produce enough insulin. The risk factors for diabetes include age, family history, obesity, and physical inactivity. Symptoms of diabetes may include frequent urination, increased thirst, and blurred vision. Treatment for diabetes may include medications, insulin therapy, and lifestyle modifications.
"""
st.sidebar.markdown(diabetes_info)








