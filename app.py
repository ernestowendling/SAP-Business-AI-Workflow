import streamlit as st

st.title("SAP Business AI Workflow Prototype")

st.write(
    "This application checks invoice data against vendor "
    "and purchase-order records."
)

uploaded_file = st.file_uploader(
    "Upload an invoice in PDF format",
    type=["pdf"],
)

if uploaded_file is not None:
    st.success("Invoice uploaded successfully.")
    st.write(f"File name: {uploaded_file.name}")