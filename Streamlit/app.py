import streamlit as st
import pandas as pd
import numpy as np

st.title("DataFrame Display Example")

# Display a simple text message
st.write("Simple text")

# Create a sample DataFrame
df = pd.DataFrame({
    "Column 1": [1, 2, 3, 4, 5],
    "Column 2": ["A", "B", "C", "D", "E"],
    "Column 3": [10.5, 20.5, 30.5, 40.5, 50.5]
})

# Display the DataFrame
st.write("DataFrame with default settings:")
st.write(df)

# Line chart
chart_data = pd.DataFrame({
    "x": np.arange(1, 11),
    "y": np.random.randint(1, 100, size=10)
})
st.write("Line chart with default settings:")
st.line_chart(chart_data.set_index("x"))