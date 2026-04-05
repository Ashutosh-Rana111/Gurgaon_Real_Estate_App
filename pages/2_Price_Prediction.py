import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.set_page_config(page_title="Price Predictor", page_icon="💰", layout="wide")

st.title("💰 Gurgaon Property Price Predictor")
st.write("Fill in the details below to estimate the property price.")

@st.cache_resource
def load_model():
    with open('Gurgaon_Model.pkl', 'rb') as file:
        return pickle.load(file)

try:
    model = load_model()
except FileNotFoundError:
    st.error("Model file 'model.pkl' not found. Please ensure it is in the App folder.")
    st.stop()


col1, col2, col3 = st.columns(3)

with col1:
  
    property_type = st.selectbox('Property Type', ['house', 'flat'])

    sector = st.selectbox('Sector', ['sector 1', 'sohna road', 'manesar', 'gwal pahari', 'dwarka expressway', 'sector 2', 'sector 3', 'sector 4', 'sector 5', 'sector 6', 'sector 7', 'sector 8', 'sector 9', 'sector 10', 'sector 11', 'sector 12', 'sector 13', 'sector 14', 'sector 15', 'sector 17', 'sector 21', 'sector 22', 'sector 23', 'sector 24', 'sector 25', 'sector 26', 'sector 27', 'sector 28', 'sector 30', 'sector 31', 'sector 33', 'sector 36', 'sector 37', 'sector 37d', 'sector 38', 'sector 39', 'sector 40', 'sector 41', 'sector 43', 'sector 45', 'sector 46', 'sector 47', 'sector 48', 'sector 49', 'sector 50', 'sector 51', 'sector 52', 'sector 53', 'sector 54', 'sector 55', 'sector 56', 'sector 57', 'sector 58', 'sector 59', 'sector 60', 'sector 61', 'sector 62', 'sector 63', 'sector 63a', 'sector 65', 'sector 66', 'sector 67', 'sector 67a', 'sector 68', 'sector 69', 'sector 70', 'sector 70a', 'sector 71', 'sector 72', 'sector 73', 'sector 74', 'sector 76', 'sector 77', 'sector 78', 'sector 79', 'sector 80', 'sector 81', 'sector 82', 'sector 82a', 'sector 83', 'sector 84', 'sector 85', 'sector 86', 'sector 88', 'sector 88a', 'sector 89', 'sector 90', 'sector 91', 'sector 92', 'sector 93', 'sector 95', 'sector 99', 'sector 102', 'sector 103', 'sector 104', 'sector 105', 'sector 106', 'sector 107', 'sector 108', 'sector 109', 'sector 110', 'sector 111', 'sector 112', 'sector 113' ])
   
    built_up_area = st.number_input('Built-up Area (sq ft)', min_value=100, max_value=20000, value=2750)
    agePossession = st.selectbox('Age/Possession', ['New Property', 'Relatively New', 'Moderately Old', 'Old Property', 'Under Construction'])
    
with col2:
    bedRoom = st.number_input('Bedrooms', min_value=1, max_value=15, value=4)
    bathroom = st.number_input('Bathrooms', min_value=1, max_value=15, value=3)
    balcony = st.selectbox('Balconies', ['0', '1', '2', '3', '3+'])
    furnishing_type = st.selectbox('Furnishing Type', ['unfurnished', 'semifurnished', 'furnished'])

with col3:
    floor_category = st.selectbox('Floor Category', ['Low', 'Mid', 'High'])
    luxury_category = st.selectbox('Luxury Category', ['Low', 'Medium', 'High'])
    
    st.write("Additional Rooms")
    study_room = st.checkbox('Study Room')
    servant_room = st.checkbox('Servant Room')
    store_room = st.checkbox('Store Room')

#  PREDICTION BUTTON
if st.button('Predict Price'):
    if luxury_category == 'High':
        luxury_category = 'Low' 
    elif luxury_category == 'Low':
        luxury_category = 'High' 
    study_room_val = 1 if study_room else 0
    servant_room_val = 1 if servant_room else 0
    store_room_val = 1 if store_room else 0

    data = [[
        property_type, sector, bedRoom, bathroom, balcony, 
        agePossession, built_up_area, study_room_val, servant_room_val, 
        store_room_val, furnishing_type, floor_category, luxury_category
    ]]
    
    columns = [
        'property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
        'agePossession', 'built_up_area', 'study room', 'servant room', 'store room',
        'furnishing_type', 'floor_category', 'luxury_category'
    ]
    
    input_df = pd.DataFrame(data, columns=columns)
  
    st.write("Input Data Summary:")
    st.dataframe(input_df)

    # Predict
    try:
        prediction = np.expm1(model.predict(input_df)[0])
        st.success(f"Estimated Price Range: ₹ {1.47*prediction:.2f} Cr to ₹ {1.75*prediction:.2f} Cr") # Adjust currency/format based on your model output
    except Exception as e:
        st.error(f"Error making prediction: {e}")