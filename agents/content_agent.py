import os
from langchain_openai import ChatOpenAI  # updated import
from langchain.prompts import ChatPromptTemplate
openai_api_key = os.environ.get("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-4o", temperature=0.3)

def enhance_profile_section(section_text, target_role):
    prompt = ChatPromptTemplate.from_template("""
You are a professional resume and profile writer. Rewrite this LinkedIn profile section so it aligns better with industry best practices for the role of {role}.
Section: {section}
""")
    messages = prompt.format_messages(section=section_text, role=target_role)
    response = llm.invoke(messages)
    return response.content
