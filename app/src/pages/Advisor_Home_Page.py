import streamlit as st
from modules.nav import SideBarLinks
from utils.style_utils import load_css
from utils.frontend_routes import (
    get_all_reviews,
    get_students_for_advisor,
    get_all_job_listings,
    get_sent_job_listings
)
import logging

logger = logging.getLogger(__name__)

# Set page configuration
st.set_page_config(
    layout="wide",
    page_title="Advisor Home",
    page_icon="🧑‍🏫"
)

# Load external CSS
load_css("./styles/advisor_home_page_styles.css")

# Sidebar Links
SideBarLinks()

# Add a hero section
st.markdown(
    """
    <div class="hero">
        <h1>Welcome, advisor Rachel</h1>
        <h3>What would you like to do today?</h3>
    </div>
    """,
    unsafe_allow_html=True
)

# Fetching data using helper functions
advisor_id = 1  # Example advisor ID
reviews = get_all_reviews()[:2]  # Limit previews to 3
students = get_students_for_advisor(advisor_id)[:2]
job_postings = get_all_job_listings()[:3]
sent_job_postings = get_sent_job_listings(advisor_id)[:3]

# Top Row: Two Features
st.markdown('<div class="row-spacing"></div>', unsafe_allow_html=True)
cols_top = st.columns(2, gap="large")

# Section: View All Job Postings (Top Left)
with cols_top[0]:
    st.markdown(
        """
        <div class="card">
            <h3>View All Job Postings</h3>
            <p>Browse through all available job postings.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("View All Job Postings", use_container_width=True):
        st.session_state['company_id'] = False
        st.session_state['my_job_postings'] = False
        st.session_state['show_deleted'] = False
        st.session_state['show_sent_jobs'] = False
        st.session_state['show_recieved_jobs'] = False
        st.switch_page("pages/Job_Listings_Page.py")

    # Preview for All Job Postings
    st.markdown(
        "<div class='preview'><h4>Preview:</h4><ul>" +
        "".join([f"<li>{jp.get('Job Title', 'N/A')} - {jp.get('Company', 'N/A')}</li>" for jp in job_postings]) +
        "</ul></div>",
        unsafe_allow_html=True
    )

# Section: My Students Reviews (Top Right)
with cols_top[1]:
    st.markdown(
        """
        <div class="card">
            <h3>View My Students Reviews</h3>
            <p>See reviews provided by your students.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("View My Students Reviews", use_container_width=True):
        st.switch_page("pages/My_Students.py")
    st.markdown(
        "<div class='preview'><h4>Preview:</h4><ul>" +
        "".join([f"<li>{r.get('Student Name', 'N/A')}: {r.get('Description', 'No Description')} - Satisfaction: {r.get('Job Satisfaction', 'N/A')}</li>" for r in reviews]) +
        "</ul></div>",
        unsafe_allow_html=True
    )

# Bottom Row: Two Features
st.markdown('<div class="row-spacing"></div>', unsafe_allow_html=True)
st.markdown('<div class="row-spacing"></div>', unsafe_allow_html=True)
cols_bottom = st.columns(2, gap="large")

# Section: Sent Job Listings (Bottom Left)
with cols_bottom[0]:
    st.markdown(
        """
        <div class="card">
            <h3>View My Sent Job Listings</h3>
            <p>Browse the job listings you’ve posted or managed.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("View My Sent Job Listings", use_container_width=True):
        st.session_state['company_id'] = False
        st.session_state['my_job_postings'] = False
        st.session_state['show_deleted'] = False
        st.session_state['show_flagged'] = False
        st.session_state['show_sent_jobs'] = True
        st.session_state['show_recieved_jobs'] = False
        st.switch_page("pages/Job_Listings_Page.py")
    st.markdown(
        "<div class='preview'><h4>Preview:</h4><ul>" +
        "".join([f"<li>{jp.get('Job Title', 'N/A')} - {jp.get('Company', 'N/A')}</li>" for jp in sent_job_postings]) +
        "</ul></div>",
        unsafe_allow_html=True
    )

# Section: My Students Analytics (Bottom Right)
with cols_bottom[1]:
    st.markdown(
        """
        <div class="card">
            <h3>View My Students Analytics</h3>
            <p>Analyze the performance and engagement of your students.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("View My Students Analytics", use_container_width=True):
        st.switch_page("pages/Advisor_Analytics.py")
    st.markdown(
        "<div class='preview'><h4>Preview:</h4><ul>" +
        "".join([f"<li>{s.get('StudentName', 'N/A')} - Email: {s.get('StudentEmail', 'N/A')}</li>" for s in students]) +
        "</ul></div>",
        unsafe_allow_html=True
    )
