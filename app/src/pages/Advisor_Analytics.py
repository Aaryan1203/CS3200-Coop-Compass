import streamlit as st
from modules.nav import SideBarLinks
from utils.frontend_routes import get_students_for_advisor, get_sent_job_listings
from utils.style_utils import load_css

# Set Streamlit page configuration
st.set_page_config(
    layout="wide",
    page_title="Advisor Analytics",
    page_icon="📊"
)

# Apply custom CSS
#load_css("./styles/advisor_analytics_styles.css")

# Retrieve Advisor ID from session
advisor_id = st.session_state.get("advisor_id", None)

# Show Sidebar
SideBarLinks()

# Page Content
st.title("Advisor Analytics Dashboard")

if advisor_id:
    # Fetch Students Data
    try:
        students = get_students_for_advisor(advisor_id)
        num_students = len(students) if students else 0
    except Exception as e:
        students = []
        st.error(f"Error fetching students: {e}")

    # Fetch Sent Job Listings Data
    try:
        sent_job_listings = get_sent_job_listings(advisor_id)
        num_sent_jobs = len(sent_job_listings) if sent_job_listings else 0
    except Exception as e:
        sent_job_listings = []
        st.error(f"Error fetching sent job listings: {e}")

    # Display Metrics
    st.subheader("Overview")
    st.metric("Number of Students Advised", num_students)
    st.metric("Number of Job Listings Sent", num_sent_jobs)

    # Show Students Table
    if students:
        st.subheader("Students")
        student_data = [{"Name": s["StudentName"], "Email": s["StudentEmail"], "Phone": s["StudentPhoneNumber"]} for s in students]
        st.table(student_data)
    else:
        st.warning("No students found for this advisor.")

    # Show Sent Job Listings Table
    if sent_job_listings:
        st.subheader("Sent Job Listings")
        job_data = [{"Job Title": j["Job Title"], "Location": j["Location"], "Student ID": j["Student ID"]} for j in sent_job_listings]
        st.table(job_data)
    else:
        st.warning("No job listings sent by this advisor.")
else:
    st.warning("No advisor ID found. Please log in.")
