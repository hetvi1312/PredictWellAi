import pickle
import streamlit as st
import os

image_path = os.path.join(os.getcwd(), 'image', '2.jpg')
image1_path = os.path.join(os.getcwd(), 'image', '5.jpg')
image2_path = os.path.join(os.getcwd(), 'image', '7.jpg')
image3_path = os.path.join(os.getcwd(), 'image', '8.jpg')
image4_path = os.path.join(os.getcwd(), 'image', '9.jpg')

st.set_page_config(page_title="PredictWellAi", layout="wide")

diabetes_model = pickle.load(open('saveModels/diabetes.sav', 'rb'))
heart_disease_model = pickle.load(open('saveModels/heart.sav', 'rb'))
parkinsons_model = pickle.load(open('saveModels/parkinsons.sav', 'rb'))
Cancer_model = pickle.load(open('saveModels/Cancer.sav', 'rb'))
Kidney_model = pickle.load(open('saveModels/Kidney.sav', 'rb'))

st.markdown(
    """
    <style>
    /* Hide Streamlit header */
    header {visibility: hidden;}

    /* Hide Streamlit footer */
    footer {visibility: hidden;}

    /* Custom navbar styling */
    .st-navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: #ffffff; /* White background */
        padding: 10px 20px; /* Adjust padding for aesthetics */
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        width: 100%;
        z-index: 1000;
        box-shadow: 0 4px 2px -2px gray;
    }

    .st-navbar .logo-text {
        font-size: 28px; /* Increased font size */
        font-weight: bold;
        color: #333; /* Text color */
    }

    .st-navbar .menu-items {
        display: flex;
        gap: 30px; /* Increased spacing between menu items */
    }

    .st-navbar .menu-items a {
        text-decoration: none;
        color: #333; /* Menu item color */
        font-size: 20px; /* Increased font size for menu items */
    }

    .st-navbar .menu-items a:hover {
        color: #007BFF; /* Hover color */
    }

    /* Increase tab font size */
    .stTabs [role="tablist"] [role="tab"] {
        font-size: 28px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""
    <div class="st-navbar">
        <div class="logo-text">PredictWellAi</div>
    </div>
    """, unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(
    ["Home", "Diabetes Prediction", "Heart Disease Prediction", "Parkinson's Prediction", "Cancer Prediction",
     "Kidney Disease Prediction", "About"])

with tab1:
    st.write("""
          ### Information about the Diseases:
    """)

    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(image_path, caption="Diabetes", width=None, use_column_width=True)
    with col2:
        st.markdown("""
               #### Diabetes
               Diabetes occurs when blood glucose, also called blood sugar, is too high. Symptoms include:
               - Urinating often
               - Feeling very thirsty
               - Extreme fatigue
               - Blurry vision
           """)
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(image1_path, caption="Heart Disease", width=None, use_column_width=True)
    with col2:
        st.markdown("""
                  #### Heart disease
                  Heart disease refers to a range of conditions that affect the heart. Symptoms and signs can vary but commonly include:
                  - Chest pain or discomfort
                  - Shortness of breath
                  - Fatigue
                  - Swelling in the legs, ankles, or feet
              """)
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(image2_path, caption="Breast Cancer Disease", width=None, use_column_width=True)
    with col2:
        st.markdown("""
                     #### Breast Cancer Disease
                     Breast cancer forms in the cells of the breasts and is the most common cancer in women after skin cancer. Symptoms include:
                     - A breast lump or thickening that feels different from the surrounding tissue
                     - Change in the size, shape, or appearance of a breast
                     - Changes to the skin over the breast, such as dimpling
                 """)

    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(image3_path, caption="Chronic Kidney Disease", use_column_width=True)
    with col2:
        st.markdown("""
                    #### Chronic Kidney Disease
                    Chronic kidney disease describes the gradual loss of kidney function. Symptoms include:
                    - Nausea
                    - Vomiting
                    - Fatigue and weakness
                    - Muscle twitches and cramps
                    """)

    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(image4_path, caption="Parkinson’s Disease", use_column_width=True)
    with col2:
        st.markdown("""
                    #### Parkinson’s Disease
                    Parkinson’s Disease is a neurodegenerative disorder that affects movement. Symptoms include:
                    - Tremors (shaking)
                    - Rigidity (muscle stiffness)
                    - Postural instability (balance issues)
                    - Sleep disturbances
                    - Depression
                    - Cognitive changes

                    """)

with tab2:
    st.write('## Diabetes Prediction')
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies', placeholder='Enter number of pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level', placeholder='Enter glucose level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value', placeholder='Enter blood pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value', placeholder='Enter skin thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level', placeholder='Enter insulin level')
    with col3:
        BMI = st.text_input('BMI value', placeholder='Enter BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value',
                                                 placeholder='Enter diabetes pedigree function value')
    with col2:
        Age = st.text_input('Age of the Person', placeholder='Enter age')

    diab_diagnosis = ''

    # Predicting the result when the button is clicked
    if st.button('Diabetes Test Result'):
        if all([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]):
            try:
                # Convert input data to floats and make the prediction
                input_data = [
                    float(Pregnancies), float(Glucose), float(BloodPressure),
                    float(SkinThickness), float(Insulin), float(BMI),
                    float(DiabetesPedigreeFunction), float(Age)
                ]
                diab_prediction = diabetes_model.predict([input_data])
                diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'
                st.success(diab_diagnosis)
            except ValueError:
                st.error("Please enter valid numerical values for all fields.")
        else:
            st.warning("Please fill in all the fields.")

with tab3:
    st.write('## Heart Disease Prediction')
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age', placeholder='Enter age')
    with col2:
        sex = st.text_input('Sex', placeholder='Enter sex')
    with col3:
        cp = st.text_input('Chest Pain types', placeholder='Enter chest pain types')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure', placeholder='Enter resting blood pressure')
    with col2:
        chol = st.text_input('Serum Cholesterol in mg/dl', placeholder='Enter serum cholesterol level')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl', placeholder='Enter fasting blood sugar level')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results', placeholder='Enter resting ECG results')
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved', placeholder='Enter maximum heart rate')
    with col3:
        exang = st.text_input('Exercise Induced Angina', placeholder='Enter exercise induced angina')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise', placeholder='Enter ST depression')
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment', placeholder='Enter slope of ST segment')
    with col3:
        ca = st.text_input('Major vessels colored by fluoroscopy', placeholder='Enter number of major vessels')
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversible defect',
                             placeholder='Enter thal value')

    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        if all([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]):
            try:
                # Convert input data to floats and make the prediction
                input_data = [
                    float(age), float(sex), float(cp), float(trestbps), float(chol), float(fbs),
                    float(restecg), float(thalach), float(exang), float(oldpeak), float(slope),
                    float(ca), float(thal)
                ]
                heart_prediction = heart_disease_model.predict([input_data])
                heart_diagnosis = 'The person is at risk of heart disease' if heart_prediction[
                                                                                  0] == 1 else 'The person is not at risk of heart disease'
                st.success(heart_diagnosis)
            except ValueError:
                st.error("Please enter valid numerical values for all fields.")
        else:
            st.warning("Please fill in all the fields.")

with tab4:
    st.write('## Parkinson’s Prediction')
    col1, col2 = st.columns(2)
    with col1:
        MDVP_Fo = st.text_input('MDVP_Fo', placeholder='Enter MDVP_Fo value')
    with col2:
        MDVP_Fhi = st.text_input('MDVP_Fhi', placeholder='Enter MDVP_Fhi value')
    with col1:
        MDVP_Flo = st.text_input('MDVP_Flo', placeholder='Enter MDVP_Flo value')
    with col2:
        MDVP_Jitter = st.text_input('MDVP_Jitter', placeholder='Enter MDVP_Jitter value')
    with col1:
        MDVP_Shimmer = st.text_input('MDVP_Shimmer', placeholder='Enter MDVP_Shimmer value')
    with col2:
        MDVP_APQ3 = st.text_input('MDVP_APQ3', placeholder='Enter MDVP_APQ3 value')
    with col1:
        MDVP_APQ5 = st.text_input('MDVP_APQ5', placeholder='Enter MDVP_APQ5 value')
    with col2:
        MDVP_DF = st.text_input('MDVP_DF', placeholder='Enter MDVP_DF value')

    parkinsons_diagnosis = ''
    if st.button('Parkinson’s Test Result'):
        if all([MDVP_Fo, MDVP_Fhi, MDVP_Flo, MDVP_Jitter, MDVP_Shimmer, MDVP_APQ3, MDVP_APQ5, MDVP_DF]):
            try:
                # Convert input data to floats and make the prediction
                input_data = [
                    float(MDVP_Fo), float(MDVP_Fhi), float(MDVP_Flo), float(MDVP_Jitter),
                    float(MDVP_Shimmer), float(MDVP_APQ3), float(MDVP_APQ5), float(MDVP_DF)
                ]
                parkinsons_prediction = parkinsons_model.predict([input_data])
                parkinsons_diagnosis = 'The person has Parkinson’s Disease' if parkinsons_prediction[
                                                                                   0] == 1 else 'The person does not have Parkinson’s Disease'
                st.success(parkinsons_diagnosis)
            except ValueError:
                st.error("Please enter valid numerical values for all fields.")
        else:
            st.warning("Please fill in all the fields.")

with tab5:
    st.write('## Cancer Prediction')
    col1, col2 = st.columns(2)
    with col1:
        radius_mean = st.text_input('Radius Mean', placeholder='Enter radius mean')
    with col2:
        texture_mean = st.text_input('Texture Mean', placeholder='Enter texture mean')
    with col1:
        perimeter_mean = st.text_input('Perimeter Mean', placeholder='Enter perimeter mean')
    with col2:
        area_mean = st.text_input('Area Mean', placeholder='Enter area mean')
    with col1:
        smoothness_mean = st.text_input('Smoothness Mean', placeholder='Enter smoothness mean')
    with col2:
        compactness_mean = st.text_input('Compactness Mean', placeholder='Enter compactness mean')
    with col1:
        concavity_mean = st.text_input('Concavity Mean', placeholder='Enter concavity mean')
    with col2:
        concave_points_mean = st.text_input('Concave Points Mean', placeholder='Enter concave points mean')
    with col1:
        symmetry_mean = st.text_input('Symmetry Mean', placeholder='Enter symmetry mean')
    with col2:
        fractal_dimension_mean = st.text_input('Fractal Dimension Mean', placeholder='Enter fractal dimension mean')

    cancer_diagnosis = ''
    if st.button('Cancer Test Result'):
        if all([radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean,
                compactness_mean, concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean]):
            try:
                # Convert input data to floats and make the prediction
                input_data = [
                    float(radius_mean), float(texture_mean), float(perimeter_mean),
                    float(area_mean), float(smoothness_mean), float(compactness_mean),
                    float(concavity_mean), float(concave_points_mean), float(symmetry_mean),
                    float(fractal_dimension_mean)
                ]
                cancer_prediction = Cancer_model.predict([input_data])
                cancer_diagnosis = 'The person has cancer' if cancer_prediction[
                                                                  0] == 1 else 'The person does not have cancer'
                st.success(cancer_diagnosis)
            except ValueError:
                st.error("Please enter valid numerical values for all fields.")
        else:
            st.warning("Please fill in all the fields.")

with tab6:
    st.write('## Kidney Disease Prediction')
    col1, col2 = st.columns(2)
    with col1:
        age1 = st.text_input('Age1', placeholder='Enter age')
    with col2:
        blood_pressure = st.text_input('Blood Pressure', placeholder='Enter blood pressure')
    with col1:
        specific_gravity = st.text_input('Specific Gravity', placeholder='Enter specific gravity')
    with col2:
        albumin = st.text_input('Albumin', placeholder='Enter albumin level')
    with col1:
        sugar = st.text_input('Sugar', placeholder='Enter sugar level')
    with col2:
        red_blood_cells = st.text_input('Red Blood Cells', placeholder='Enter number of red blood cells')
    with col1:
        pus_cell = st.text_input('Pus Cell', placeholder='Enter pus cell count')
    with col2:
        pus_cell_clumps = st.text_input('Pus Cell Clumps', placeholder='Enter pus cell clumps count')
    with col1:
        bacteria = st.text_input('Bacteria', placeholder='Enter bacteria count')
    with col2:
        blood_glucose_random = st.text_input('Blood Glucose Random', placeholder='Enter blood glucose random value')

    kidney_diagnosis = ''
    if st.button('Kidney Disease Test Result'):
        if all([age1, blood_pressure, specific_gravity, albumin, sugar, red_blood_cells,
                pus_cell, pus_cell_clumps, bacteria, blood_glucose_random]):
            try:
                # Convert input data to floats and make the prediction
                input_data = [
                    float(age1), float(blood_pressure), float(specific_gravity), float(albumin),
                    float(sugar), float(red_blood_cells), float(pus_cell), float(pus_cell_clumps),
                    float(bacteria), float(blood_glucose_random)
                ]
                kidney_prediction = Kidney_model.predict([input_data])
                kidney_diagnosis = 'The person has kidney disease' if kidney_prediction[
                                                                          0] == 1 else 'The person does not have kidney disease'
                st.success(kidney_diagnosis)
            except ValueError:
                st.error("Please enter valid numerical values for all fields.")
        else:
            st.warning("Please fill in all the fields.")

with tab7:
    st.write('## About')
    st.write("""

    PredictWellAi is a comprehensive platform leveraging machine learning and AI technologies to offer accurate predictions for multiple diseases. We are committed to providing users with reliable and accessible health insights based on advanced analytical models.

    ### Our Mission
    Our mission is to empower individuals with knowledge about their health through cutting-edge technology. We aim to assist healthcare providers and patients by providing quick, accurate assessments, facilitating early detection, and improving overall health outcomes.

    ### Our Models:
    - **Diabetes Model:** Predicts the likelihood of diabetes.
    - **Heart Disease Model:** Assesses the risk of heart disease.
    - **Parkinson’s Model:** Detects the presence of Parkinson’s Disease.
    - **Cancer Model:** Identifies potential cancer.
    - **Kidney Disease Model:** Evaluates the risk of kidney disease.
    ### Features
    - **Multi-Disease Prediction**: We cover a range of diseases including Diabetes, Heart Disease, Parkinson's, Cancer, and Kidney Disease.
    - **User-Friendly Interface**: Our platform is designed to be intuitive and accessible to users of all backgrounds.
    - **Secure & Confidential**: We prioritize your privacy and ensure that all data is handled securely.

    ### How It Works
    1. **Input Data**: Users enter relevant health data points.
    2. **Model Analysis**: Our models analyze the data to predict the likelihood of a particular disease.
    3. **Results**: Receive immediate feedback on your health status.

    **Disclaimer**: PredictWellAi is not a substitute for professional medical advice, diagnosis, or treatment. Always consult with a healthcare provider for medical advice.
    """)


