import os
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

openai_api_key = os.environ.get("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-4o", temperature=0.3)

def career_counseling(jobfit_result):
    prompt = ChatPromptTemplate.from_messages([
        ("system", 
         "You are a seasoned career coach and talent strategist with deep industry insights. "
         "Based on the user's job fit analysis, your goal is to provide a highly personalized and actionable growth roadmap."),
        
        ("user", 
        """Analyze the following Job Fit Report and do the following:

1️⃣ Identify 3–5 **key skill gaps or weak areas** the candidate needs to improve.
2️⃣ Recommend **specific technical or soft skills** the user should acquire.
3️⃣ Suggest at least **two professional certifications or courses** (mention platforms like Coursera, Udemy, etc.) that directly address these gaps.
4️⃣ Conclude with 2–3 **career tips** tailored to someone targeting this job role.

Output in this format:
---
🔍 Skill Gaps:
- ...
- ...

📚 Skill Recommendations:
- ...
- ...

🎓 Suggested Courses/Certifications:
- [Course Name] – [Platform] – [Why it helps]

💡 Career Tips:
- ...
- ...

Job Fit Report:
{jobfit}
""")
    ])

    messages = prompt.format_messages(jobfit=jobfit_result)
    response = llm.invoke(messages)
    return response.content
