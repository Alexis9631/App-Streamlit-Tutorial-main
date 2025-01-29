import streamlit as st
import pandas as pd
import altair as alt

# Load data
data_path = "data/example_data.csv"
df = pd.read_csv(data_path)

# Set the title of the app
st.title("Interactive Streamlit App")

# Display a text header
st.header("Exploring US Cities")

# Display some markdown text
st.markdown("""
This app showcases some interactive features of Streamlit, including data visualizations and maps.
""")

# Display the dataframe
st.subheader("City Data")
st.write(df)

# Create a slider for filtering by population
population_filter = st.slider("Select minimum population:", 0, int(df['population'].max()), 1000000)
filtered_df = df[df['population'] >= population_filter]

st.subheader(f"Cities with population greater than {population_filter}")
st.write(filtered_df)

# Create an Altair chart
st.subheader("Population of Cities")
chart = alt.Chart(filtered_df).mark_bar().encode(
    x='city',
    y='population',
    color='city'
).properties(width=600, height=400)
st.altair_chart(chart)

# Display a map using PyDeck
st.subheader("City Locations on Map")
st.map(filtered_df[['latitude', 'longitude']])

# Add a sidebar with interactive filters
st.sidebar.title("Filter Options")
selected_city = st.sidebar.selectbox("Select a city", df['city'].unique())
st.sidebar.write(f"You selected: {selected_city}")

city_data = df[df['city'] == selected_city]
st.sidebar.write(city_data)

# Run the Streamlit app using 'streamlit run app.py' in your terminal
