#!/usr/bin/env python
# coding: utf-8

# In[5]:


import streamlit as st
import pickle
import numpy as np
import pandas as pd
from datetime import datetime
def IRIS_FLOWER_CLASSIFICATION_APP():
    st.sidebar.markdown("# IRIS FLOWER CLASSIFICATION APP")
    final_model = pickle.load(open('Iris_flower_model.pkl', 'rb'))
    html_temp= """
        <div style="background-color:tomato;padding:10px">
        <h2 style="color:white;text-align:centre;">IRIS FLOWER CLASSIFICATION APP </h2>
        </div>
        """
    st.markdown(html_temp,unsafe_allow_html=True)

    st.markdown(

        """
         Here in this web app you can predict the type of Iris flower species by entering the Sepal Length,        Sepal Width, Petal Length and Petal Width. All these lengths were in centimeters.
    """
    )
    #['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']

    SepalLengthCm=float(st.number_input("Sepal Length (Cm)"))
    SepalWidthCm=float(st.number_input("Sepal Width (Cm)"))
    PetalLengthCm=float(st.number_input("Petal Length (Cm)"))
    PetalWidthCm=float(st.number_input("Petal Width (Cm)"))
    Warning="By selecting the check box you are agree to use our app.\nDon't worry!! We will not save your any data."
    check=st.checkbox("I agree",help=Warning)
    if(check):
        st.write('Great!')
        btn=st.button("predict")
        if btn:
            if SepalLengthCm == 0 or SepalWidthCm==0 or PetalLengthCm==0 or PetalWidthCm==0:
                st.text("WARNING⚠️")
                st.text("Please Enter Data to predict")
            pred=(final_model.predict(np.array([[SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm]])))
            x=pred[0]
            if x==1:
                result="Iris-setosa"
            elif x==2:
                result="Iris-versicolor"
            elif x==3:
                result="Iris-virginica"
            else:
                Result="model can't predict the species"
            st.success('Output :The Species is  {}'.format(result))
            st.text("Thanks for using")
    if st.button("About"):
            st.text("Created by Surendra Kumar")

def Human_Survival_Status_Prediction_After_Heart_Attack():
    st.sidebar.markdown("# Human Survival Status Prediction After Heart Attack")
    final_model = pickle.load(open('model.pkl', 'rb'))

    html_temp= """
        <div style="background-color:tomato;padding:10px">
        <h2 style="color:white;text-align:centre;">Human Survival Status Prediction After Heart Attack  </h2>
        </div>
        """
    st.markdown(html_temp,unsafe_allow_html=True)

    st.markdown(

        """
        Heart is one of the most important organs in Human’s body. In life, some changes may happen that may bring various diseases like, blood pressure, sugar etc. Similarly, heart failure is also a dreadful disease.Heart Failure prediction is a complex task in the medical field. This app will help in medical field to understand the effect of some major factor on survival of patient. 
    """
    )
    #['time','ejection_fraction','serum_creatinine','high_blood_pressure','serum_sodium']

    time=float(st.number_input("Time (days)"))
    ejection_fraction=float(st.number_input("Ejection Fraction (percentage)"))
    serum_creatinine=float(st.number_input("Serum Creatinine (mg/dL)"))
    high_blood_pressure=float(st.number_input("High Blood Pressure (yes=1 or No=0)"))
    serum_sodium=float(st.number_input("Serum Sodium (mEq/L)"))
    Warning="By selecting the check box you are agree to use our app.\nDon't worry. We will not save your any data."
    check=st.checkbox("I agree",help=Warning)
    if(check):
        st.write('Great!')
        btn=st.button("predict")
        if btn:
            if ejection_fraction == 0 or serum_creatinine==0 or high_blood_pressure==0 or serum_sodium==0:
                st.text("WARNING⚠️")
                st.text("Please Enter Data to predict")
            else:

                pred=(final_model.predict(np.array([[time,ejection_fraction,serum_creatinine,high_blood_pressure,serum_sodium]])))
                x=pred[0]
                if x==0:
                    result="The Patient Survived "
                elif x==1:
                    result="The Patient Not Survived"
                else:
                    result="model can't predict the status"
                st.success('Output :  {}'.format(result))
            st.text("Thanks for using")
    if st.button("About"):
            st.text("Created by Surendra Kumar")
    
    
    
page_names_to_funcs = {
    "IRIS FLOWER CLASSIFICATION APP": IRIS_FLOWER_CLASSIFICATION_APP,
    "Human Survival Status Prediction After Heart Attack": Human_Survival_Status_Prediction_After_Heart_Attack,}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()



## footer
from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgb


def image(src_as_string, **style):
    return img(src=src_as_string, style=styles(**style))


def link(link, text, **style):
    return a(_href=link, _target="_blank", style=styles(**style))(text)


def layout(*args):
    style = """
    <style>
      # MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
     .stApp { bottom: 105px; }
    </style>
    """

    style_div = styles(
        position="fixed",
        left=0,
        bottom=0,
        margin=px(0, 0, 0, 0),
        width=percent(100),
        color="black",
        text_align="center",
        height="auto",
        opacity=1
    )

    style_hr = styles(
        display="block",
        margin=px(8, 8, "auto", "auto"),
        border_style="solid",
        border_width=px(0.5)
    )

    body = p()
    foot = div(
        style=style_div
    )(
        hr(
            style=style_hr
        ),
        body
    )
    st.markdown(style,unsafe_allow_html=True)

    for arg in args:
        if isinstance(arg, str):
            body(arg)

        elif isinstance(arg, HtmlElement):
            body(arg)

    st.markdown(str(foot), unsafe_allow_html=True)


def footer():
    myargs = [
        "©️ surendraKumar",
        br(),
        link("https://www.linkedin.com/in/surendra-kumar-51802022b", image('https://icons.getbootstrap.com/assets/icons/linkedin.svg') ),
        br(),
        link("https://www.instagram.com/im_surendra_dhaka/",image('https://icons.getbootstrap.com/assets/icons/instagram.svg')),
    ]
    layout(*myargs)

if __name__ == "__main__":
    footer()

