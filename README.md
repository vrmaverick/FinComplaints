# FinComplaints: Token Handling and Classification

**FinComplaints** is an NLP project designed for Semester 7. It classifies financial complaints into different departments based on the provided input token. The project utilizes a pre-trained machine learning model for token classification, hosted on Streamlit.

### Project URL
You can access the project here: [FinComplaints App](https://fincomplaints-nlp.streamlit.app/)

## Features
- **User Input**: Users can enter a token (financial complaint) into the text area for classification.
- **Department Prediction**: The app predicts the department responsible for handling the complaint.
- **Department Categories**: The complaint can be classified into one of the following departments:
  - Credit Card
  - Debt Collection
  - Retail Banking
  - Mortgages and Loans
  - Credit Reporting
- **Interactive UI**: Streamlit is used for building a simple and interactive web interface for users.

## Technology Stack
- **Streamlit**: Used to build the web interface for user input and displaying predictions.
- **Joblib**: Used to load the pre-trained classification model from a `.pkl` file.
- **Python**: Backend logic, including the prediction model and token classification.

## How It Works
1. **Model Loading**: A pre-trained model is loaded using `joblib`.
2. **User Input**: Users provide a complaint token in the input text area.
3. **Prediction**: The app predicts the appropriate department for the token using the trained model.
4. **Result Display**: The predicted department is displayed to the user.

      
## Installation
To run this project locally, follow the steps below:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/FinComplaints.git
2. **Navigate to the project directory:**:
   ```bash
   cd FinComplaints
3. **Install the required packages:**:
   ```bash
   pip install -r requirements.txt
4. **Run the Streamlit app:**:
   ```bash
   streamlit run app.py
   
## Usage
Once the app is running, enter a token (financial complaint) in the input text area.  
Click on the "Submit Token" button.  
The predicted department handling the complaint will be displayed on the screen.

<div align="center">
  <h2>Contributors</h2>
  <p><strong>Vedant Ranade</strong> - Project Developer</p>
  <p>Special thanks to <strong><a href="https://github.com/otheruser(https://github.com/Om1520)">Om patil</a></strong> for contributions to the project.</p>
</div>

<div align="center">
  <h2>Credits</h2>
  <p>This project is developed as part of the Semester 7 curriculum for a Bachelor of Engineering (BE) in Artificial Intelligence and Data Science.</p>
</div>

   
### Folder Structure
```bash
.
├── model
│   ├── model_0.pkl           # Pre-trained classification model
│   ├── label_encoder.pkl     # Optional label encoder (currently not in use)
├── app.py                    # Streamlit app code
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
