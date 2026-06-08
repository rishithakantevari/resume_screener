import streamlit as st
import pdfplumber
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("Resume Screener")

uploaded_file = st.file_uploader("Upload your resume", type="pdf")
job_desc = st.text_area("Paste job description here")

if uploaded_file and job_desc:
    with pdfplumber.open(uploaded_file) as pdf:
        resume_text = ""
        for page in pdf.pages:
            resume_text += page.extract_text()

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, job_desc])
    score = cosine_similarity(vectors[0], vectors[1])[0][0]

    st.write(f"### Match Score: {round(score * 100, 2)}%")