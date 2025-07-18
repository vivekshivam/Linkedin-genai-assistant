import os
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

openai_api_key = os.environ.get("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-4o", temperature=0.3)

def job_fit_analysis(profile_data, target_role):
    # Step 1: Generate a strong JD dynamically
    jd_prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a professional recruiter and domain expert."),
        ("user", 
        """Generate a detailed and realistic industry-standard job description (JD) for the following role:
        
Role: {role}

Include the following sections:
1. Job Summary (2–3 lines)
2. Key Responsibilities (bullet points)
3. Required Skills & Technologies (bullet points)
4. Preferred Qualifications (optional)
5. Soft Skills or Traits Ideal for this Role""")
    ])
    
    jd_response = llm.invoke(jd_prompt.format_messages(role=target_role))
    jd = jd_response.content

    # Step 2: Compare user profile to the generated JD
    comparison_prompt = ChatPromptTemplate.from_messages([
        ("system", 
         "You are a job fit analyst. You compare LinkedIn profiles to job descriptions and provide insights."),
        ("user",
        """Based on the LinkedIn profile and the job description below:

1️⃣ Assign a **Job Fit Score** between 0–100.
2️⃣ List at least 3–5 **missing or weak areas** compared to the JD.
3️⃣ Provide **brief suggestions** on how to close those gaps.

Return in this format:
---
📊 Job Fit Score: <number>

❌ Gaps/Weak Areas:
- ...
- ...

✅ Suggestions to Improve Fit:
- ...
- ...

🔗 Inputs:
LinkedIn Profile:
{profile}

Generated Job Description:
{jd}
""")
    ])

    messages = comparison_prompt.format_messages(profile=profile_data, jd=jd)
    response = llm.invoke(messages)
    return response.content
