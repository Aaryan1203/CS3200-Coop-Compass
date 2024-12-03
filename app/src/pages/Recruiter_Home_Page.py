import streamlit as st
import logging
from modules.nav import SideBarLinks
from utils.style_utils import load_css
from utils.frontend_routes import (
    get_all_companies,
    get_all_job_listings,
    get_job_listings_by_recruiter,
    get_recruiter_analytics
)

logger = logging.getLogger(__name__)

# Set Streamlit page configuration for a modern, wide layout
st.set_page_config(
    layout="wide",
    page_title="Recruiter Home",
    page_icon="👔"
)

# Apply custom CSS for consistent dark mode theme
load_css("./styles/recruiter_home_page_styles.css")

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

# Add a hero section
st.markdown(
    f"""
    <div class="hero">
        <h1>Welcome recruiter, {st.session_state['first_name']}.</h1>
        <h3>What would you like to do today?</h3>
    </div>
    """,
    unsafe_allow_html=True
)

# Fetch data for previews
recruiter_id = st.session_state.get('recruiter_id', '300')  # Example recruiter ID
companies = get_all_companies()[:10]
all_job_postings = get_all_job_listings()[:10]
my_job_postings = get_job_listings_by_recruiter(recruiter_id)[:10]
#flagged_reviews = get_flagged_reviews_by_recruiter(recruiter_id)[:10]
analytics = get_recruiter_analytics(recruiter_id)

# Create columns for cards
cols = st.columns(5, gap="large")

# Section: View all Companies
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
    # Preview for Companies
    st.markdown(
        "<div class='preview'><h4>Preview:</h4><ul>" +
        "".join([f"<li>{c.get('Name', 'N/A')} - {c.get('Headline', 'No Headline')}</li>" for c in companies]) +
        "</ul></div>",
        unsafe_allow_html=True
    )

# Section: View all Job Postings
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
        st.session_state['company_id'] = False
        st.session_state['my_job_postings'] = False
        st.session_state['show_deleted'] = False
        st.session_state['show_flagged'] = False
        st.switch_page('pages/Job_Listings_Page.py')
    # Preview for All Job Postings
    st.markdown(
        "<div class='preview'><h4>Preview:</h4><ul>" +
        "".join([f"<li>{jp.get('Job Title', 'N/A')} - {jp.get('Company', 'N/A')}</li>" for jp in all_job_postings]) +
        "</ul></div>",
        unsafe_allow_html=True
    )

# Section: View my Job Postings
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
        st.session_state['company_id'] = False
        st.session_state['my_job_postings'] = True
        st.session_state['show_deleted'] = False
        st.session_state['show_flagged'] = False
        st.session_state['show_my_flagged'] = False
        st.switch_page('pages/Job_Listings_Page.py')
    # Preview for Recruiter's Job Postings
    st.markdown(
        "<div class='preview'><h4>Preview:</h4><ul>" +
        "".join([f"<li>{jp.get('Job Title', 'N/A')} - {jp.get('Company', 'N/A')}</li>" for jp in my_job_postings]) +
        "</ul></div>",
        unsafe_allow_html=True
    )

# Section: View all my Flagged Reviews
with cols[3]:
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
        st.session_state['show_flagged'] = False
        st.session_state['show_my_flagged'] = True
        st.session_state['show_deleted'] = False
        st.session_state['job_listing_id'] = False
        st.switch_page('pages/Reviews_Page.py')
    # Preview for Flagged Reviews
    # st.markdown(
    #     "<div class='preview'><h4>Preview:</h4><ul>" +
    #     "".join([f"<li>{fr.get('Description', 'N/A')} - Reason: {fr.get('Reason', 'No Reason')}</li>" for fr in flagged_reviews]) +
    #     "</ul></div>",
    #     unsafe_allow_html=True
    #)

# Section: View my Job Analytics
with cols[4]:
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
    # Preview for Analytics (if any)
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
