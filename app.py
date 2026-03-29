import streamlit as st 
import joblib
import pandas as pd
import numpy as np 
model = joblib.load("model.pkl")
st.title("Student Performance Predictor")
st.set_page_config(page_title="Student Predictor",layout='centered')
st.markdown("Enter Student details to predict final grade (G3)")
col1,col2 = st.columns(2)
with col1:
    age = st.slider("Age",10,25,15)
    Medu = st.slider("Mother Education (0-4)",0,4,2)
    Fedu = st.slider("Father Education (0-4)",0,4,2)
    traveltime = st.slider("Travel Time (1-4)",1,4,2)
    studytime = st.slider("Study Time (1-4)",1,4,2)
    failures = st.slider("Failures",0,4,0)
with col2:
    higher = st.selectbox("Want higher Education",['yes','no'])
    internet = st.selectbox("Internet Access?",['yes','no'])
    freetime = st.slider("Free Time (1-5)", 1, 5, 3)
    goout = st.slider("Going Out (1-5)", 1, 5, 3)
    health = st.slider("Health (1-5)", 1, 5, 3)
    absences = st.slider("Absences", 0, 100, 5)
    G1 = st.slider("MST1", 0, 20, 10)
    G2 = st.slider(" MST2", 0, 20, 10)
    # alc = st.slider("Alcohol Consumption (0–10)", 0.0, 10.0, 2.0)
    alc = 0
higher = 1 if higher == "yes" else 0
internet = 1 if internet == "yes" else 0
if st.button("🔮 Predict"):
    data = pd.DataFrame([[age, Medu, Fedu, traveltime, studytime,
                          failures, higher, internet, freetime,
                          goout, health, absences, G1, G2,alc]],
                        columns=[
                            'age','Medu','Fedu','traveltime','studytime',
                            'failures','higher','internet','freetime',
                            'goout','health','absences','G1','G2','alc'
                        ])

    prediction = model.predict(data)[0]
    prediction = round(float(prediction), 2)

    st.success(f"Predicted Final Grade : {prediction}")


    if prediction >= 16:
        st.info("🏆 Excellent Performance")
    elif prediction >= 12:
        st.info("👍 Good Performance")
    elif prediction >= 8:
        st.warning("⚠️ Average Performance")
    else:
        st.error("❌ Needs Improvement")

