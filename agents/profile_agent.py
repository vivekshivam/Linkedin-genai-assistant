import os
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

openai_api_key = os.environ.get("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-4o", temperature=0.3)

def analyze_profile(profile_data):
    prompt = ChatPromptTemplate.from_messages([
        ("system", 
         "You are a senior career strategist and LinkedIn optimization expert. Your task is to deeply assess LinkedIn profile content and suggest improvements aligned with industry expectations."),
        ("user", 
        """Analyze the LinkedIn profile below and return insights in this format:

📋 **Section-Wise Evaluation**

🔹 About Section:
- Summary of content quality
- Missing or weak points
- Suggestions for improvement

🔹 Experience Section:
- Relevance and clarity
- Use of metrics, outcomes, or impact
- Weaknesses or vague parts

🔹 Skills Section:
- Any missing or outdated skills
- Alignment with modern job market

⚖️ **Overall Strengths**:
- Bullet points summarizing key positives

⚠️ **Overall Weaknesses**:
- Bullet points summarizing key gaps

🔧 **Profile Optimization Suggestions**:
- Actionable steps to improve visibility, clarity, and impact

Profile Data:
{profile}
""")
    ])
    
    messages = prompt.format_messages(profile=profile_data)
    response = llm.invoke(messages)
    return response.content
