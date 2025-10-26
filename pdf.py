import streamlit as st
import google.generativeai as genai
import PyPDF2

# Set up Gemini API key 
genai.configure(api_key="AIzaSyDgLgcbBs_8CuttAzMUOqdzJl56Uk4gqDs")

# Initialize Gemini model
model = genai.GenerativeModel("gemma-3-4b-it")

# Streamlit UI
st.title("📄 Chat with Your PDF (Gemini)")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    # Extract PDF text
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    pdf_text = ""
    for page in pdf_reader.pages:
        pdf_text += page.extract_text() or ""

    st.success("✅ PDF uploaded and text extracted!")

    query = st.text_input("Ask a question about your PDF:")

    if st.button("Ask"):
        if query:
            prompt = f"""
            You are a helpful assistant. Answer based on this PDF text:
            {pdf_text[:20000]}

            Question: {query}
            """
            response = model.generate_content(prompt)
            st.markdown("### 💬 Answer:")
            st.write(response.text)
        else:
            st.warning("Please enter a question.")

