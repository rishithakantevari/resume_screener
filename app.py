import streamlit as st
import pdfplumber
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', ' ', text)
    return text

st.title("Resume Screener")

uploaded_file = st.file_uploader("Upload your resume", type="pdf")
job_desc = st.text_area("Paste job description here")
submit = st.button("Analyze Resume")

if submit and uploaded_file and job_desc:
    with pdfplumber.open(uploaded_file) as pdf:
        resume_text = ""
        for page in pdf.pages:
            resume_text += page.extract_text()

    resume_clean = clean_text(resume_text)
    job_clean = clean_text(job_desc)

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_clean, job_clean])
    score = cosine_similarity(vectors[0], vectors[1])[0][0]

    st.write(f"### Match Score: {round(score * 100, 2)}%")

    stopwords = set(["a", "an", "the", "is", "are", "we", "for", "in",
                     "of", "and", "or", "to", "with", "have", "should",
                     "that", "this", "it", "as", "be", "on", "at", "by"])

    job_words = set(job_clean.split())
    resume_words = set(resume_clean.split())
    missing = job_words - resume_words - stopwords
    missing = set([w.strip() for w in missing])

    st.write("### Missing Keywords:")
    st.write(", ".join(missing))