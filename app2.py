# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 00:03:41 2024

@author: hp
"""

import streamlit as st
import pickle
import pandas as pd
import numpy as np
from PIL import Image
model = pickle.load(open('model.sav', 'rb'))
st.header(':green[Heart Disease Prediction using streamlit]')
st.markdown("""<b>Streamlit is an open-source Python framework for machine
learning and data science teams.</b>""",unsafe_allow_html=True)
st.markdown("""<b>The trend of Data Science and Analytics is increasing day by day. 
From the data science pipeline, one of the most important steps is model deployment.
We have a lot of options in python for deploying our model.
Some popular frameworks are Flask and Django. But the issue with using
these frameworks is that we should have some knowledge of 
HTML, CSS, and JavaScript.Its better to use streamlit as streamlit
is very easy for deployement of ml model.
        </b> """,unsafe_allow_html=True)

st.markdown("""<b>Using streamlit you can deploy any machine learning model
and any python project with ease and without worrying
about the frontend. Streamlit is very user-friendly.To know more about Streamlit
click on the below link</b>""",unsafe_allow_html=True)
if st.button("Know more"):
    st.markdown("[link](https://docs.streamlit.io/get-started)")
st.markdown("""<b>By using streamlit deployement of heart disease prediction 
            has been performed.</b>""",unsafe_allow_html=True)

image0=Image.open("C:\\Users\\hp\\Desktop\\placement\\heart disease prediction\\streamlit logo.jpeg")
st.image(image0)
                  
st.sidebar.header(':orange[Heart Disease Parameters]')

image1=Image.open("C:\\Users\\hp\\Desktop\\placement\\heart disease prediction\\image1.jpg")
st.image(image1,'')
image2=Image.open("C:\\Users\\hp\\Desktop\\placement\\heart disease prediction\\machine learning.jpeg")
st.image(image2,'')
image3=Image.open("C:\\Users\\hp\\Desktop\\placement\\heart disease prediction\\image2.jpg")
st.image(image3,'')

st.header(":green[Upload dataset]")
file=st.file_uploader("choose file")
st.dataframe(file)

st.header(":green[Attribute information and Research]")
st.markdown("""<b>:orange[1)Age]: The age of the patient.<br>
:orange[2)Sex]: The gender of the patient.<br>
:orange[3)Chest pain type]: A categorical attribute indicating the type of chest pain
experienced by the patient. It has four possible values.<br>
:orange[4)Resting blood pressure]: The resting blood pressure of the patient.<br>
:orange[5)Serum cholestoral]: The serum cholesterol level in mg/dl of the patient.<br>
:orange[6)Fasting blood sugar]: Indicates whether the patient's fasting blood sugar is
greater than 120 mg/dl.<br>
:orange[7)Resting electrocardiographic results]: A categorical attribute representing
the results of the resting electrocardiogram. It has three possible values.<br>
:orange[8)Maximum heart rate achieved]: The maximum heart rate achieved by the patient.<br>
:orange[9)Exercise induced angina]: Indicates whether the patient experienced angina
(chest pain) induced by exercise.<br>
:orange[10)Oldpeak]: ST depression induced by exercise relative to rest.<br>
:orange[11)Slope]: The slope of the peak exercise ST segment.<br>
:orange[12)Heart Disease]: The target column serves as the outcome variable and indicates
the presence of heart disease in the patient. A value of 0 signifies the absence
of heart disease, while a value of 1 indicates the presence of heart disease.</b>""",unsafe_allow_html=True)

#function

def user_input():
    st.subheader(":green[Select values based on these parameters]")
    Age=st.sidebar.slider('Age',1,100, 1 )
    Sex=st.sidebar.slider('Sex', 0,1)
    st.write("0 --> female , 1-->male")
    ChestPainType=st.sidebar.slider('ChestPainType', 0,3)
    st.write(" 1 ->ata, 2 -> nap,  0->ASY, 3->TA")
    RestingBP=st.sidebar.slider('RestingBP',0,210)
    Cholesterol=st.sidebar.slider('Cholesterol',0,700)
    FastingBS=st.sidebar.slider('FastingBS',0,1)
    st.write("0 -->no fasting , 1-->fasting")
    RestingECG=st.sidebar.slider('RestingECG',1,3)
    st.write("1-->Normal , 2-->ST , 3-->LVH")
    MaxHR=st.sidebar.slider("MaxHR",50,210)
    ExerciseAngina=st.sidebar.slider("ExerciseAngina",0,1)
    st.write("0 --> N , 1--> Y")
    Oldpeak=st.sidebar.slider("Oldpeak",-3,8)
    ST_Slope=st.sidebar.slider("ST_Slope",0,2)
    st.write("2-->up , 1-->flat , 0-->down")
    
    
    user_report_data={
        'Age':Age,
        'Sex':Sex,
        'ChestPainType':ChestPainType,
        'RestingBP':RestingBP,
        'Cholesterol':Cholesterol,
        'FastingBS':FastingBS,
        'RestingECG':RestingECG,
        'MaxHR':MaxHR,
        'ExerciseAngina':ExerciseAngina,
        'Oldpeak':Oldpeak,
        'ST_Slope':ST_Slope
        }
    report_data = pd.DataFrame(user_report_data, index=[0])
    return report_data
user_data =user_input()
st.subheader(":green[Heart Data]")
st.write(user_data)
predictions=model.predict(user_data)
if st.button("Predict"):
    st.subheader(str(np.round(predictions[0], 2)))
    st.text("""0 means person won't get any heart attack,
1 means there might be chance for him to get heart attack""")
    st.markdown("<b>:blue[predicted correctly] </b>",unsafe_allow_html=True)
if st.camera_input("project was done by :"):
    st.success("photo uploaded successfully")
    