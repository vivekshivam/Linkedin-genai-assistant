import os
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

openai_api_key = os.environ.get("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-4o", temperature=0.3)

def enhance_profile_section(section_text, target_role):
    prompt = ChatPromptTemplate.from_messages([
        ("system", """
You are an expert LinkedIn profile strategist and resume coach with 10+ years of experience crafting high-converting, ATS-friendly professional profiles.

Your goal is to rewrite the following LinkedIn section to:
- Be more aligned with the job role of {target_role}
- Highlight relevant accomplishments and impact
- Use action-driven language and power verbs
- Ensure clarity, conciseness, and professional tone
- Quantify results where possible
- Remove filler or redundant content

Make sure the tone is confident yet authentic, and the style follows top LinkedIn profile best practices. Avoid generic buzzwords and ensure the content reflects real, credible expertise.
"""),
        ("user", """
Current LinkedIn Section:
{section}

Please return only the professionally rewritten version of the section.
""")
    ])
    
    messages = prompt.format_messages(section=section_text, target_role=target_role)
    response = llm.invoke(messages)
    return response.content
