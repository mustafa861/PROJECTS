import streamlit as st
import pandas as pd

st.title("BMI Calculator")

# Input sliders
height = st.slider("Enter your height (in cm):", 100, 250, 175)
weight = st.slider("Enter your weight (in kg):", 40, 200, 70)  # Fixed unit

# BMI Calculation
bmi = weight / ((height / 100) ** 2)

st.write(f"Your BMI is **{bmi:.2f}**")

# Determine BMI Category
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 25:
    category = "Normal weight"
elif 25 <= bmi < 30:
    category = "Overweight"
else:
    category = "Obesity"

st.write(f"According to your BMI, you are in the **{category}** category.")

# BMI Info
st.markdown("### BMI Categories")
st.markdown("- **Underweight**: BMI less than 18.5")
st.markdown("- **Normal weight**: BMI between 18.5 and 24.9")
st.markdown("- **Overweight**: BMI between 25 and 29.9")
st.markdown("- **Obesity**: BMI 30 or greater")
