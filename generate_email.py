import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()


class EmailGenerator:
    def __init__(self):
        self.llm = ChatGroq(temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.1-70b-versatile")

    def generate_email(self, candidate_name, job_description, resume):
        # Prepare the email prompt
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ### RESUME CONTENT:
            {resume}

            ### INSTRUCTION:
            You are an HR representative at a company. Write a personalized email to {candidate_name} regarding the job mentioned above. 
            Highlight why the candidate is a strong fit for this position based on their resume. 
            Do not provide a preamble.
            ### EMAIL (NO PREAMBLE):
            """
        )

        # Invoke the model with the constructed prompt
        chain_email = prompt_email | self.llm
        response = chain_email.invoke(
            {"job_description": job_description, "resume": resume, "candidate_name": candidate_name})

        return response.content


if __name__ == "__main__":
    print("Email generator initialized.")
