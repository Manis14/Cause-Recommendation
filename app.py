from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from Backend import DataProcessing
from Backend.DataProcessing import prediction

app = Flask(__name__)

# Symptom dictionary
symptom_dict = {
    'itching': 0, 'skin_rash': 1, 'nodal_skin_eruptions': 2, 'continuous_sneezing': 3, 'shivering': 4, 'chills': 5,
    'joint_pain': 6, 'stomach_pain': 7, 'acidity': 8, 'ulcers_on_tongue': 9, 'muscle_wasting': 10, 'vomiting': 11,
    'burning_micturition': 12, 'spotting_urination': 13, 'fatigue': 14, 'weight_gain': 15, 'anxiety': 16,
    'cold_hands_and_feets': 17, 'mood_swings': 18, 'weight_loss': 19, 'restlessness': 20, 'lethargy': 21,
    'patches_in_throat': 22, 'irregular_sugar_level': 23, 'cough': 24, 'high_fever': 25, 'sunken_eyes': 26,
    'breathlessness': 27, 'sweating': 28, 'dehydration': 29, 'indigestion': 30, 'headache': 31, 'yellowish_skin': 32,
    'dark_urine': 33, 'nausea': 34, 'loss_of_appetite': 35, 'pain_behind_the_eyes': 36, 'back_pain': 37,
    'constipation': 38, 'abdominal_pain': 39, 'diarrhoea': 40, 'mild_fever': 41, 'yellow_urine': 42,
    'yellowing_of_eyes': 43, 'acute_liver_failure': 44, 'fluid_overload': 45, 'swelling_of_stomach': 46,
    'swelled_lymph_nodes': 47, 'malaise': 48, 'blurred_and_distorted_vision': 49, 'phlegm': 50, 'throat_irritation': 51,
    'redness_of_eyes': 52, 'sinus_pressure': 53, 'runny_nose': 54, 'congestion': 55, 'chest_pain': 56,
    'weakness_in_limbs': 57, 'fast_heart_rate': 58, 'pain_during_bowel_movements': 59, 'pain_in_anal_region': 60,
    'bloody_stool': 61, 'irritation_in_anus': 62, 'neck_pain': 63, 'dizziness': 64, 'cramps': 65, 'bruising': 66,
    'obesity': 67, 'swollen_legs': 68, 'swollen_blood_vessels': 69, 'puffy_face_and_eyes': 70, 'enlarged_thyroid': 71,
    'brittle_nails': 72, 'swollen_extremeties': 73, 'excessive_hunger': 74, 'extra_marital_contacts': 75,
    'drying_and_tingling_lips': 76, 'slurred_speech': 77, 'knee_pain': 78, 'hip_joint_pain': 79, 'muscle_weakness': 80,
    'stiff_neck': 81, 'swelling_joints': 82, 'movement_stiffness': 83, 'spinning_movements': 84, 'loss_of_balance': 85,
    'unsteadiness': 86, 'weakness_of_one_body_side': 87, 'loss_of_smell': 88, 'bladder_discomfort': 89,
    'foul_smell_of_urine': 90, 'continuous_feel_of_urine': 91, 'passage_of_gases': 92, 'internal_itching': 93,
    'toxic_look_(typhos)': 94, 'depression': 95, 'irritability': 96, 'muscle_pain': 97, 'altered_sensorium': 98,
    'red_spots_over_body': 99, 'belly_pain': 100, 'abnormal_menstruation': 101, 'dischromic_patches': 102,
    'watering_from_eyes': 103, 'increased_appetite': 104, 'polyuria': 105, 'family_history': 106, 'mucoid_sputum': 107,
    'rusty_sputum': 108, 'lack_of_concentration': 109, 'visual_disturbances': 110, 'receiving_blood_transfusion': 111,
    'receiving_unsterile_injections': 112, 'coma': 113, 'stomach_bleeding': 114, 'distention_of_abdomen': 115,
    'history_of_alcohol_consumption': 116, 'fluid_overload.1': 117, 'blood_in_sputum': 118, 'prominent_veins_on_calf': 119,
    'palpitations': 120, 'painful_walking': 121, 'pus_filled_pimples': 122, 'blackheads': 123, 'scurring': 124,
    'skin_peeling': 125, 'silver_like_dusting': 126, 'small_dents_in_nails': 127, 'inflammatory_nails': 128,
    'blister': 129, 'red_sore_around_nose': 130, 'yellow_crust_ooze': 131
}

Symptoms_names = [symptom.replace('_', ' ').capitalize() for symptom in symptom_dict.keys()]

@app.route('/')
def home():
    """
    Renders the home page with a list of symptom names.
    """
    return render_template('index.html', Symptoms_names=Symptoms_names, prediction = False)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Renders the login page and handles login logic.
    """
    if request.method == 'POST':
        # Add login logic here
        pass
    return render_template('login.html')

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    """
    Renders the registration page and handles user registration.
    """
    if request.method == 'POST':
        # Add registration logic here
        pass
    return render_template('registration.html')

@app.route('/process-symptoms', methods=['POST'])
def process_symptoms():
    """
    Processes input symptoms, predicts disease, and handles warnings or errors.
    """
    action = request.form.get('action')  # Check if the button was clicked
    selected_symptoms = request.form.getlist('symptoms')  # Get selected symptoms as a list
    warning_message = ""
    predicted_disease = ""

    if action == 'submit_symptoms':
        if selected_symptoms:
            # Convert selected symptoms to their corresponding numeric values
            selected_symptoms = ', '.join(selected_symptoms)

            # Call the DataProcessing module to predict the disease
            prediction_result = DataProcessing.prediction(selected_symptoms)

            # Handle warnings and predicted diseases
            if prediction_result:
                predicted_disease = prediction_result.strip()
            else:
                predicted_disease = "No Disease Detected"
            return render_template(
                'index.html',
                prediction=predicted_disease,
                warning_message = False,
                Symptoms_names=Symptoms_names,  # Retain dropdown options
                selected_symptoms= selected_symptoms
            )
        else:
            # warning_message = "Please select symptoms to proceed."
            return render_template(
                'index.html',
                warning_message= True,
                Symptoms_names=Symptoms_names  # Retain dropdown options
            )

    # Default return in case no action
    return render_template('index.html', Symptoms_names=Symptoms_names)

@app.route('/disease-details')
def disease_details():
    """
    Render details of a predicted disease.
    """
    disease_name = request.args.get('disease')
    if not disease_name:
        return "No disease specified", 400  # Handle case where no disease is provided
    # Add logic to fetch and display disease details
    Definition, Workout, Diet, Precaution, Medication = DataProcessing.To_know_Your_Disease(disease_name)
    disease_info = {
        "Definition": "Detailed definition of the disease.",
        "Workout": "Recommended workout routines.",
        "Diet": "Suggested diet plan.",
        "Precaution": "Precautionary measures to take.",
        "Medication": "Common medications prescribed."
    }

    return render_template('disease_details.html', disease_name=disease_name, definition=Definition, workout=Workout,
                           diet=Diet, precaution=Precaution, medication=Medication)

if __name__ == '__main__':
    app.run(debug=True)
