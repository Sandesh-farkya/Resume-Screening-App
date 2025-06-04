import streamlit as st
import pickle
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from docx import Document
import fitz  # PyMuPDF

nltk.data.path.append("nltk_data")


# Load model and vectorizer
knn_model = pickle.load(open("knn_model.pkl", 'rb'))
tfidf_vectorizer = pickle.load(open("tfidf_vectorizer.pkl", 'rb'))

# Label mapping list
label_names = ['Advocate', 'Arts', 'Automation Testing', 'Blockchain', 'Business Analyst',
               'Civil Engineer', 'Data Science', 'Database', 'DevOps Engineer', 'DotNet Developer',
               'ETL Developer', 'Electrical Engineering', 'HR', 'Hadoop', 'Health and fitness',
               'Java Developer', 'Mechanical Engineer', 'Network Security Engineer', 'Operations Manager',
               'PMO', 'Python Developer', 'SAP Developer', 'Sales', 'Testing', 'Web Designing']



# Text cleaning function
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    return ' '.join(tokens)

# Extract text from docx
def extract_text_from_docx(file):
    doc = Document(file)
    return '\n'.join([para.text for para in doc.paragraphs])

# Extract text from pdf
def extract_text_from_pdf(file):
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        return "\n".join(page.get_text() for page in doc)

# Main app
def main():
    st.title("Resume Screening App")
    uploaded_file = st.file_uploader("Upload your resume", type=["pdf", "docx", "txt"])

    if uploaded_file is not None:
        file_type = uploaded_file.name.split('.')[-1].lower()

        try:
            if file_type == "pdf":
                resume_text = extract_text_from_pdf(uploaded_file)
            elif file_type == "docx":
                resume_text = extract_text_from_docx(uploaded_file)
            else:  # txt
                resume_bytes = uploaded_file.read()
                try:
                    resume_text = resume_bytes.decode("utf-8")
                except UnicodeDecodeError:
                    resume_text = resume_bytes.decode("latin-1", errors="ignore")

            st.text_area("Resume Text", resume_text, height=300)

            cleaned = clean_text(resume_text)
            input_feature = tfidf_vectorizer.transform([cleaned])
            prediction_id = knn_model.predict(input_feature)[0]
            predicted_label = label_names[prediction_id]
            st.success(f"Your resume is classified as: {predicted_label}")


        except Exception as e:
            st.error(f"Error processing file: {e}")

if __name__ == '__main__':
    main()
