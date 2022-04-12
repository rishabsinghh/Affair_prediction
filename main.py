from unicodedata import name
import streamlit as st
import pandas as pd
import numpy as np
import pickle
model=pickle.load(open('clf.pkl','rb'))
def predict(list1):
    results=model.predict(list1)
    return results 

def main():
    st.title("Affair prediction")
    html_temp="""
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Web App</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    age=st.text_input("Age:", "")
    rate_marriage=st.text_input("rate your marriage out of 5","")
    education=st.text_input("rate your education ","")
    years=st.text_input("Years Married ","")
    children=st.text_input("Number of Children ","")
    rel=st.text_input("Rate your Religiousness out of 5 ","")
    occ=st.text_input("Rate your Occupation","")
    hocc=st.text_input("Rate your Husband's occupation","")
    res=""
    if st.button("Predict"):
        st.write("Prediction")
        try:
            res=predict([[age,rate_marriage,education,years,children,rel,occ,hocc]])
            if res==1:
                st.success("You are cheating")
            else:
                st.success("You are a loyal woman")
        except Exception as e:
            st.write("Please enter all values")
            print(e)
        

if __name__ == '__main__':
    main()