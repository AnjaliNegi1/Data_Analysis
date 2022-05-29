import streamlit as st
import pandas as pd
import seaborn as sns


st.title("DATA ANALYSIS")
st.subheader("Auto Mobile Industry analysis")


data = pd.read_csv('cars_engage_2022.csv')

data_shape = st.radio("Which dimension do you want to know ?", ('rows', 'columns'))
if data_shape== 'rows':
                st.text("Number of rows")
                st.write(data.shape[0])
if data_shape== 'columns':
                st.text("Number of columns")
                st.write(data.shape[1])

st.text("Different Makers")
st.write(data['Make'].value_counts())

st.text("Most Popular Models")
st.write(data['Model'].value_counts())

st.text("Popular car displacements")
st.write(data['Displacement'].value_counts())

st.text("Fuel used by most ")
st.write(data['Fuel_Type'].value_counts())

st.text("How many are Automatic?")
st.write(data[data['Type'].isin(['Automatic'])])

st.text("Whether it has a Parking Assistance or not?")
st.write(data[data['Parking_Assistance'].isin(['Rear sensors with camera'])])

st.text("How many has a Navigation System?")
st.write(data['Navigation_System'].value_counts())
st.write(data[data['Navigation_System'].isin(['Yes'])])