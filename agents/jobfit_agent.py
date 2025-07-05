import os
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
openai_api_key = os.environ.get("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-4o", temperature=0.3)

def job_fit_analysis(profile_data, target_role):
    # Step 1: Dynamically generate a standard JD using OpenAI
    jd_prompt = ChatPromptTemplate.from_template("""
You are a professional recruiter. Write a standard industry job description (JD) for the role of {role}.
Include key skills, responsibilities, and qualifications.
""")
    jd_response = llm.invoke(jd_prompt.format_messages(role=target_role))
    jd = jd_response.content

    # Step 2: Compare the profile to the generated JD
    prompt = ChatPromptTemplate.from_template("""
You are a job fit analyst. Compare the given LinkedIn profile to the standard JD below.
- Provide a match score from 0-100.
- List the key missing or weak areas compared to the JD.

LinkedIn Profile: {profile}
Standard JD: {jd}
""")
    messages = prompt.format_messages(profile=profile_data, jd=jd)
    response = llm.invoke(messages)
    return response.content
