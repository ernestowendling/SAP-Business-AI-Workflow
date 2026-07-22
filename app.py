import streamlit as st

from utils.parser import extract_text_from_pdf


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

    try:
        extracted_text = extract_text_from_pdf(uploaded_file)

        st.subheader("Extracted invoice text")

        if extracted_text:
            st.text_area(
                "Text found in the PDF",
                value=extracted_text,
                height=300,
            )
        else:
            st.warning(
                "No readable text was found in this PDF. "
                "The document may be a scanned image."
            )

    except Exception as error:
        st.error("The PDF could not be read.")
        st.write(f"Technical details: {error}")