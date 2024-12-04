import streamlit as st
from modules.nav import SideBarLinks
from utils.frontend_routes import (
    get_reviews_by_student,
    get_all_companies,
    get_all_job_listings,
    get_received_job_listings,
)
from utils.style_utils import load_css

# Set page configuration
st.set_page_config(
    layout="wide",
    page_title="Student Home",
    page_icon="🎓"
)

load_css("./styles/student_home_page_styles.css")

# Sidebar Links
SideBarLinks()

# Add a hero section
st.markdown(
    """
    <div class="hero">
        <h1>Welcome, Aaryan</h1>
        <h3>What would you like to do today?</h3>
    </div>
    """,
    unsafe_allow_html=True
)

# Fetch all data
companies = get_all_companies()[:2]
job_postings = get_all_job_listings()[:2]
student_id = st.session_state.get("student_id", "100")
all_reviews = get_reviews_by_student(student_id)[:3]
received_job_listings = get_received_job_listings(student_id)[:3]

# Top Row: Two features
st.markdown('<div class="row-spacing"></div>', unsafe_allow_html=True)
cols_top = st.columns(2, gap="large")

# View All Companies
with cols_top[0]:
    st.markdown(
        """
        <div class="card">
            <h3>View All Companies</h3>
            <p>Explore a list of all the companies offering co-op opportunities.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("View All Companies", use_container_width=True):
        st.switch_page("pages/Companies_Page.py")

    st.markdown(
        "<div class='preview'><h4>Preview:</h4><ul>" +
        "".join([f"<li>{c.get('Name', 'N/A')} - {c.get('Headline', 'No Headline')}</li>" for c in companies]) +
        "</ul></div>",
        unsafe_allow_html=True,
    )

# View All Job Postings
with cols_top[1]:
    st.markdown(
        """
        <div class="card">
            <h3>View All Job Postings</h3>
            <p>Browse through the latest job postings and find your next opportunity.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("View All Job Postings", use_container_width=True):
        st.session_state['company_id'] = False
        st.session_state['my_job_postings'] = False
        st.session_state['show_deleted'] = False
        st.session_state['show_sent_jobs'] = False
        st.session_state['show_recieved_jobs'] = False
        st.session_state['recruiter_id'] = False
        st.switch_page("pages/Job_Listings_Page.py")

    st.markdown(
        "<div class='preview'><h4>Preview:</h4><ul>" +
        "".join([f"<li>{jp.get('Job Title', 'N/A')} - {jp.get('Company', 'N/A')}</li>" for jp in job_postings]) +
        "</ul></div>",
        unsafe_allow_html=True,
    )

# Add spacing between rows
st.markdown('<div class="row-spacing"></div>', unsafe_allow_html=True)
st.markdown('<div class="row-spacing"></div>', unsafe_allow_html=True)

# Bottom Row: Two features
cols_bottom = st.columns(2, gap="large")

# View My Reviews
with cols_bottom[0]:
    st.markdown(
        """
        <div class="card">
            <h3>View My Reviews</h3>
            <p>See all of my reviews.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("View My Reviews", use_container_width=True):
        st.session_state['job_listing_id'] = False
        st.session_state['show_deleted'] = False
        st.session_state['show_flagged'] = False
        st.session_state['show_my_flagged'] = False
        st.switch_page("pages/Reviews_Page.py")

    st.markdown(
        "<div class='preview'><h4>Preview:</h4><ul>" +
        "".join([f"<li>{r.get('Description', 'N/A')} - Satisfaction: {r.get('Job Satisfaction', 'N/A')}</li>" for r in all_reviews]) +
        "</ul></div>",
        unsafe_allow_html=True,
    )

# View My Received Job Listings
with cols_bottom[1]:
    st.markdown(
        """
        <div class="card">
            <h3>View My Received Job Listings</h3>
            <p>See my received job listings.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("View My Received Listings", use_container_width=True):
        st.session_state['show_recieved_jobs'] = True
        st.session_state['company_id'] = False
        st.session_state['my_job_postings'] = False
        st.session_state['show_deleted'] = False
        st.session_state['show_sent_jobs'] = False
        st.session_state['recruiter_id'] = False
        st.switch_page("pages/Job_Listings_Page.py")

    st.markdown(
        "<div class='preview'><h4>Preview:</h4><ul>" +
        "".join([f"<li>{jp.get('Job Title', 'N/A')} - {jp.get('Company', 'N/A')}</li>" for jp in received_job_listings]) +
        "</ul></div>",
        unsafe_allow_html=True,
    )
