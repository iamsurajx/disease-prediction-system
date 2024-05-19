import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕")

    
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

                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction',
                            'Cancer Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person','activity'],
                           default_index=0)

#Diabetes Predictions

# Page selection (this should be dynamic in actual implementation)
# selected = 'Diabetes Prediction'

if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        PatientId = st.text_input('Patient Id')

    with col2:
        Age = st.text_input('Age of Person')
        
    with col3:
        Pregnancies = st.text_input('Pregnancies')

    with col1:
        Glucose = st.text_input('Glucose Level')

    with col2:
        BloodPressure = st.text_input('Blood Pressure value')

    with col3:
        SkinThickness = st.text_input('Skin Thickness value')

    with col1:
        Insulin = st.text_input('Insulin Level')

    with col2:
        BMI = st.text_input('BMI value')

    with col3:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    diab_diagnosis = ''

    # Function to validate and convert inputs
    def validate_and_convert(input_str, data_type):
        try:
            if data_type == 'int':
                return int(input_str)
            elif data_type == 'float':
                return float(input_str)
        except ValueError:
            return None

    # Check if button is clicked
    if st.button('Diabetes Test Result'):
        # Convert inputs to appropriate types
        inputs = [
            validate_and_convert(PatientId, 'float') , # Assuming the additional feature is a float
            validate_and_convert(Age, 'int'),
            validate_and_convert(Pregnancies, 'int'),
            validate_and_convert(Glucose , 'float'),
            validate_and_convert(BloodPressure, 'int'),
            validate_and_convert(SkinThickness, 'float'),
            validate_and_convert(Insulin, 'float'),
            validate_and_convert(BMI, 'float'),
            validate_and_convert(DiabetesPedigreeFunction, 'float'),
        ]

        # Check if all inputs are valid
        if None not in inputs:
            try:
                # Ensure inputs match the model's expectations
                if len(inputs) == 9:
                    # Make prediction using diabetes_model (assuming it's loaded)
                    diab_prediction = diabetes_model.predict([inputs])

                    if diab_prediction[0] == 1:
                        diab_diagnosis = 'The person is diabetic'
                    else:
                        diab_diagnosis = 'The person is not diabetic'
                else:
                    diab_diagnosis = 'The input features do not match the model expectations.'
            except Exception as e:
                diab_diagnosis = f'An error occurred during prediction: {e}'
                st.error(diab_diagnosis)
        else:
            diab_diagnosis = 'Please enter valid numerical values for all fields.'
            st.error(diab_diagnosis)

        # Display the diagnosis message
        st.success(diab_diagnosis)


#Heart disease
if selected == 'Heart Disease Prediction':
# Page selection (this should be dynamic in actual implementation)
 selected = 'Heart Prediction'

if selected == 'Heart Prediction':
    st.title('Heart Prediction using ML')

    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Patient Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholesterol in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Max Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina (1 = yes; 0 = no)')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by fluoroscopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversible defect')

    # Assuming the 14th feature is "target" which should not be user-provided but required by the model
    # Adding a placeholder for the 14th feature
    with col2:
        additional_feature = st.text_input('Additional Feature')

    heart_diagnosis = ''

    # Function to validate and convert inputs
    def validate_and_convert(input_str, data_type):
        try:
            if data_type == 'int':
                return int(input_str)
            elif data_type == 'float':
                return float(input_str)
        except ValueError:
            return None

    # Check if button is clicked
    if st.button('Heart Disease Test Result', key='heart_test_result'):
        # Convert inputs to appropriate types
        inputs = [
            validate_and_convert(age, 'int'),
            validate_and_convert(sex, 'int'),
            validate_and_convert(cp, 'int'),
            validate_and_convert(trestbps, 'int'),
            validate_and_convert(chol, 'int'),
            validate_and_convert(fbs, 'int'),
            validate_and_convert(restecg, 'int'),
            validate_and_convert(thalach, 'int'),
            validate_and_convert(exang, 'int'),
            validate_and_convert(oldpeak, 'float'),
            validate_and_convert(slope, 'int'),
            validate_and_convert(ca, 'int'),
            validate_and_convert(thal, 'int'),
            validate_and_convert(additional_feature, 'float')  # Additional feature
        ]

        # Check if all inputs are valid
        if None not in inputs:
            try:
                # Ensure inputs match the model's expectations
                if len(inputs) == 14:  # There should be 14 features
                    # Make prediction using heart_disease_model (assuming it's loaded)
                    heart_prediction = heart_disease_model.predict([inputs])

                    if heart_prediction[0] == 1:
                        heart_diagnosis = 'The person has heart disease'
                    else:
                        heart_diagnosis = 'The person does not have heart disease'
                else:
                    heart_diagnosis = 'The input features do not match the model expectations.'
            except Exception as e:
                heart_diagnosis = f'An error occurred during prediction: {e}'
                st.error(heart_diagnosis)
        else:
            heart_diagnosis = 'Please enter valid numerical values for all fields.'
            st.error(heart_diagnosis)

        # Display the diagnosis message
        st.success(heart_diagnosis)




    


# # Heart Disease Prediction Page
# if selected == 'Heart Disease Prediction':

#     # page title
#     st.title('Heart Disease Prediction using ML')

#     col1, col2, col3 = st.columns(3)

#     with col1:
#         age = st.text_input('Age')

#     # with col2:
#     #     sex = st.text_input('Sex')

#     with col3:
#         cp = st.text_input('Chest Pain types')

#     with col1:
#         trestbps = st.text_input('Resting Blood Pressure')

#     with col2:
#         chol = st.text_input('Serum Cholestoral in mg/dl')

#     with col3:
#         fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

#     with col1:
#         restecg = st.text_input('Resting Electrocardiographic results')

#     with col2:
#         thalach = st.text_input('Maximum Heart Rate achieved')

#     with col3:
#         exang = st.text_input('Exercise Induced Angina')

#     with col1:
#         oldpeak = st.text_input('ST depression induced by exercise')

#     with col2:
#         slope = st.text_input('Slope of the peak exercise ST segment')

#     with col3:
#         ca = st.text_input('Major vessels colored by flourosopy')

#     with col1:
#         thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

#     # code for Prediction
#     heart_diagnosis = ''

#    # creating a button for Prediction
# if st.button('Heart Disease Test Result'):
#     # Validate input fields
#     if any(value == '' for value in [Age, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]):
#         st.error('Please fill in all the input fields.')
#     else:
#         # Convert input fields to float
#         user_input = [float(x) for x in [age, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]

#         # Add default values for missing features (assuming last two features are missing)
#         user_input.extend([0.0, 0.0])  # Assuming last two features are missing, you can adjust this based on your actual requirements

#         heart_prediction = heart_disease_model.predict([user_input])

#         if heart_prediction[0] == 1:
#             heart_diagnosis = 'The person is having heart disease'
#         else:
#             heart_diagnosis = 'The person does not have any heart disease'

#     st.success(heart_diagnosis)



# Parkinsons Prediction 
if selected == "Parkinsons Prediction":

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)




#cancer predictions
if selected == "Cancer Prediction":

    # page title
    st.title("cancer's Disease Prediction using ML")

    col1, col2, col3 = st.columns(3)

    with col1:
            Age = st.text_input('Age')
    
    with col2:
            Gender = st.text_input('Gender')
    
    with col3:
            AirPollution = st.text_input('AirPollution')
    
    with col1:
            Alcoholuse = st.text_input('Alcoholuse')

    with col2:
            DustAllergy = st.text_input('DustAllergy')

    with col3:
            OccuPationalHazards = st.text_input('OccuPationalHazards')
    with col1:
            GeneticRisk = st.text_input('GeneticRisk')
    
    with col2:
            chronicLungDisease = st.text_input('chronicLungDisease')

    with col3:
            BalancedDie = st.text_input('BalancedDie')

    with col1:
            Obesity = st.text_input('Obesity')
    with col2:
            Smoking = st.text_input('Smoking')
    
    with col3:
            PassiveSmoker = st.text_input('PassiveSmoker')

    with col1:
            ChestPain = st.text_input('ChestPain')

    with col2:
            CoughingofBlood = st.text_input('CoughingofBlood')
    with col3:
            Fatigue = st.text_input('Fatigue')
    
    with col1:
            WeightLoss = st.text_input('WeightLoss')

    with col2:
            ShortnessofBreath = st.text_input('ShortnessofBreath')

    with col3:
            Wheezing = st.text_input('Wheezing')

    with col1:
            SwallowingDifficulty = st.text_input('SwallowingDifficulty')

    with col2:
            ClubbingofFingerNails = st.text_input('ClubbingofFingerNails')

    with col3:
            FrequentCold = st.text_input('FrequentCold')

    with col1:
            DryCough = st.text_input('DryCough')

    with col2:
            Snoring = st.text_input('Snoring')

    cancer_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Cancer Result"):
         # Validate input fields
            if any(value == '' for value in [Age,Gender,AirPollution,Alcoholuse,DustAllergy,OccuPationalHazards,GeneticRisk,chronicLungDisease,BalancedDie,Obesity,Smoking,PassiveSmoker,ChestPain,CoughingofBlood,Fatigue,WeightLoss,ShortnessofBreath,Wheezing,SwallowingDifficulty,ClubbingofFingerNails,FrequentCold,DryCough,Snoring]):
                st.error('Please fill in all the input fields.')
            else:
                    # Convert input fields to float
                    user_input = [float(x) for x in [Age,Gender,AirPollution,Alcoholuse,DustAllergy,OccuPationalHazards,GeneticRisk,chronicLungDisease,BalancedDie,Obesity,Smoking,PassiveSmoker,ChestPain,CoughingofBlood,Fatigue,WeightLoss,ShortnessofBreath,Wheezing,SwallowingDifficulty,ClubbingofFingerNails,FrequentCold,DryCough,Snoring]]

            user_input = [Age,Gender,AirPollution,Alcoholuse,DustAllergy,OccuPationalHazards,GeneticRisk,chronicLungDisease,BalancedDie,Obesity,Smoking,PassiveSmoker,ChestPain,CoughingofBlood,Fatigue,WeightLoss,ShortnessofBreath,Wheezing,SwallowingDifficulty,ClubbingofFingerNails,FrequentCold,DryCough,Snoring]

            # user_input = [float(x) for x in user_input]
            user_input_float = [float(x) if x.replace('.', '', 1).isdigit() else 1.0 if x.lower() == 'yes' else 0.0 if x.lower() == 'no' else None for x in user_input]


            cancer_prediction = Cancer_model.predict([user_input])

            if cancer_prediction[0] == 1:
               cancer_diagnosis = "The person has Cancer's disease"
            else:
              cancer_diagnosis = "The person does not have Cancer's disease"

    st.success(cancer_diagnosis)
    
    
# import os
# import pickle
# import streamlit as st
# from streamlit_option_menu import option_menu

# # Set page configuration
# st.set_page_config(page_title="Health Assistant",
#                    layout="wide",
#                    page_icon="🧑‍⚕")

# # getting the working directory of the main.py
# working_dir = os.path.dirname(os.path.abspath(__file__))

# # loading the saved models
# diabetes_model = pickle.load(open(f'{working_dir}/models_train/diabetes_model.sav', 'rb'))
# heart_disease_model = pickle.load(open(f'{working_dir}/models_train/heart_disease_model.sav', 'rb'))
# parkinsons_model = pickle.load(open(f'{working_dir}/models_train/parkinsons_model.sav', 'rb'))
# cancer_model = pickle.load(open(f'{working_dir}/models_train/Cancer_disease_model.sav', 'rb'))

# # sidebar for navigation
# with st.sidebar:
#     selected = option_menu('Multiple Disease Prediction System',
#                            ['Diabetes Prediction',
#                             'Heart Disease Prediction',
#                             'Parkinsons Prediction',
#                             'Cancer Prediction'],
#                            menu_icon='hospital-fill',
#                            icons=['activity', 'heart', 'person', 'activity'],
#                            default_index=0)

# # Diabetes Predictions

# if selected == 'Diabetes Prediction':
#     st.title('Diabetes Prediction using ML')

#     # Getting the input data from the user
#     col1, col2, col3 = st.columns(3)

#     with col1:
#         PatientId = st.text_input('Patient Id')

#     with col2:
#         Age = st.text_input('Age of Person')
        
#     with col3:
#         Pregnancies = st.text_input('Pregnancies')

#     with col1:
#         Glucose = st.text_input('Glucose Level')

#     with col2:
#         BloodPressure = st.text_input('Blood Pressure value')

#     with col3:
#         SkinThickness = st.text_input('Skin Thickness value')

#     with col1:
#         Insulin = st.text_input('Insulin Level')

#     with col2:
#         BMI = st.text_input('BMI value')

#     with col3:
#         DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

#     diab_diagnosis = ''

#     # Function to validate and convert inputs
#     def validate_and_convert(input_str, data_type):
#         try:
#             if data_type == 'int':
#                 return int(input_str)
#             elif data_type == 'float':
#                 return float(input_str)
#         except ValueError:
#             return None

#     # Check if button is clicked
#     if st.button('Diabetes Test Result'):
#         # Convert inputs to appropriate types
#         inputs = [
#             validate_and_convert(PatientId, 'float'),  # Assuming the additional feature is a float
#             validate_and_convert(Age, 'int'),
#             validate_and_convert(Pregnancies, 'int'),
#             validate_and_convert(Glucose, 'float'),
#             validate_and_convert(BloodPressure, 'int'),
#             validate_and_convert(SkinThickness, 'float'),
#             validate_and_convert(Insulin, 'float'),
#             validate_and_convert(BMI, 'float'),
#             validate_and_convert(DiabetesPedigreeFunction, 'float'),
#         ]

#         # Check if all inputs are valid
#         if None not in inputs:
#             try:
#                 # Ensure inputs match the model's expectations
#                 if len(inputs) == 9:
#                     # Make prediction using diabetes_model (assuming it's loaded)
#                     diab_prediction = diabetes_model.predict([inputs])

#                     if diab_prediction[0] == 1:
#                         diab_diagnosis = 'The person is diabetic'
#                     else:
#                         diab_diagnosis = 'The person is not diabetic'
#                 else:
#                     diab_diagnosis = 'The input features do not match the model expectations.'
#             except Exception as e:
#                 diab_diagnosis = f'An error occurred during prediction: {e}'
#                 st.error(diab_diagnosis)
#         else:
#             diab_diagnosis = 'Please enter valid numerical values for all fields.'
#             st.error(diab_diagnosis)

#         # Display the diagnosis message
#         st.success(diab_diagnosis)

# # Heart Disease Prediction
# if selected == 'Heart Disease Prediction':
#     st.title('Heart Prediction using ML')

#     # Getting the input data from the user
#     col1, col2, col3 = st.columns(3)

#     with col1:
#         age = st.text_input('Patient Age')

#     with col2:
#         sex = st.text_input('Sex')

#     with col3:
#         cp = st.text_input('Chest Pain')

#     with col1:
#         trestbps = st.text_input('Resting Blood Pressure')

#     with col2:
#         chol = st.text_input('Serum Cholesterol in mg/dl')

#     with col3:
#         fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)')

#     with col1:
#         restecg = st.text_input('Resting Electrocardiographic results')

#     with col2:
#         thalach = st.text_input('Max Heart Rate achieved')

#     with col3:
#         exang = st.text_input('Exercise Induced Angina (1 = yes; 0 = no)')

#     with col1:
#         oldpeak = st.text_input('ST depression induced by exercise')

#     with col2:
#         slope = st.text_input('Slope of the peak exercise ST segment')

#     with col3:
#         ca = st.text_input('Major vessels colored by fluoroscopy')

#     with col1:
#         thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversible defect')

#     # Assuming the 14th feature is "target" which should not be user-provided but required by the model
#     # Adding a placeholder for the 14th feature
#     with col2:
#         additional_feature = st.text_input('Additional Feature')

#     heart_diagnosis = ''

#     # Check if button is clicked
#     if st.button('Heart Disease Test Result'):
#         # Convert inputs to appropriate types
#         inputs = [
#             validate_and_convert(Age, 'int'),
#             validate_and_convert(sex, 'int'),
#             validate_and_convert(cp, 'int'),
#             validate_and_convert(trestbps, 'int'),
#             validate_and_convert(chol, 'int'),
#             validate_and_convert(fbs, 'int'),
#             validate_and_convert(restecg, 'int'),
#             validate_and_convert(thalach, 'int'),
#             validate_and_convert(exang, 'int'),
#             validate_and_convert(oldpeak, 'float'),
#             validate_and_convert(slope, 'int'),
#             validate_and_convert(ca, 'int'),
#             validate_and_convert(thal, 'int'),
#             validate_and_convert(additional_feature, 'float')  # Additional feature
#         ]

#         # Check if all inputs are valid
#         if None not in inputs:
#             try:
#                 # Ensure inputs match the model's expectations
#                 if len(inputs) == 14:  # There should be 14 features
#                     # Make prediction using heart_disease_model (assuming it's loaded)
#                     heart_prediction = heart_disease_model.predict([inputs])

#                     if heart_prediction[0] == 1:
#                         heart_diagnosis = 'The person has heart disease'
#                     else:
#                         heart_diagnosis = 'The person does not have heart disease'
#                 else:
#                     heart_diagnosis = 'The input features do not match the model expectations.'
#             except Exception as e:
#                 heart_diagnosis = f'An error occurred during prediction: {e}'
#                 st.error(heart_diagnosis)
#         else:
#             heart_diagnosis = 'Please enter valid numerical values for all fields.'
#             st.error(heart_diagnosis)

#         # Display the diagnosis message
#         st.success(heart_diagnosis)

# # Parkinsons Prediction
# if selected == "Parkinsons Prediction":
#     st.title("Parkinson's Disease Prediction using ML")

#     col1, col2, col3, col4, col5 = st.columns(5)

#     with col1:
#         fo = st.text_input('MDVP:Fo(Hz)')

#     with col2:
#         fhi = st.text_input('MDVP:Fhi(Hz)')

#     with col3:
#         flo = st.text_input('MDVP:Flo(Hz)')

#     with col4:
#         Jitter_percent = st.text_input('MDVP:Jitter(%)')

#     with col5:
#         Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

#     with col1:
#         RAP = st.text_input('MDVP:RAP')

#     with col2:
#         PPQ = st.text_input('MDVP:PPQ')

#     with col3:
#         DDP = st.text_input('Jitter:DDP')

#     with col4:
#         Shimmer = st.text_input('MDVP:Shimmer')

#     with col5:
#         Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

#     with col1:
#         APQ3 = st.text_input('Shimmer:APQ3')

#     with col2:
#         APQ5 = st.text_input('Shimmer:APQ5')

#     with col3:
#         APQ = st.text_input('MDVP:APQ')

#     with col4:
#         DDA = st.text_input('Shimmer:DDA')

#     with col5:
#         NHR = st.text_input('NHR')

#     with col1:
#         HNR = st.text_input('HNR')

#     with col2:
#         RPDE = st.text_input('RPDE')

#     with col3:
#         DFA = st.text_input('DFA')

#     with col4:
#         spread1 = st.text_input('spread1')

#     with col5:
#         spread2 = st.text_input('spread2')

#     with col1:
#         D2 = st.text_input('D2')

#     with col2:
#         PPE = st.text_input('PPE')

#     parkinsons_diagnosis = ''

#     if st.button("Parkinson's Test Result"):
#         inputs = [
#             validate_and_convert(fo, 'float'),
#             validate_and_convert(fhi, 'float'),
#             validate_and_convert(flo, 'float'),
#             validate_and_convert(Jitter_percent, 'float'),
#             validate_and_convert(Jitter_Abs, 'float'),
#             validate_and_convert(RAP, 'float'),
#             validate_and_convert(PPQ, 'float'),
#             validate_and_convert(DDP, 'float'),
#             validate_and_convert(Shimmer, 'float'),
#             validate_and_convert(Shimmer_dB, 'float'),
#             validate_and_convert(APQ3, 'float'),
#             validate_and_convert(APQ5, 'float'),
#             validate_and_convert(APQ, 'float'),
#             validate_and_convert(DDA, 'float'),
#             validate_and_convert(NHR, 'float'),
#             validate_and_convert(HNR, 'float'),
#             validate_and_convert(RPDE, 'float'),
#             validate_and_convert(DFA, 'float'),
#             validate_and_convert(spread1, 'float'),
#             validate_and_convert(spread2, 'float'),
#             validate_and_convert(D2, 'float'),
#             validate_and_convert(PPE, 'float'),
#         ]

#         # Check if all inputs are valid
#         if None not in inputs:
#             try:
#                 # Ensure inputs match the model's expectations
#                 if len(inputs) == 22:  # There should be 22 features
#                     # Make prediction using parkinsons_model (assuming it's loaded)
#                     parkinsons_prediction = parkinsons_model.predict([inputs])

#                     if parkinsons_prediction[0] == 1:
#                         parkinsons_diagnosis = "The person has Parkinson's disease"
#                     else:
#                         parkinsons_diagnosis = "The person does not have Parkinson's disease"
#                 else:
#                     parkinsons_diagnosis = 'The input features do not match the model expectations.'
#             except Exception as e:
#                 parkinsons_diagnosis = f'An error occurred during prediction: {e}'
#                 st.error(parkinsons_diagnosis)
#         else:
#             parkinsons_diagnosis = 'Please enter valid numerical values for all fields.'
#             st.error(parkinsons_diagnosis)

#         # Display the diagnosis message
#         st.success(parkinsons_diagnosis)

# # Cancer Prediction
# if selected == 'Cancer Prediction':
#     st.title('Cancer Prediction using ML')

#     # Getting the input data from the user
#     col1, col2, col3 = st.columns(3)

#     with col1:
#         mean_radius = st.text_input('mean radius')

#     with col2:
#         mean_texture = st.text_input('mean texture')

#     with col3:
#         mean_perimeter = st.text_input('mean perimeter')

#     with col1:
#         mean_area = st.text_input('mean area')

#     with col2:
#         mean_smoothness = st.text_input('mean smoothness')

#     with col3:
#         mean_compactness = st.text_input('mean compactness')

#     with col1:
#         mean_concavity = st.text_input('mean concavity')

#     with col2:
#         mean_concave_points = st.text_input('mean concave points')

#     with col3:
#         mean_symmetry = st.text_input('mean symmetry')

#     with col1:
#         mean_fractal_dimension = st.text_input('mean fractal dimension')

#     cancer_diagnosis = ''

#     if st.button('Cancer Test Result'):
#         # Convert inputs to appropriate types
#         inputs = [
#             validate_and_convert(mean_radius, 'float'),
#             validate_and_convert(mean_texture, 'float'),
#             validate_and_convert(mean_perimeter, 'float'),
#             validate_and_convert(mean_area, 'float'),
#             validate_and_convert(mean_smoothness, 'float'),
#             validate_and_convert(mean_compactness, 'float'),
#             validate_and_convert(mean_concavity, 'float'),
#             validate_and_convert(mean_concave_points, 'float'),
#             validate_and_convert(mean_symmetry, 'float'),
#             validate_and_convert(mean_fractal_dimension, 'float')
#         ]

#         # Check if all inputs are valid
#         if None not in inputs:
#             try:
#                 # Ensure inputs match the model's expectations
#                 if len(inputs) == 10:
#                     # Make prediction using cancer_model (assuming it's loaded)
#                     cancer_prediction = cancer_model.predict([inputs])

#                     if cancer_prediction[0] == 1:
#                         cancer_diagnosis = 'The person has cancer'
#                     else:
#                         cancer_diagnosis = 'The person does not have cancer'
#                 else:
#                     cancer_diagnosis = 'The input features do not match the model expectations.'
#             except Exception as e:
#                 cancer_diagnosis = f'An error occurred during prediction: {e}'
#                 st.error(cancer_diagnosis)
#         else:
#             cancer_diagnosis = 'Please enter valid numerical values for all fields.'
#             st.error(cancer_diagnosis)

#         # Display the diagnosis message
#         st.success(cancer_diagnosis)

    