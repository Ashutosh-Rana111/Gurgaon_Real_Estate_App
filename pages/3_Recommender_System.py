import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.set_page_config(page_title="Apartments Recommender", page_icon="🏘️", layout="wide")
st.title("🏘️ Apartment Recommender")

# 1. CACHE THE DATA LOADING
@st.cache_data
def load_data():
    location_df = pickle.load(open('location_distance.pkl', 'rb'))
    cos_sim_Loc = pickle.load(open('cos_sim_Loc', 'rb'))
    cos_sim_Facility = pickle.load(open('cos_sim_Facility', 'rb'))
    cos_sim_Price = pickle.load(open('cos_sim_Price', 'rb'))
    
    cosine_sim_matrix = 0.5 * cos_sim_Facility + 0.8 * cos_sim_Price + 1.0 * cos_sim_Loc
    
    return location_df, cosine_sim_matrix

try:
    location_df, cosine_sim_matrix = load_data()
except FileNotFoundError:
    st.error("Pickle files missing. Please ensure all 4 files are in the App folder.")
    st.stop()


#SECTION 1: DISTANCE RECOMMENDER
st.header('📍 Discover by Location and Radius')
col1, col2 = st.columns(2)

with col1:
    exclude = ['AIIMS', 'AIIMS Jhajjar']
    landmark_list = sorted(location_df.columns.to_list())
    filtered_list = [loc for loc in landmark_list if loc not in exclude]
    selected_location = st.selectbox('Select a Landmark', filtered_list)

with col2:
    radius = st.number_input('Radius (in km)', min_value=0.5, max_value=60.0, value=15.0, step=1.0)

if st.button('Search Nearby'):
    result_ser = location_df[location_df[selected_location] < radius * 1000][selected_location].sort_values()
    
    if result_ser.empty:
        st.warning(f"No apartments found within {radius} km of {selected_location}.")
    else:
        res_df = pd.DataFrame({
            "Apartment": result_ser.index,
            "Distance (km)": (result_ser.values / 1000).round(2)
        })
        st.dataframe(res_df, hide_index=True)

st.markdown("---")

#SECTION 2: SIMILARITY RECOMMENDER
st.header('🏢 Recommend Similar Apartments')

def recommend_properties_with_scores(property_name, top_n=6):

    sim_scores = list(enumerate(cosine_sim_matrix[location_df.index.get_loc(property_name)]))

    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    top_indices = [i[0] for i in sorted_scores[1:top_n+1]]
    top_scores = [i[1] for i in sorted_scores[1:top_n+1]]
    
    top_properties = location_df.index[top_indices].tolist()
    
    recommendations_df = pd.DataFrame({
        'Property Name': top_properties,
        'Similarity Score': np.round(top_scores, 3)
    })
    
    return recommendations_df

selected_apartment = st.selectbox('Select an apartment you like', sorted(location_df.index.to_list()))

if st.button('Recommend'):
    recommendation_df = recommend_properties_with_scores(selected_apartment, top_n=6)
    
    final_recs = recommendation_df[recommendation_df['Similarity Score'] > 0]
    
    if final_recs.empty:
         st.warning("No highly similar properties found.")
    else:
         st.dataframe(final_recs, hide_index=True)

# SECTION 3: HOW IT WORKS 
st.subheader("🧠 How does our recommendation engine work?")
st.info("""
When you select an apartment, our smart algorithm compares it against hundreds of others based on three carefully weighted factors:

* 📍 **Location (Highest Priority):** We look for properties geographically closest to your choice.
* 💰 **Price Dynamics (High Priority):** We match you with properties that fall within a similar budget and pricing bracket.
* 🏊 **Amenities & Facilities (Medium Priority):** We ensure the recommended apartments offer a comparable lifestyle, matching features like gyms, pools, and security.
""")
