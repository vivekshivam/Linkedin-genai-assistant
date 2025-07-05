from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
os.environ.get("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-4o", temperature=0.3)

def career_counseling(jobfit_result):
    prompt = ChatPromptTemplate.from_template("""
You are an experienced career counselor.
Based on the following job fit analysis, do these three things:
1) Identify key missing or weak skills.
2) Recommend specific skills or certifications to acquire.
3) Suggest at least 2 relevant courses (with example providers) or learning paths.

Job Fit Analysis:
{jobfit}
""")
    messages = prompt.format_messages(jobfit=jobfit_result)
    response = llm.invoke(messages)
    return response.content
