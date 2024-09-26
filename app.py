import streamlit as st
import joblib

# Load the model pipeline using joblib
@st.cache_resource
def load_model():
    with open(r'D:\Project\nlp\FinComplaints\model\model_0.pkl', 'rb') as file:
        model = joblib.load(file)
    return model

# Load the LabelEncoder (optional if you still want to use it)
# @st.cache_resource
# def load_label_encoder():
#     with open(r'D:\Project\nlp\FinComplaints\model\label_encoder.pkl', 'rb') as file:
#         label_encoder = joblib.load(file)
#     return label_encoder

# Load the model and label encoder
model = load_model()
# label_encoder = load_label_encoder()  # Optional if you don't use it

# Dictionary mapping labels to department names
label_dict = {
    0: "Credit Card",
    1: "Debt Collection",
    2: "Retail Banking",
    3: "Mortgages and Loans",
    4: "Credit Reporting"
}

# Streamlit app title
st.title("Token Handling and Classification")

# Input token from the user
user_token = st.text_area("Enter the token for classification:")

# When the user clicks the 'Submit Token' button
if st.button("Submit Token"):
    if user_token:
        # Make a prediction using the loaded model
        department_prediction = model.predict([user_token])

        # Get the predicted department from the dictionary
        predicted_department = label_dict.get(department_prediction[0], "Unknown Department")

        # Display the department handling the token
        st.write(f"Token served to: {predicted_department} Department")

        # Display confirmation message
        st.success("Token is filled successfully!")
    else:
        st.warning("Please enter a token for classification.")
