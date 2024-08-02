import streamlit as st
import pandas as pd
import os
from io import BytesIO


# Function to convert an Excel file to CSV with semicolon delimiter
def convert_excel_to_csv(excel_file):
    excel_data = pd.read_excel(excel_file)
    csv_buffer = BytesIO()
    excel_data.to_csv(csv_buffer, sep=";", index=False)
    csv_buffer.seek(0)
    return csv_buffer


# Streamlit app
st.title("Excel to CSV Converter")

# File uploader for multiple files
uploaded_files = st.file_uploader(
    "Upload Excel files", type="xlsx", accept_multiple_files=True
)

if uploaded_files:
    for uploaded_file in uploaded_files:
        csv_buffer = convert_excel_to_csv(uploaded_file)
        csv_filename = os.path.splitext(uploaded_file.name)[0] + ".csv"
        st.download_button(
            label=f"Download {csv_filename}",
            data=csv_buffer,
            file_name=csv_filename,
            mime="text/csv",
        )
    st.success("All files have been converted.")
else:
    st.write("Please upload Excel files to convert.")