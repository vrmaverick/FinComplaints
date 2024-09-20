import streamlit as st
import joblib

# Load the model using joblib
@st.cache_resource
def load_model():
    with open(r'D:\Project\nlp\FinComplaints\model\model_0.pkl', 'rb') as file:
        model = joblib.load(file)
    return model

# Load the model
model = load_model()

# Streamlit app title
st.title("Token Handling and Classification")

# Input token from the user
user_token = st.text_area("Enter the token for classification:")

# When the user clicks the 'Submit Token' button
if st.button("Submit Token"):
    if user_token:
        # Make a prediction using the loaded model
        department_prediction = model.predict([user_token])

        # Display the department handling the token
        st.write(f"Token served to: {department_prediction[0]} Department")

        # Display confirmation message
        st.success("Token is filled successfully!")
    else:
        st.warning("Please enter a token for classification.")
