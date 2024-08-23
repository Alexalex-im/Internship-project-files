import streamlit as st

# Page title
st.title("Personal Details and BMI Calculator")

# User input fields
name = st.text_input("Name")
gender = st.radio("Gender", ('Male', 'Female', 'Other'))
age = st.number_input("Age", min_value=1, max_value=120, step=1)
address = st.text_area("Address")
hobbies = st.multiselect("Hobbies", ['Reading', 'Traveling', 'Sports', 'Music', 'Cooking', 'Other'])
weight = st.number_input("Weight in kg", min_value=0.1, max_value=500.0, step=0.1)
height = st.number_input("Height in cms", min_value=0.1, max_value=300.0, step=0.1)

# Calculate BMI
if weight and height:
    height_m = height / 100  # Convert height to meters
    bmi = weight / (height_m ** 2)  # BMI formula

    # Display user information and BMI
    st.subheader("Personal Details")
    st.write(f"**Name:** {name}")
    st.write(f"**Gender:** {gender}")
    st.write(f"**Age:** {age}")
    st.write(f"**Address:** {address}")
    st.write(f"**Hobbies:** {', '.join(hobbies) if hobbies else 'None'}")
    st.write(f"**Weight:** {weight} kg")
    st.write(f"**Height:** {height} cm")

    st.subheader("BMI Calculation")
    st.write(f"**BMI:** {bmi:.2f}")

    # Determine the BMI category
    if bmi < 18.5:
        st.warning("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        st.success("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        st.warning("You are overweight.")
    else:
        st.error("You are obese.")
