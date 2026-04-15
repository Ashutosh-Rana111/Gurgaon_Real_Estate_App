# 🏙️ Gurgaon Real Estate Analytics & AI Assistant

#### A comprehensive end-to-end data science project that leverages Machine Learning and Generative AI to provide deep insights into the Gurgaon real estate market.

## 🚀 Live Demo

https://gurgaonrealestateapp.streamlit.app/

### 🔗 Related Projects
- This application is powered by a comprehensive machine learning pipeline developed in a separate project. The pipeline includes extensive data cleaning, advanced feature engineering, and robust model building, achieving **R² ≈ 0.90** using optimized ensemble models.

- It also integrates a hybrid recommendation system that suggests similar societies based on location proximity, price & configuration, and amenities, combining multiple similarity signals for more relevant results.

- The backend pipeline ensures that predictions and recommendations are data-driven, scalable, and aligned with real-world real estate patterns, making this application more than just a UI layer
- Check it out here  - https://github.com/Ashutosh-Rana111/Real_Estate_Project.git

---
## 🌟 Key Features

### 💰 1. Property Price Predictor

- Uses an XGBoost Regression model to estimate property values.

- Features Target Encoding for high-cardinality categorical data (Sectors).

- Adjusted for 2026 market appreciation to ensure realistic estimates.

## 📊 2. Interactive Market Analysis

- **Geospatial Mapping**: Interactive Plotly scatter maps showing price distribution across Gurgaon sectors.

- **Data Visualization**: Detailed charts analyzing BHK distributions, property types, and luxury scores.

## 🏘️ 3. Apartment Recommender

- **Landmark-based Search**: Find properties within a specific radius (km) of major Gurgaon landmarks.

- **Content-Based Filtering**: Uses Cosine Similarity to recommend similar apartments based on facilities, location, and price point.

## 🤖 4. AI Market Assistant (GenAI)

- Integrated `Gemini 2.5 Flash` model with Google Search Grounding.

- Provides live answers to real-time queries about infrastructure, new launches, and market news.

- Optimized for conciseness and token efficiency.

## 🛠️ Tech Stack

- Frontend: Streamlit

- Machine Learning: Scikit-Learn, XGBoost, Category Encoders

- Generative AI: Google GenAI SDK (Gemini 2.5 Flash)

- Data Handling: Pandas, NumPy

- Visualization: Plotly, Matplotlib, Seaborn

## 🔧 Local Setup

### Clone the repo:

git clone [https://github.com/Ashutosh-Rana111/Gurgaon_Real_Estate_App.git](https://github.com/Ashutosh-Rana111/Gurgaon_Real_Estate_App.git)


### Install dependencies:

pip install -r requirements.txt


### Set up API Key:
Create a `.streamlit/secrets.toml` file and add:

GEMINI_API_KEY = "your_google_api_key"


### Run the app:

streamlit run Gurgaon_Price_Predictor.py


👨‍💻 Author

Ashutosh Rana B.Tech Computer Science [www.linkedin.com/in/ashutosh-rana-7258432a7]
