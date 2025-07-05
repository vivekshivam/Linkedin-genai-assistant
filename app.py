from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import fitz  # PyMuPDF

from agents.profile_agent import analyze_profile
from agents.jobfit_agent import job_fit_analysis
from agents.content_agent import enhance_profile_section
from agents.counseling_agent import career_counseling
from memory.memory_manager import update_memory, get_memory

st.set_page_config(page_title="LinkedIn GenAI Chat Assistant")
st.title("🔗 LinkedIn Optimizer & Career Guide")

memory = get_memory()

# Initialize session state
if "profile_data" not in st.session_state:
    st.session_state.profile_data = {}
if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = None
if "jobfit_result" not in st.session_state:
    st.session_state.jobfit_result = None
if "counseling_result" not in st.session_state:
    st.session_state.counseling_result = None

profile_pdf = st.file_uploader("Upload your LinkedIn Profile PDF:", type=["pdf"])

def extract_text_from_pdf(uploaded_file):
    text = ""
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

if profile_pdf and st.button("Analyze Profile"):
    with st.spinner("Reading uploaded profile..."):
        # Clear previous session data when new PDF is uploaded
        st.session_state.profile_data = {}
        st.session_state.analysis_result = None
        st.session_state.jobfit_result = None
        st.session_state.counseling_result = None

        profile_text = extract_text_from_pdf(profile_pdf)
        st.session_state.profile_data = {"about": profile_text}
    if st.session_state.profile_data:
        analysis = analyze_profile(st.session_state.profile_data)
        st.session_state.analysis_result = analysis
        update_memory("Uploaded Profile PDF", analysis)
    else:
        st.error("Could not read profile PDF. Try another file.")

if st.session_state.analysis_result:
    st.write("**Profile Analysis:**")
    st.write(st.session_state.analysis_result)

if st.session_state.profile_data:
    st.subheader("Job Fit Analysis")
    target_role_input = st.text_input("Enter target job role (e.g., Data Analyst)", key="target_role")

    if target_role_input and st.button("Analyze Job Fit"):
        fit_analysis = job_fit_analysis(st.session_state.profile_data, target_role_input)
        st.session_state.jobfit_result = fit_analysis
        update_memory(f"Target Role: {target_role_input}", fit_analysis)

    if st.session_state.jobfit_result:
        st.write("**Job Fit Analysis:**")
        st.write(st.session_state.jobfit_result)

    st.subheader("Enhance Profile Sections")
    section_text = st.text_area("Paste a profile section you want improved (e.g., your About section)")
    if section_text and target_role_input and st.button("Enhance Section"):
        enhanced = enhance_profile_section(section_text, target_role_input)
        update_memory(f"Enhance Section for {target_role_input}", enhanced)
        st.write("**Enhanced Section:**")
        st.write(enhanced)

    st.subheader("Career Counseling & Skill Gap Recommendations")
    if st.session_state.jobfit_result and target_role_input and st.button("Get Career Counseling"):
        counseling = career_counseling(st.session_state.jobfit_result)
        st.session_state.counseling_result = counseling
        update_memory(f"Career Counseling for {target_role_input}", counseling)

    if st.session_state.counseling_result:
        st.write("**Career Counseling & Skill Gap Recommendations:**")
        st.write(st.session_state.counseling_result)

if st.button("Clear All"):
    st.session_state.clear()
    st.experimental_rerun()


st.sidebar.title("📝 Chat Memory")
for msg in memory:
    st.sidebar.markdown(f"- **{msg['type'].title()}**: {msg['content']}")
