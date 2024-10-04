import os
import streamlit as st
from dotenv import load_dotenv
from generate_email import EmailGenerator
from PyPDF2 import PdfReader

# Load environment variables
load_dotenv()

# Initialize the EmailGenerator
email_generator = EmailGenerator()

# Streamlit application layout
st.title("Career Catalyst")

# File uploader for job description
job_desc_file = st.file_uploader("Upload Job Description (Text File)", type=["txt"])

# File uploader for resume
resume_file = st.file_uploader("Upload Candidate Resume (PDF File)", type=["pdf"])

# Input section for candidate name
selected_candidate = st.text_input("Enter Candidate Name")

# Initialize variables for job description and resume text
job_description = ""
resume_text = ""

# Read job description from the uploaded file
if job_desc_file is not None:
    job_description = job_desc_file.read().decode("utf-8")
    st.text_area("Job Description", job_description, height=200)

# Read resume text from the uploaded PDF file
if resume_file is not None:
    pdf_reader = PdfReader(resume_file)
    resume_text = ""
    for page in pdf_reader.pages:
        resume_text += page.extract_text() + "\n"
    st.text_area("Resume Text", resume_text, height=200)

# Button to generate email
if st.button("Generate Email"):
    if selected_candidate and job_description and resume_text:
        try:
            # Generate email for the selected candidate
            email_content = email_generator.generate_email(selected_candidate, job_description, resume_text)
            st.subheader("Generated Email")
            st.write(email_content)
        except Exception as e:
            st.error(f"Error generating email: {e}")
    else:
        st.warning("Please fill in all fields before generating the email.")

if __name__ == "__main__":
    st.write("Application is running.")

