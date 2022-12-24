import streamlit as st
import pickle
import numpy as np
import pandas as pd
from datetime import datetime

final_model = pickle.load(open('model.pkl', 'rb'))


st.title("Human Survival Status Prediction After Heart Attack")
st.markdown(
    """
    Heart is one of the most important organs in Human’s body. In life, some changes may happen that may bring various diseases like, blood pressure, sugar, etc. Similarly, heart failure is also a dreadful disease.Heart Failure prediction is a complex task in the medical field. This app will help in medical field to understand the effect of some major factor on survival of patient. 
"""
)
#['time','ejection_fraction','serum_creatinine','high_blood_pressure','serum_sodium']

time=float(st.number_input("Time (days)"))
ejection_fraction=float(st.number_input("Ejection Fraction (percentage)"))
serum_creatinine=float(st.number_input("Serum Creatinine (mg/dL)"))
high_blood_pressure=float(st.number_input("High Blood Pressure (yes=1 or No=0)"))
serum_sodium=float(st.number_input("Serum Sodium (mEq/L)"))
    
btn=st.button("predict")
if btn:
    if ejection_fraction == 0 or serum_creatinine==0 or high_blood_pressure==0 or serum_sodium==0:
        st.text("Processing, please wait .....")
        st.text("WARNING⚠️")
        st.text("Please Enter Data to predict")
    else:
        
        pred=(final_model.predict(np.array([[time,ejection_fraction,serum_creatinine,high_blood_pressure,serum_sodium]])))
        x=pred[0]
        if x==0:
            st.subheader("The Patient Survived ")
        elif x==1:
            st.subheader("The Patient Not Survived")
        else:
            st.text("model can't predict the status")
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