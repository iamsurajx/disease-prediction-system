import os
import pickle
from altair import DataType, value
from pandas import options
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant App",
                   layout="wide",
                   page_icon="🧑‍⚕")

# Add custom CSS
st.markdown("""
    <style>
    body {
        background-color: #f0f2f6;
        color: #333;
    }
    .sidebar .sidebar-content {
        background: #e0e4ec;
    }
    .stButton button  {
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 4px;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        transition-duration: 0.4s;
    }
    .stButton button:hover {
        background-color: white;
        color: black;
        border: 2px solid #4CAF50;
    }
    .stMarkdown h1, h2, h3 {
        color: white;
    }
    .stMarkdown {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 20px;
    }
    </style>
    """, unsafe_allow_html=True)



# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

diabetes_model = pickle.load(open(f'{working_dir}/models_train/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open(f'{working_dir}/models_train/heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open(f'{working_dir}/models_train/parkinsons_model.sav', 'rb'))

Cancer_model = pickle.load(open(f'{working_dir}/models_train/Cancer_disease_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['User guide',
                            'Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction',
                            'Cancer Prediction'],
                           menu_icon='hospital-fill',
                           icons=['house','activity', 'heart', 'person','activity'],
                           default_index=0)
# Home page
if selected == 'User guide':
    #selected == 'User guide'
    st.title('Welcome to the Health Assistant Guide')
    
    st.markdown("""
    <div style="background-color: #f9f9f9; padding: 15px; border-radius: 10px; border: 1px solid #ddd;">
        <h3 style="color: #333;">Diabetes Prediction Guide</h3>
        <ol style="color: #555;">
            <li>Enter the required personal information like <b>Patient Id<b> <b>Age</b> and <b>Gender</b>.</li>
            <li>Provide health metrics such as <b>Glucose Level</b>, <b>Blood Pressure</b>, <b>Skin Thickness</b>, <b>Insulin Level</b>, <b>BMI</b>, and <b>Diabetes Pedigree Function</b>.</li>
            <li>Click on <b>[Check Your Diabetes Here]</b> to see the prediction result.</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

    
    st.markdown("""
    <div style="background-color: #f9f9f9; padding: 15px; border-radius: 10px; border: 1px solid #ddd;">
        <h3 style="color: #333;">Heart Prediction Guide</h3>
        <ol style="color: #555;">
            <li>Enter the required personal information like <b>PatientId</b> <b>Age</b> and <b>Gender</b>.</li>
            <li>Provide health metrics such as <b>Chest Pain Type</b>, <b>Resting Blood Pressure</b>, <b>Serum Cholesterol in mg/dl</b>, <b>Fasting Blood Sugar</b>, <b>Resting Electrocardiographic</b>, <b>Max Heart Rate achieved</b>, <b>Select Exercise Induced Angina</b>, <b>ST depression induced by exercise</b>, <b>etc</b>.</li>
            <li>Click on <b>[Check Your Heart Disease Here]</b> to see the prediction result.</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: #f9f9f9; padding: 15px; border-radius: 10px; border: 1px solid #ddd;">
        <h3 style="color: #333;">Parkinson Prediction Guide</h3>
        <ol style="color: #555;">
            <li>Enter the required personal information like <b>Patient Id<b/>, <b>Age</b> and <b>Gender</b>.</li>
            <li>Provide health metrics such as <b>Family history</b>, <b>Tremors</b>, <b>Bradykinesia</b>, <b>Muscle rigidity</b>, <b>Medical history</b>, <b>Postural instability type</b>, <b>UPDRS Score</b>, <b>etc</b>.</li>
            <li>Click on <b>[Check Your Parkinson Disease Here]</b> to see the prediction result.</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: #f9f9f9; padding: 15px; border-radius: 10px; border: 1px solid #ddd;">
        <h3 style="color: #333;">Cancer Prediction Guide</h3>
        <ol style="color: #555;">
            <li>Enter the required personal information like <b>Age</b> and <b>Gender</b>.</li>
            <li>Provide health metrics such as <b>Air Pollution value</b>, <b>Alcohol use</b>, <b>Dust Allergy</b>, <b>Occupational Hazards</b>, <b>Genetic Risk</b>, <b>Chronic Lung Disease</b>, <b>Balanced Diet</b>, <b>Obesity</b>, <b>smoking</b>,<b>etc<b/>.</li>
            <li>Click on <b>[Check Your Cancer Disease Here]</b> to see the prediction result.</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: #f9f9f9; padding: 15px; border-radius: 10px; border: 1px solid #ddd;">
        <h3 style="color: #333;">NOTE:</h3>
        <ol style="color: #555;">
            <ol>1.It's important to ensure that the input provided is accurate to obtain correct results from the machine.</ol>
            <ol>2.If the input is invalid, the machine may or may not produce accurate results, so it's your responsibility to verify the information before proceeding.<ol/>
        </ol>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="margin-top: 20px; text-align: center;">
        <a href="https://mldpsystem.netlify.app//" style="color: white; background-color: #4CAF50; padding: 10px 20px; text-decoration: none; border-radius: 5px;">Click here to Home Page</a>
    </div>
    """, unsafe_allow_html=True)





### 1.Diabetes predictions:-
import streamlit as st

### 1.Diabetes predictions:-
def validate_and_convert(value, datatype, options=None):
    if datatype == 'int':
        try:
            return int(value)
        except ValueError:
            return None
    elif datatype == 'float':
        try:
            return float(value)
        except ValueError:
            return None
    elif datatype == 'char' and options:
        if value in options:
            return value
        else:
            return None
    else:
        return None


def validate_and_convert(value, data_type, min_value=None, max_value=None):
    try:
        if data_type == 'int':
            value = int(value)
        elif data_type == 'float':
            value = float(value)
        else:
            return value

        if min_value is not None and value < min_value:
            st.warning(f"Value should not be less than the range.")
            return None
        if max_value is not None and value > max_value:
            st.warning(f"Value should not be greater than the range.")
            return None
        return value
    except ValueError:
        st.warning(f"Invalid input. Please enter a valid value range.")
        return None 

def encode_gender(gender):
    if gender == 'Male':
        return 0
    elif gender == 'Female':
        return 1
    else:
        return None

# Page selection (this should be dynamic in actual implementation)
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction Using ML')

    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        PatientId = st.text_input('Patient Id', placeholder='Enter Patient Id')

    with col2:
        Age = st.text_input('Age of Person', placeholder='Enter age of Person')
        
    with col3:
        Gender = st.selectbox('Gender', options=[" Please Select type","Male","Female"])

    with col1:
        Glucose = st.text_input('Glucose Level', placeholder='Enter glucose level 0-600(mg/dL)')

    with col2:
        BloodPressure = st.text_input('Blood Pressure value', placeholder='Enter Blood Pressure 0-300(mm Hg)')

    with col3:
        SkinThickness = st.text_input('Skin Thickness value', placeholder='Enter skin fold thickness 0-100(mm)')

    with col1:
        Insulin = st.text_input('Insulin Level', placeholder='Enter Insulin Level 0-1000')

    with col2:
        BMI = st.text_input('BMI value', placeholder='Enter BMI value 0-100(kg/m)')

    with col3:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value', placeholder='Enter Diabetes Pedigree Function value 0-2.5')

    diab_diagnosis = ''

    # Check if button is clicked
    if st.button('Check Your Diabetes Here' ,key='Diabetes_test_result'):
        try:
            # Convert inputs to appropriate types
            inputs = [
                validate_and_convert(PatientId, 'int', min_value=1, max_value=830),  # Assuming PatientId is an int
                validate_and_convert(Age, 'int', min_value=0, max_value=100),
                encode_gender(Gender),  # Encode gender as 0 or 1
                validate_and_convert(Glucose, 'float', min_value=0, max_value=600),
                validate_and_convert(BloodPressure, 'int', min_value=0, max_value=300),
                validate_and_convert(SkinThickness, 'float', min_value=0, max_value=100),
                validate_and_convert(Insulin, 'float', min_value=0, max_value=1000),
                validate_and_convert(BMI, 'float', min_value=0, max_value=100),
                validate_and_convert(DiabetesPedigreeFunction, 'float', min_value=0, max_value=2.5),
            ]

            # Check if all inputs are valid
            if None not in inputs:
                # Ensure inputs match the model's expectations
                if len(inputs) == 9:
                    # Make prediction using diabetes_model (assuming it's loaded)
                    diab_prediction = diabetes_model.predict([inputs])

                    if diab_prediction[0] == 1:
                        diab_diagnosis = 'Sorry you are diabetic please consult doctor'
                    else:
                        diab_diagnosis = 'Congratulation you are not diabetic'
                else:
                    diab_diagnosis = 'The input features do not match the model expectations.'
            else:
                diab_diagnosis = 'Please enter valid values for all fields.'
                st.error(diab_diagnosis)
        except Exception as e:
            diab_diagnosis = f'An error occurred during prediction: {e}'
            st.error(diab_diagnosis)

        # Display the diagnosis message
        st.success(diab_diagnosis)


# # #heart disease
import streamlit as st
import pickle

# Encoding functions
def encode_gender(gender):
    gender_mapping = {
        "Please Select": None,
        "Male": 1,
        "Female": 0,
    }
    return gender_mapping.get(gender, None)

def encode_chest_pain(cp):
    cp_mapping = {
        "Please select": None,
        "Typical Angina": 1,
        "Atypical Angina": 2,
        "Non-Anginal Pain": 3,
        "Asymptomatic": 4
    }
    return cp_mapping.get(cp, None)

def encode_exang(exang):
    exang_mapping = {
        "Please select": None,
        "Yes": 1,
        "No": 0,
    }
    return exang_mapping.get(exang, None)

def encode_slope(slope):
    slope_mapping = {
        "Please select": None,
        "Upsloping": 1,
        "Flat": 2,
        "Downsloping": 3
    }
    return slope_mapping.get(slope, None)

def encode_thal(thal):
    thal_mapping = {
        "Please select": None,
        "No Thalassemia": 1,
        "Thalassemia Minor": 2,
        "Thalassemia Major": 3,
        "Thalassemia Intermedia": 4
    }
    return thal_mapping.get(thal, None)

# Function to validate and convert input values
def validate_and_convert(value, data_type, min_value=None, max_value=None):
    try:
        if data_type == 'int':
            value = int(value)
        elif data_type == 'float':
            value = float(value)
        else:
            return value

        if min_value is not None and value < min_value:
            st.warning(f"Value should not be less than {min_value}")
            return None
        if max_value is not None and value > max_value:
            st.warning(f"Value should not be greater than {max_value}")
            return None
        return value
    except ValueError:
        st.warning(f"Invalid input. Please enter a valid value range.")
        return None

# Page selection (this should be dynamic in actual implementation)
  # Simulate the selection of the page
if selected == 'Heart Disease Prediction':
    #selected = 'Heart Disease Prediction'
    st.title('Heart Prediction using ML')

    # Collect input values using Streamlit's input functions
    col1, col2, col3 = st.columns(3)

    with col1:
        PatientId = st.text_input('Patient Id', key='patient_id', placeholder='Enter Patient Id')
    with col2:
        Age = st.text_input('Age of Patient', key='age', placeholder='Enter Age of Patient')
    with col3:
        Gender = st.selectbox('Gender', ["Please Select", "Male", "Female"], key='gender')
    with col1:
        cp = st.selectbox('Chest Pain Type', ["Please select", "Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"], key='chest_pain')
    with col2:
        trestbps = st.text_input('Resting Blood Pressure', key='trestbps', placeholder='Enter Resting blood pressure 0-300(mm/Hg)')
    with col3:
        chol = st.text_input('Serum Cholesterol', key='chol', placeholder='Serum cholesterol level 0-600(mg/dl)')
    with col1:
        fbs = st.text_input('Fasting Blood Sugar', key='fbs', placeholder='Enter Fasting blood sugar 0-120(mg/dl)')
    with col2:
        restecg = st.text_input('Resting Electrocardiographic', key='restecg', placeholder='Enter Resting electrocardiographic value 0-2')
    with col3:
        thalach = st.text_input('Max Heart Rate achieved', key='thalach', placeholder='Enter maximum heart rate achieved value 60-220(bpm)')
    with col1:
        exang = st.selectbox('Select Exercise Induced Angina', ["Please select", "Yes", "No"], key='exang')
    with col2:
        oldpeak = st.text_input('ST depression induced by exercise', key='oldpeak', placeholder='Enter ST Depression 0-6')
    with col3:
        slope = st.selectbox('Slope of the peak exercise ST segment', ["Please select", "Upsloping", "Flat", "Downsloping"], key='slope')
    with col1:
        ca = st.text_input('Major vessels colored by fluoroscopy (0-3)', key='ca', placeholder='Enter Num Major Vessels value 0-4')
    with col2:
        thal = st.selectbox('Thalassemia', ["Please select", "No Thalassemia", "Thalassemia Minor", "Thalassemia Major", "Thalassemia Intermedia"], key='thal')
    
    # Code for prediction
    heart_diagnosis = ''

    # Validate and convert inputs on button click
    if st.button('Check your Heart Disease Here', key='heart_test_result'):
        # Validate inputs
        inputs = [
            validate_and_convert(PatientId, 'int', min_value=1, max_value=4224),
            validate_and_convert(Age, 'int', min_value=0, max_value=100),
            encode_gender(Gender),
            encode_chest_pain(cp),
            validate_and_convert(trestbps, 'int', min_value=0, max_value=300),
            validate_and_convert(chol, 'int', min_value=0, max_value=600),
            validate_and_convert(fbs, 'int', min_value=0, max_value=120),
            validate_and_convert(restecg, 'int', min_value=0, max_value=2),
            validate_and_convert(thalach, 'int', min_value=60, max_value=220),
            encode_exang(exang),
            validate_and_convert(oldpeak, 'float', min_value=0, max_value=6),
            encode_slope(slope),
            validate_and_convert(ca, 'int', min_value=0, max_value=4),
            encode_thal(thal),
        ]
        
        # Check if all inputs are valid
        if None not in inputs:
            try:
                # Ensure inputs match the model's expectations
                if len(inputs) == 14:  # There should be 14 features
                    # Make prediction using heart_disease_model (assuming it's loaded)
                    heart_prediction = heart_disease_model.predict([inputs])

                    if heart_prediction[0] == 1:
                        heart_diagnosis = 'Sorry, you have a heart disease. Please consult a doctor.'
                    else:
                        heart_diagnosis = 'Congratulations, you do not have a heart disease.'
                else:
                    heart_diagnosis = 'The input features do not match the model expectations.'
            except Exception as e:
                heart_diagnosis = f'An error occurred during prediction: {e}'
                st.error(heart_diagnosis)
        else:
            heart_diagnosis = 'Please enter valid values for all fields.'
            st.error(heart_diagnosis)

        # Display the diagnosis message
        st.success(heart_diagnosis)




 
#  #parkinsons 
# import streamlit as st

# # Define the function to validate and convert input values
# def validate_and_convert(value, datatype, options=None):
#     if datatype == 'int':
#         try:
#             return int(value)
#         except ValueError:
#             return None
#     elif datatype == 'float':
#         try:
#             return float(value)
#         except ValueError:
#             return None
#     return None

# # Define encoding functions for categorical variables
# def encode_gender(gender):
#     return 0 if gender == 'Male' else 1 if gender == 'Female' else None

# def encode_binary(value):
#     return 0 if value == 'Yes' else 1 if value == 'No' else None

# def encode_n_motor_i(value):
#     mapping = {
#         "Please select type": None,
#         "REM sleep behavior disorder": 1,
#         "Cognitive decline": 2,
#     }
#     return mapping.get(value, None)

# def encode_shimmer(value):
#     mapping = {
#         "Please select type": None,
#         "Shimmer (dB)": 1,
#         "Shimmer (APQ3)": 2,
#         "Shimmer (APQ5)": 3,
#         "Shimmer (APQ11)": 4,
#     }
#     return mapping.get(value, None)

# def validate_and_convert(value, data_type, min_value=None, max_value=None):
#     try:
#         if data_type == 'int':
#             value = int(value)
#         elif data_type == 'float':
#             value = float(value)
#         else:
#             return value

#         if min_value is not None and value < min_value:
#             st.warning(f"Value should not be less than the range.")
#             return None
#         if max_value is not None and value > max_value:
#             st.warning(f"Value should not be greater than the range.")
#             return None
#         return value
#     except ValueError:
#         st.warning(f"Invalid input. Please enter a valid value range.")
#         return None 


# # Main function for Parkinson's prediction app
# if selected == 'Parkinsons Prediction':
#     #selected =='Parkinsons Prediction'
#     st.title('Parkinsons Disease Prediction using ML')

#     # Input fields
#     col1, col2, col3 = st.columns(3)
    
#     with col1:
#         PatientId = st.text_input('Patient Id', placeholder='Enter Patient Id')

#     with col2:
#         age = st.text_input('Age', placeholder='Enter Age of Patient')

#     with col3:
#         Gender = st.selectbox('Gender', options=['Please Select', 'Male', 'Female'])
    
#     with col1:
#         fh = st.selectbox('Family history', options=['Please Select', 'Yes', 'No'])
    
#     with col2:
#         tremors = st.selectbox('Tremors', options=['Please Select', 'Yes', 'No'])
    
#     with col3:
#         bk = st.selectbox('Bradykinesia', options=['Please Select', 'Yes', 'No'])

#     with col1:
#         mr = st.selectbox('Muscle rigidity', options=['Please Select', 'Yes', 'No'])
    
#     with col2:
#         mh = st.selectbox('Medical history', options=['Please Select', 'Yes', 'No'])

#     with col3:
#         N_motor_i = st.selectbox('Postural instability type', options=['Please select type', 'REM sleep behavior disorder', 'Cognitive decline'])

#     with col1:
#         UPDRS_score = st.text_input('Unified Parkinsons Disease Rating Scale score', placeholder='Enter UPDRS Score value 0-199')

#     with col2:
#         Jitter_percent = st.text_input('Enter jitter Value', placeholder='Enter jitter value 0.1-5(%) ')

#     with col3:
#         Smoking_status = st.selectbox('Smoking status', options=['Please Select', 'Yes', 'No'])

#     with col1:
#         shimmer_value = st.text_input('Shimmer', placeholder='Enter Shimmer Percent value 0-10(%)')

#     with col2:
#         shimmer_type = st.selectbox('Type of Shimmer', options=['Please select type', 'Shimmer (dB)', 'Shimmer (APQ3)', 'Shimmer (APQ5)', 'Shimmer (APQ11)'])

#     with col3:
#         NHR = st.text_input('Noise-to-harmonics ratio', placeholder='Enter NHR value range 0-2(radio)')

#     with col1:
#         HNR = st.text_input('Harmonic-to-Noise Ratio', placeholder='Enter Harmonic-to-Noise Ratio value 0-5(dB)')

#     # Code for prediction
#     parkinsons_diagnosis = ''

#     # Check if button is clicked
#     if st.button('Check your Parkinsons Disease Here', key='Parkinsons_test_result'):
#         # Convert inputs to appropriate types
#         inputs = [
#             validate_and_convert(PatientId, 'int', min_value=1, max_value=5000),
#             validate_and_convert(age, 'int', min_value=0, max_value=100),
#             encode_gender(Gender),
#             encode_binary(fh),
#             encode_binary(tremors),
#             encode_binary(bk),
#             encode_binary(mr),
#             encode_binary(mh),
#             encode_n_motor_i(N_motor_i),
#             validate_and_convert(UPDRS_score, 'int', min_value=0, max_value=199),
#             validate_and_convert(Jitter_percent, 'float', min_value=0.1, max_value=2),  # Convert to float
#             encode_binary(Smoking_status),
#             validate_and_convert(shimmer_value, 'float', min_value=0.1, max_value=5),  
#             encode_shimmer(shimmer_type),
#             validate_and_convert(NHR, 'float', min_value=0, max_value=5),  
#             validate_and_convert(HNR, 'float', min_value=0, max_value=50), 
#         ]

#         # Check if all inputs are valid
#         if None not in inputs:
#             try:
#                 # Ensure inputs match the model's expectations
#                 if len(inputs) == 16:  # Ensure correct number of inputs
#                     # Make prediction using parkinsons_model (assuming it's loaded)
#                     parkinsons_prediction = parkinsons_model.predict([inputs])

#                     if parkinsons_prediction[0] == 1:
#                         parkinsons_diagnosis = 'Sorry you are Parkinsons disease please consult doctor'
#                     else:
#                         parkinsons_diagnosis = 'Congratulation you are not Parkinsons disease'
#                 else:
#                     parkinsons_diagnosis = 'The input features do not match the model expectations.'
#             except Exception as e:
#                 parkinsons_diagnosis = f'An error occurred during prediction: {e}'
#                 st.error(parkinsons_diagnosis)
#         else:
#             parkinsons_diagnosis = 'Please enter valid values for all fields.'
#             st.error(parkinsons_diagnosis)

#         # Display the diagnosis message
#         st.success(parkinsons_diagnosis)
#parkinsons 
import streamlit as st

# Define the function to validate and convert input values
def validate_and_convert(value, datatype, options=None):
    if datatype == 'int':
        try:
            return int(value)
        except ValueError:
            return None
    elif datatype == 'float':
        try:
            return float(value)
        except ValueError:
            return None
    return None

# Define encoding functions for categorical variables
def encode_gender(gender):
    return 0 if gender == 'Male' else 1 if gender == 'Female' else None

def encode_binary(value):
    return 0 if value == 'Yes' else 1 if value == 'No' else None

def encode_n_motor_i(value):
    mapping = {
        "Please select type": None,
        "REM sleep behavior disorder": 1,
        "Cognitive decline": 2,
    }
    return mapping.get(value, None)

def encode_shimmer(value):
    mapping = {
        "Please select type": None,
        "Shimmer (dB)": 1,
        "Shimmer (APQ3)": 2,
        "Shimmer (APQ5)": 3,
        "Shimmer (APQ11)": 4,
    }
    return mapping.get(value, None)

def validate_and_convert(value, data_type, min_value=None, max_value=None):
    try:
        if data_type == 'int':
            value = int(value)
        elif data_type == 'float':
            value = float(value)
        else:
            return value

        if min_value is not None and value < min_value:
            st.warning(f"Value should not be less than the range.")
            return None
        if max_value is not None and value > max_value:
            st.warning(f"Value should not be greater than the range.")
            return None
        return value
    except ValueError:
        st.warning(f"Invalid input. Please enter a valid value range.")
        return None 


# Main function for Parkinson's prediction app
if selected == 'Parkinsons Prediction':
    #selected =='Parkinsons Prediction'
    st.title('Parkinsons Disease Prediction using ML')

    # Input fields
    col1, col2, col3 = st.columns(3)
    
    with col1:
        PatientId = st.text_input('Patient Id', placeholder='Enter Patient Id')

    with col2:
        age = st.text_input('Age', placeholder='Enter Age of Patient')

    with col3:
        Gender = st.selectbox('Gender', options=['Please Select', 'Male', 'Female'])
    
    with col1:
        fh = st.selectbox('Family history', options=['Please Select', 'Yes', 'No'])
    
    with col2:
        tremors = st.selectbox('Tremors', options=['Please Select', 'Yes', 'No'])
    
    with col3:
        bk = st.selectbox('Bradykinesia', options=['Please Select', 'Yes', 'No'])

    with col1:
        mr = st.selectbox('Muscle rigidity', options=['Please Select', 'Yes', 'No'])
    
    with col2:
        mh = st.selectbox('Medical history', options=['Please Select', 'Yes', 'No'])

    with col3:
        N_motor_i = st.selectbox('Postural instability type', options=['Please select type', 'REM sleep behavior disorder', 'Cognitive decline'])

    with col1:
        UPDRS_score = st.text_input('Unified Parkinsons Disease Rating Scale score', placeholder='Enter UPDRS Score value 0-199')

    with col2:
        Jitter_percent = st.text_input('Enter jitter Value', placeholder='Enter jitter value 0.1-5(%) ')

    with col3:
        Smoking_status = st.selectbox('Smoking status', options=['Please Select', 'Yes', 'No'])

    with col1:
        shimmer_value = st.text_input('Shimmer', placeholder='Enter Shimmer Percent value 0-10(%)')

    with col2:
        shimmer_type = st.selectbox('Type of Shimmer', options=['Please select type', 'Shimmer (dB)', 'Shimmer (APQ3)', 'Shimmer (APQ5)', 'Shimmer (APQ11)'])

    with col3:
        NHR = st.text_input('Noise-to-harmonics ratio', placeholder='Enter NHR value range 0-2(radio)')

    with col1:
        HNR = st.text_input('Harmonic-to-Noise Ratio', placeholder='Enter Harmonic-to-Noise Ratio value 0-5(dB)')

    # Code for prediction
    parkinsons_diagnosis = ''

    # Check if button is clicked
    if st.button('Check your Parkinsons Disease Here', key='Parkinsons_test_result'):
        # Convert inputs to appropriate types
        inputs = [
            validate_and_convert(PatientId, 'int', min_value=1, max_value=5000),
            validate_and_convert(age, 'int', min_value=0, max_value=100),
            encode_gender(Gender),
            encode_binary(fh),
            encode_binary(tremors),
            encode_binary(bk),
            encode_binary(mr),
            encode_binary(mh),
            encode_n_motor_i(N_motor_i),
            validate_and_convert(UPDRS_score, 'int', min_value=0, max_value=199),
            validate_and_convert(Jitter_percent, 'float', min_value=0.1, max_value=2),  # Convert to float
            encode_binary(Smoking_status),
            validate_and_convert(shimmer_value, 'float', min_value=0.1, max_value=5),  
            encode_shimmer(shimmer_type),
            validate_and_convert(NHR, 'float', min_value=0, max_value=5),  
            validate_and_convert(HNR, 'float', min_value=0, max_value=50), 
        ]

        # Check if all inputs are valid
        if None not in inputs:
            try:
                # Ensure inputs match the model's expectations
                if len(inputs) == 16:  # Ensure correct number of inputs
                    # Make prediction using parkinsons_model (assuming it's loaded)
                    parkinsons_prediction = parkinsons_model.predict([inputs])

                    if parkinsons_prediction[0] == 1:
                        parkinsons_diagnosis = 'Sorry you are Parkinsons disease please consult doctor'
                    else:
                        parkinsons_diagnosis = 'Congratulation you are not Parkinsons disease'
                else:
                    parkinsons_diagnosis = 'The input features do not match the model expectations.'
            except Exception as e:
                parkinsons_diagnosis = f'An error occurred during prediction: {e}'
                st.error(parkinsons_diagnosis)
        else:
            parkinsons_diagnosis = 'Please enter valid values for all fields.'
            st.error(parkinsons_diagnosis)

        # Display the diagnosis message
        st.success(parkinsons_diagnosis)

# #Cancer Disease

import streamlit as st

# Function to validate and convert input values
def validate_and_convert(value, data_type, min_value=None, max_value=None):
    try:
        if data_type == 'int':
            value = int(value)
        elif data_type == 'float':
            value = float(value)
        else:
            return value

        if min_value is not None and value < min_value:
            st.warning(f"Value should not be less than the range.")
            return None
        if max_value is not None and value > max_value:
            st.warning(f"Value should not be greater than the range.")
            return None
        return value
    except ValueError:
        st.warning(f"Invalid input. Please enter a valid value range.")
        return None

# Encoding functions
def encode_binary_option(Gender):
    exang_mapping = {
        "Please select": None,
        "Male": 1,
        "Female": 2,
    }
    return exang_mapping.get(Gender, None)

def encode_binary_option(Alcoholuse):
    exang_mapping = {
        "Please select": None,
        "Yes": 1,
        "No": 2,
    }
    return exang_mapping.get(Alcoholuse, None)

def encode_binary_option(DustAllergy):
    exang_mapping = {
        "Please select": None,
        "Yes": 1,
        "No": 2,
    }
    return exang_mapping.get(DustAllergy, None)

def encode_binary_option(chronicLungDisease):
    exang_mapping = {
        "Please select": None,
        "Yes": 1,
        "No": 2,
    }
    return exang_mapping.get(chronicLungDisease, None)

def encode_binary_option(Obesity):
    exang_mapping = {
        "Please select": None,
        "Yes": 1,
        "No": 2,
    }
    return exang_mapping.get(Obesity, None)

def encode_binary_option(Smoking):
    exang_mapping = {
        "Please select": None,
        "Yes": 1,
        "No": 2,
    }
    return exang_mapping.get(Smoking, None)

def encode_binary_option(PassiveSmoker):
    exang_mapping = {
        "Please select": None,
        "Yes": 1,
        "No": 2,
    }
    return exang_mapping.get(PassiveSmoker, None)

def encode_binary_option(ChestPain):
    exang_mapping = {
        "Please select": None,
        "Yes": 1,
        "No": 2,
    }
    return exang_mapping.get(ChestPain, None)

def encode_binary_option(CoughingofBlood):
    exang_mapping = {
        "Please select": None,
        "Yes": 1,
        "No": 2,
    }
    return exang_mapping.get(CoughingofBlood, None)

def encode_binary_option(Fatigue):
    exang_mapping = {
        "Please select": None,
        "Yes": 1,
        "No": 2,
    }
    return exang_mapping.get(Fatigue, None)

def encode_binary_option(WeightLoss):
    exang_mapping = {
        "Please select": None,
        "Yes": 1,
        "No": 2,
    }
    return exang_mapping.get(WeightLoss, None)

def encode_binary_option(ShortnessofBreath):
    exang_mapping = {
        "Please select": None,
        "Yes": 1,
        "No": 2,
    }
    return exang_mapping.get(ShortnessofBreath, None)

def encode_binary_option(Wheezing):
    exang_mapping = {
        "Please select": None,
        "Yes": 1,
        "No": 2,
    }
    return exang_mapping.get(Wheezing, None)

def encode_binary_option(SwallowingDifficulty):
    exang_mapping = {
        "Please select": None,
        "Yes": 1,
        "No": 2,
    }
    return exang_mapping.get(SwallowingDifficulty, None)

def encode_binary_option(ClubbingofFingerNails):
    exang_mapping = {
        "Please select": None,
        "Yes": 1,
        "No": 2,
    }
    return exang_mapping.get(ClubbingofFingerNails, None)

def encode_binary_option(FrequentCold):
    exang_mapping = {
        "Please select": None,
        "Yes": 1,
        "No": 2,
    }
    return exang_mapping.get(FrequentCold, None)

def encode_binary_option(DryCough):
    exang_mapping = {
        "Please select": None,
        "Yes": 1,
        "No": 2,
    }
    return exang_mapping.get(DryCough, None)

def encode_binary_option(Snoring):
    exang_mapping = {
        "Please select": None,
        "Yes": 1,
        "No": 2,
    }
    return exang_mapping.get(Snoring, None)

# Application logic
if selected == "Cancer Prediction":
    #selected == 'Cancer Prediction'
    st.title("Cancer Disease Prediction using ML")

    col1, col2, col3 = st.columns(3)

    with col1:
        Age = st.text_input('Age', placeholder="Enter Age of Pitent")
    with col2:
        Gender = st.selectbox('Gender', options=['Please select', 'Male', 'Female'])
    with col3:
        AirPollution = st.text_input('Air Pollution value', placeholder='Enter a value between 0 and 10(Arbitrary pollution level)')
    with col1:
        Alcoholuse = st.selectbox('Alcohol use', options=['Please select', 'Yes', 'No'])
    with col2:
        DustAllergy = st.selectbox('Dust Allergy', options=['Please select', 'Yes', 'No'])
    with col3:
        OccuPationalHazards = st.text_input('Occupational Hazards', placeholder='Enter a value between 0 and 10(Arbitrary hazard level)')
    with col1:
        GeneticRisk = st.text_input('Genetic Risk', placeholder='Enter a value between 0 and 10')
    with col2:
        chronicLungDisease = st.selectbox('Chronic Lung Disease', options=['Please select', 'Yes', 'No'])
    with col3:
        BalancedDie = st.text_input('Balanced Diet', placeholder='Enter a value between 0 and 10')
    with col1:
        Obesity = st.selectbox('Obesity', options=['Please select', 'Yes', 'No'])
    with col2:
        Smoking = st.selectbox('Smoking', options=['Please select', 'Yes', 'No'])
    with col3:
        PassiveSmoker = st.selectbox('Passive Smoker', options=['Please select', 'Yes', 'No'])
    with col1:
        ChestPain = st.selectbox('Chest Pain', options=['Please select', 'Yes', 'No'])
    with col2:
        CoughingofBlood = st.selectbox('Coughing of Blood', options=['Please select', 'Yes', 'No'])
    with col3:
        Fatigue = st.selectbox('Fatigue', options=['Please select', 'Yes', 'No'])
    with col1:
        WeightLoss = st.selectbox('Weight Loss', options=['Please select', 'Yes', 'No'])
    with col2:
        ShortnessofBreath = st.selectbox('Shortness of Breath', options=['Please select', 'Yes', 'No'])
    with col3:
        Wheezing = st.selectbox('Wheezing', options=['Please select', 'Yes', 'No'])
    with col1:
        SwallowingDifficulty = st.selectbox('Swallowing Difficulty', options=['Please select', 'Yes', 'No'])
    with col2:
        ClubbingofFingerNails = st.selectbox('Clubbing of Finger Nails', options=['Please select', 'Yes', 'No'])
    with col3:
        FrequentCold = st.selectbox('Frequent Cold', options=['Please select', 'Yes', 'No'])
    with col1:
        DryCough = st.selectbox('Dry Cough', options=['Please select', 'Yes', 'No'])
    with col2:
        Snoring = st.selectbox('Snoring', options=['Please select', 'Yes', 'No'])

    cancer_diagnosis = ''

    # Check if button is clicked
    if st.button('Check your Cancer Disease Here', key='cancer_test_result'):
        # Convert inputs to appropriate types
        inputs = [
            validate_and_convert(Age, 'int', min_value=0, max_value=120),
            encode_gender(Gender),
            validate_and_convert(AirPollution, 'int', min_value=0, max_value=10),
            encode_binary_option(Alcoholuse),
            encode_binary_option(DustAllergy),
            validate_and_convert(OccuPationalHazards, 'int', min_value=0, max_value=10),
            validate_and_convert(GeneticRisk, 'int', min_value=0, max_value=10),
            encode_binary_option(chronicLungDisease),
            validate_and_convert(BalancedDie, 'int', min_value=0, max_value=10),
            encode_binary_option(Obesity),
            encode_binary_option(Smoking),
            encode_binary_option(PassiveSmoker),
            encode_binary_option(ChestPain),
            encode_binary_option(CoughingofBlood),
            encode_binary_option(Fatigue),
            encode_binary_option(WeightLoss),
            encode_binary_option(ShortnessofBreath),
            encode_binary_option(Wheezing),
            encode_binary_option(SwallowingDifficulty),
            encode_binary_option(ClubbingofFingerNails),
            encode_binary_option(FrequentCold),
            encode_binary_option(DryCough),
            encode_binary_option(Snoring),
        ]

        # Check if all inputs are valid
        if None not in inputs:
            try:
                # Ensure inputs match the model's expectations
                if len(inputs) == 23:  # Ensure correct number of inputs
                    # Make prediction using cancer_model (assuming it's loaded)
                    cancer_prediction = Cancer_model.predict([inputs])

                    if cancer_prediction[0] == 1:
                        cancer_diagnosis = 'Sorry, you have cancer disease. Please consult a doctor.'
                    else:
                        cancer_diagnosis = 'Congratulations, you do not have cancer disease.'
                else:
                    cancer_diagnosis = 'The input features do not match the model expectations.'
            except Exception as e:
                cancer_diagnosis = f'An error occurred during prediction: {e}'
                st.error(cancer_diagnosis)
        else:
            cancer_diagnosis = 'Please enter valid values for all fields.'
            st.error(cancer_diagnosis)

        # Display the diagnosis message
        st.success(cancer_diagnosis)
