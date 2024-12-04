import streamlit as st
import logging
from modules.nav import SideBarLinks
from utils.style_utils import load_css
from utils.frontend_routes import (
    get_all_companies,
    get_all_job_listings,
    get_job_listings_by_recruiter,
    get_flagged_reviews,
    get_recruiter_analytics
)

logger = logging.getLogger(__name__)

# Define the function to filter flagged reviews by recruiter
def get_flagged_reviews_by_recruiter(recruiter_id):
    """Fetch flagged reviews for a specific recruiter."""
    all_flagged_reviews = get_flagged_reviews()  # Get all flagged reviews
    return [review for review in all_flagged_reviews if review.get('recruiter_id') == recruiter_id]

# Set Streamlit page configuration
st.set_page_config(
    layout="wide",
    page_title="Recruiter Home",
    page_icon="👔"
)

# Apply custom CSS
load_css("./styles/recruiter_home_page_styles.css")

# Sidebar Links
SideBarLinks()

# Hero Section
st.markdown(
    """
    <div class="hero">
        <h1>Welcome recruiter, Quandale.</h1>
        <h3>What would you like to do today?</h3>
    </div>
    """,
    unsafe_allow_html=True
)

# Fetch data for previews
recruiter_id = st.session_state.get('recruiter_id', '300')  # Example recruiter ID
companies = get_all_companies()[:2]
all_job_postings = get_all_job_listings()[:4]
my_job_postings = get_job_listings_by_recruiter(recruiter_id)[:4]
flagged_reviews = get_flagged_reviews_by_recruiter(recruiter_id)[:4]
analytics = get_recruiter_analytics(recruiter_id)

# First Row: Columns for the first three features
st.markdown('<div class="row-spacing"></div>', unsafe_allow_html=True)
cols = st.columns(3, gap="large")

# View all Companies
with cols[0]:
    st.markdown(
        """
        <div class="card">
            <h3>View all Companies</h3>
            <p>Explore all companies registered on the platform.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button('View all Companies', use_container_width=True):
        st.switch_page('pages/Companies_Page.py')
    st.markdown(
        "<div class='preview'><h4>Preview:</h4><ul>" +
        "".join([f"<li>{c.get('Name', 'N/A')} - {c.get('Headline', 'No Headline')}</li>" for c in companies]) +
        "</ul></div>",
        unsafe_allow_html=True
    )

# View all Job Postings
with cols[1]:
    st.markdown(
        """
        <div class="card">
            <h3>View all Job Postings</h3>
            <p>Browse all available job postings.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button('View all Job Postings', use_container_width=True):
        st.session_state['my_job_postings'] = False
        st.session_state['show_sent_jobs'] = False
        st.switch_page('pages/Job_Listings_Page.py')
    st.markdown(
        "<div class='preview'><h4>Preview:</h4><ul>" +
        "".join([f"<li>{jp.get('Job Title', 'N/A')} - {jp.get('Company', 'N/A')}</li>" for jp in all_job_postings]) +
        "</ul></div>",
        unsafe_allow_html=True
    )

# View my Job Postings
with cols[2]:
    st.markdown(
        """
        <div class="card">
            <h3>View my Job Postings</h3>
            <p>Manage your job postings.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button('View my Job Postings', use_container_width=True):
        st.session_state['my_job_postings'] = True
        st.switch_page('pages/Job_Listings_Page.py')
    st.markdown(
        "<div class='preview'><h4>Preview:</h4><ul>" +
        "".join([f"<li>{jp.get('Job Title', 'N/A')} - {jp.get('Company', 'N/A')}</li>" for jp in my_job_postings]) +
        "</ul></div>",
        unsafe_allow_html=True
    )

# Add space before the second row
st.markdown('<div class="row-spacing"></div>', unsafe_allow_html=True)

# Second Row: Columns for the remaining features
cols = st.columns(3, gap="large")

# View all my Flagged Reviews
with cols[0]:
    st.markdown(
        """
        <div class="card">
            <h3>View all my Flagged Reviews</h3>
            <p>Review feedback that needs your attention.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button('View all my Flagged Reviews', use_container_width=True):
        st.session_state['show_my_flagged'] = True
        st.switch_page('pages/Reviews_Page.py')
    st.markdown(
        "<div class='preview'><h4>Preview:</h4><ul>" +
        "".join([f"<li>{fr.get('Description', 'N/A')} - Reason: {fr.get('Reason', 'No Reason')}</li>" for fr in flagged_reviews]) +
        "</ul></div>",
        unsafe_allow_html=True
    )

# View my Job Analytics
with cols[1]:
    st.markdown(
        """
        <div class="card">
            <h3>View my Job Analytics</h3>
            <p>Analyze the performance of your job postings.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button('View my Job Analytics', use_container_width=True):
        st.switch_page('pages/Recruiter_Analytics.py')
    if analytics:
        st.markdown(
            f"""
            <div class='preview'>
                <h4>Analytics Summary:</h4>
                <p>Average Job Satisfaction: {analytics[0].get('averageJobSatisfaction', 'N/A')}</p>
                <p>Number of Reviews: {analytics[0].get('numberOfReviews', 'N/A')}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
