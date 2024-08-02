import streamlit as st
import pandas as pd
from io import BytesIO


# Function to convert an Excel file to CSV with semicolon delimiter
def convert_excel_to_csv(excel_file):
    excel_data = pd.read_excel(excel_file).dropna(how="all")  # Remove empty rows
    csv_buffer = BytesIO()
    excel_data.to_csv(csv_buffer, sep=";", index=False)
    csv_buffer.seek(0)
    return csv_buffer


# Streamlit app
st.subheader("Excel to CSV (semicolon delimiter)")

# File uploader for a single file
uploaded_file = st.file_uploader(label="Upload Excel file", type="xlsx")

# Display the file as a DataFrame and convert to CSV
if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.write(f"{uploaded_file.name} data:")
    st.write(df)

    csv_buffer = convert_excel_to_csv(uploaded_file)
    csv_text = csv_buffer.getvalue().decode("utf-8")
    csv_filename = uploaded_file.name.replace(".xlsx", ".csv")

    # Display the raw text data
    st.write("Converted CSV raw text data:")
    st.code(csv_text, language="csv")

    # Check if the last row starts with ;
    if csv_text.splitlines()[-1].startswith(";"):
        st.warning("Recheck the .XLSX file you have uploaded. Extra rows are present.")

    st.success("File has been converted.")
    st.download_button(
        label="✅ Download CSV with semicolons separator",
        data=csv_buffer,
        file_name=csv_filename,
        mime="text/csv",
        type="primary",
        use_container_width=True,
    )

else:
    st.write("Please upload an Excel file to convert.")
