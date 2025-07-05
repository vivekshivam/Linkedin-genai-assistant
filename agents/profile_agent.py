import os
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
openai_api_key = os.environ.get("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-4o", temperature=0.3)

def analyze_profile(profile_data):
    prompt = ChatPromptTemplate.from_template("""
You are an expert career coach. Carefully analyze this LinkedIn profile data and provide:
- A list of missing or weak information in the About, Experience, and Skills sections.
- Overall strengths and weaknesses.

Profile Data: {profile}
""")
    messages = prompt.format_messages(profile=profile_data)
    response = llm.invoke(messages)
    return response.content
