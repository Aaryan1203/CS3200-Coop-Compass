import streamlit as st
import logging
from modules.nav import SideBarLinks
from utils.style_utils import load_css
from utils.frontend_routes import (
    get_all_companies,
    get_all_job_listings,
    get_deleted_job_listings,
    get_flagged_reviews,
    get_deleted_reviews
)

logger = logging.getLogger(__name__)

st.set_page_config(
    layout="wide",
    page_title="Admin Home",
    page_icon="🛠️"
)

# Apply custom CSS
load_css("./styles/admin_home_page_styles.css")

# Sidebar Links
SideBarLinks()

# Hero Section
st.markdown(
    """
    <div class="hero">
        <h1>Welcome admin, Sam.</h1>
        <h3>What would you like to do today?</h3>
    </div>
    """,
    unsafe_allow_html=True
)

# Fetch Data
companies = get_all_companies()[:10]  # Fetch top 10 companies
job_postings = get_all_job_listings()[:10]  # Fetch top 10 active job postings
deleted_job_postings = get_deleted_job_listings()[:10]  # Fetch top 10 deleted job postings
flagged_reviews = get_flagged_reviews()[:10]  # Fetch top 10 flagged reviews
deleted_reviews = get_deleted_reviews()[:10]  # Fetch top 10 deleted reviews

# Create columns for cards
cols = st.columns(5, gap="large")

# Section: View All Companies
with cols[0]:
    st.markdown(
        """
        <div class="card">
            <h3>View all Companies</h3>
            <p>See a list of all registered companies.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("View all Companies", use_container_width=True):
        st.switch_page("pages/Companies_Page.py")

    # Preview for Companies
    st.markdown(
        "<div class='preview'><h4>Preview:</h4><ul>" +
        "".join([f"<li>{c.get('Name', 'N/A')} - {c.get('Headline', 'No Headline')}</li>" for c in companies]) +
        "</ul></div>",
        unsafe_allow_html=True
    )

# Section: View All Job Postings
with cols[1]:
    st.markdown(
        """
        <div class="card">
            <h3>View all Job Postings</h3>
            <p>Browse through all active job postings.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("View all Job Postings", use_container_width=True):
        st.session_state['my_job_postings'] = False
        st.session_state['show_deleted'] = False
        st.session_state['show_flagged'] = False
        st.session_state['show_sent_jobs'] = False
        st.session_state['show_recieved_jobs'] = False
        st.switch_page("pages/Job_Listings_Page.py")

    # Preview for Job Postings
    st.markdown(
        "<div class='preview'><h4>Preview:</h4><ul>" +
        "".join([f"<li>{jp.get('Job Title', 'N/A')} - {jp.get('Company', 'N/A')}</li>" for jp in job_postings]) +
        "</ul></div>",
        unsafe_allow_html=True
    )

# Section: View All Deleted Job Postings
with cols[2]:
    st.markdown(
        """
        <div class="card">
            <h3>View all Deleted Job Postings</h3>
            <p>Review job postings that have been deleted.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("View all Deleted Job Postings", use_container_width=True):
        st.session_state['my_job_postings'] = False
        st.session_state['show_deleted'] = True
        st.session_state['show_flagged'] = False
        st.session_state['show_sent_jobs'] = False
        st.session_state['show_recieved_jobs'] = False
        st.switch_page("pages/Job_Listings_Page.py")

    # Preview for Deleted Job Postings
    st.markdown(
        "<div class='preview'><h4>Preview:</h4><ul>" +
        "".join([f"<li>{djp.get('Job Title', 'N/A')} - {djp.get('Company', 'N/A')}</li>" for djp in deleted_job_postings]) +
        "</ul></div>",
        unsafe_allow_html=True
    )

# Section: View All Flagged Reviews
with cols[3]:
    st.markdown(
        """
        <div class="card">
            <h3>View all Flagged Reviews</h3>
            <p>See reviews flagged for inappropriate content.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("View all Flagged Reviews", use_container_width=True):
        st.session_state['show_flagged'] = True
        st.session_state['show_deleted'] = False
        st.session_state['job_listing_id'] = False
        st.session_state['show_my_flagged'] = False
        st.switch_page("pages/Reviews_Page.py")

    # Preview for Flagged Reviews
    st.markdown(
        "<div class='preview'><h4>Preview:</h4><ul>" +
        "".join([f"<li>{fr.get('Description', 'N/A')} - Reason: {fr.get('Reason', 'No Reason')}</li>" for fr in flagged_reviews]) +
        "</ul></div>",
        unsafe_allow_html=True
    )

# Section: View All Deleted Reviews
with cols[4]:
    st.markdown(
        """
        <div class="card">
            <h3>View all Deleted Reviews</h3>
            <p>Browse through all deleted reviews.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("View all Deleted Reviews", use_container_width=True):
        st.session_state['show_flagged'] = False
        st.session_state['show_deleted'] = True
        st.session_state['job_listing_id'] = False
        st.switch_page("pages/Reviews_Page.py")

    # Preview for Deleted Reviews
    st.markdown(
        "<div class='preview'><h4>Preview:</h4><ul>" +
        "".join([f"<li>{dr.get('Description', 'N/A')} - Satisfaction: {dr.get('Job Satisfaction', 'N/A')}</li>" for dr in deleted_reviews]) +
        "</ul></div>",
        unsafe_allow_html=True
    )
