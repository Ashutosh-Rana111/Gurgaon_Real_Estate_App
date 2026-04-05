import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("data_viz1.csv")

df = load_data()

st.sidebar.header("Filters")

sector_list = ["All"] + sorted(df['sector'].dropna().unique().tolist())
selected_sector = st.sidebar.selectbox("Select Sector", sector_list)

bedroom_list = ["All"] + sorted(df['bedRoom'].dropna().unique().tolist())
selected_bedroom = st.sidebar.selectbox("Select Bedroom", bedroom_list)

filtered_df = df.copy()

if selected_sector != "All":
    filtered_df = filtered_df[filtered_df['sector'] == selected_sector]

if selected_bedroom != "All":
    filtered_df = filtered_df[filtered_df['bedRoom'] == selected_bedroom]

st.title("📊 Gurgaon Real Estate Dashboard")

# KPI METRICS 
col1, col2, col3 = st.columns(3)

col1.metric("Avg Price", f"{1.5 * int(filtered_df['price'].mean()):,} Crore")
col2.metric("Avg Price/sqft", f"{1.5 * int(filtered_df['price_per_sqft'].mean()):,} K")
col3.metric("Total Properties", len(filtered_df))

st.markdown("---")

#  MAP 
cols = ['price','price_per_sqft','built_up_area','latitude','longitude']

group_df = filtered_df.groupby('sector')[cols].mean().reset_index()

center = {
    "lat": group_df["latitude"].mean(),
    "lon": group_df["longitude"].mean()
}

st.subheader("📍 Property Map")

fig = px.scatter_map(
    group_df,
    lat="latitude",
    lon="longitude",
    color="price_per_sqft",
    size="built_up_area",
    size_max=15,
    zoom=11,
    center=center,
    map_style="open-street-map",
    text="sector",
    color_continuous_scale=px.colors.sequential.Plasma,
    opacity=0.7
)

fig.update_layout(height=700)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

#  AREA VS PRICE + BEDROOM DIST 
col1, col2 = st.columns(2)

with col1:
    fig = px.scatter(
        filtered_df,
        x="built_up_area",
        y="price",
        color="bedRoom",
        title="Area vs Price",
        color_discrete_sequence=px.colors.qualitative.Set1
    )
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    bedroom_counts = filtered_df['bedRoom'].value_counts().reset_index()
    bedroom_counts.columns = ['bedRoom', 'count']

    fig = px.bar(
        bedroom_counts,
        x='bedRoom',
        y='count',
        title="Bedroom Distribution",
        color='bedRoom',
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

#  BOX PLOT + CORRELATION 
col1, col2 = st.columns(2)

with col1:
    fig = px.box(
        filtered_df,
        x='bedRoom',
        y='price',
        title="Price Distribution by Bedroom"
    )
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    corr = filtered_df[['price','price_per_sqft','built_up_area','bedRoom']].corr()

    fig = px.imshow(
        corr,
        text_auto=True,
        title="Feature Correlation Heatmap"
    )
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)