import streamlit as st
import pandas as pd
import pickle

st.title("🎓 Student Dropout Prediction")

st.write("Upload dataset to predict student dropout risk.")

file = st.file_uploader("Upload CSV file")

if file:

    df = pd.read_csv(file)

    st.write("Dataset Preview")
    st.dataframe(df.head())

    if st.button("Predict Dropout"):

        model = pickle.load(open("../models/trained_model.pkl", "rb"))

        prediction = model.predict(df)

        df["Prediction"] = prediction

        st.write(df)