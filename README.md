# Symptom-based Disease Prediction Application

A Flask-based web application that allows users to input symptoms and receive a predicted disease along with helpful information about the disease, including workout routines, diet suggestions, precautions, and medications.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Routes](#routes)

## Introduction
This web application uses a predefined set of symptoms and predicts the disease based on user input. After the prediction, it provides relevant information regarding the disease such as its definition, recommended workout routines, dietary plans, precautionary measures, and medications.

## Features
- **Symptom Selection:** Users can select multiple symptoms to predict the possible disease.
- **Disease Prediction:** The application predicts the disease based on the symptoms.
- **Disease Information:** Provides detailed information about the predicted disease.
- **User Registration/Login:** Handles user registration and login functionality.

## Technologies Used
- **Backend:** Flask, Python
- **Frontend:** HTML, CSS, JavaScript (via Flask templating)
- **Libraries:** Pandas, NumPy
- **Data Handling:** Backend module `DataProcessing.py` handles data processing and prediction logic.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/repository-name.git
    cd repository-name
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Windows: venv\Scripts\activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask application:
    ```bash
    python app.py
    ```

5. Navigate to `http://127.0.0.1:5000/` in your browser.

## Usage
1. **Home Page:** Select symptoms from the dropdown, click "Submit," and get a predicted disease.
2. **Login/Registration:** The application also supports login and registration for users.
3. **Disease Details:** After prediction, navigate to the "Disease Details" page for more in-depth information about the disease.

## Routes
- `/`: Home page for symptom selection and disease prediction.
- `/login`: User login page.
- `/registration`: User registration page.
- `/process-symptoms`: Processes the symptoms selected and returns the predicted disease.
- `/disease-details`: Provides detailed information on the predicted disease.


---

**Note:** Please switch to the `master` branch to access the latest stable version of the project.
