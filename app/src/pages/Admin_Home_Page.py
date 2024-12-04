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
companies = get_all_companies()[:2]
job_postings = get_all_job_listings()[:3]
deleted_job_postings = get_deleted_job_listings()[:3]
flagged_reviews = get_flagged_reviews()[:3]
deleted_reviews = get_deleted_reviews()[:3]

# Create Rows for Cards
row1_cols = st.columns(3, gap="large")  # First row with 3 cards
# Add space before second row
st.markdown('<div class="row-spacing"></div>', unsafe_allow_html=True)

row2_cols = st.columns(2, gap="large")  # Second row with 2 cards

# Row 1: Companies, Active Job Postings, Deleted Job Postings
with row1_cols[0]:
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
    st.markdown(
        "<div class='preview'><h4>Preview:</h4><ul>" +
        "".join([f"<li>{c.get('Name', 'N/A')} - {c.get('Headline', 'No Headline')}</li>" for c in companies]) +
        "</ul></div>",
        unsafe_allow_html=True
    )

with row1_cols[1]:
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
        st.session_state["show_deleted"] = False
        st.session_state['my_job_postings'] = False
        st.session_state['show_sent_jobs'] = False
        st.session_state['show_recieved_jobs'] = False
        st.switch_page("pages/Job_Listings_Page.py")
    st.markdown(
        "<div class='preview'><h4>Preview:</h4><ul>" +
        "".join([f"<li>{jp.get('Job Title', 'N/A')} - {jp.get('Company', 'N/A')}</li>" for jp in job_postings]) +
        "</ul></div>",
        unsafe_allow_html=True
    )

with row1_cols[2]:
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
        st.session_state["show_deleted"] = True
        st.session_state["company_id"] = None
        st.session_state["my_job_postings"] = False
        st.switch_page("pages/Job_Listings_Page.py")
    st.markdown(
        "<div class='preview'><h4>Preview:</h4><ul>" +
        "".join([f"<li>{djp.get('Job Title', 'N/A')} - {djp.get('Company', 'N/A')}</li>" for djp in deleted_job_postings]) +
        "</ul></div>",
        unsafe_allow_html=True
    )

# Row 2: Flagged Reviews, Deleted Reviews
with row2_cols[0]:
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
        st.session_state["show_flagged"] = True
        st.session_state['show_my_flagged'] = False
        st.session_state['job_listing_id'] = False
        st.session_state['show_deleted'] = False
        st.switch_page("pages/Reviews_Page.py")
    st.markdown(
        "<div class='preview'><h4>Preview:</h4><ul>" +
        "".join([f"<li>{fr.get('Description', 'N/A')} - Reason: {fr.get('Reason', 'No Reason')}</li>" for fr in flagged_reviews]) +
        "</ul></div>",
        unsafe_allow_html=True
    )

with row2_cols[1]:
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
        st.session_state["show_deleted"] = True
        st.switch_page("pages/Reviews_Page.py")
    st.markdown(
        "<div class='preview'><h4>Preview:</h4><ul>" +
        "".join([f"<li>{dr.get('Description', 'N/A')} - Satisfaction: {dr.get('Job Satisfaction', 'N/A')}</li>" for dr in deleted_reviews]) +
        "</ul></div>",
        unsafe_allow_html=True
    )
