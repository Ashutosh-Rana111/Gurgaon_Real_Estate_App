import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Gurgaon Real Estate Analytics",
    page_icon="🏙️",
    layout="wide"
)

st.title("🏙️ Welcome to Gurgaon Real Estate Analytics")
st.markdown("---")

st.markdown("""
### Your Ultimate Guide to Property in Gurgaon
This platform helps you navigate the dynamic real estate market of Gurgaon using data-driven insights, machine learning, and live AI assistance.

**👈 Use the sidebar menu to navigate between our tools:**

#### 📊 1. Market Analysis
* Explore an interactive Geospatial Map showing price variations across different sectors.
* Understand price trends and market dynamics through detailed charts.
* Analyze the distribution of property types, BHKs, and luxury categories.
            
#### 💰 2. Price Predictor
* Estimate the current market value of flats and houses in various sectors.
* Outputs are adjusted for the latest 2026 market appreciation.
* Predictions are based on historical data, location, size, and amenities.

#### 🏘️ 3. Apartment Recommender
* **Distance-Based:** Enter a landmark and a radius to discover nearby apartments.
* **Similarity-Based:** Select an apartment you like, and our smart algorithm will recommend similar properties based on Location, Price, and Amenities.

#### 🤖 4. AI Assistant
* Ask questions about current property rates, infrastructure news, or future developments in Gurgaon.
* Powered by Google's Gemini 2.5 Flash, the assistant searches the live web to bring you the most up-to-date and accurate market information.
""")

st.markdown("---")
st.info("Built by Ashutosh | Powered by Machine Learning, GenAI & Streamlit")