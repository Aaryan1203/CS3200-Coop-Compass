import streamlit as st
import logging
from modules.nav import SideBarLinks
from utils.style_utils import load_css

logger = logging.getLogger(__name__)

st.set_page_config(
    layout="wide",
    page_title="Admin Home",
    page_icon="🛠️"
)

# Apply custom CSS for consistent dark mode theme
load_css("./styles/admin_home_page_styles.css")

# Sidebar Links
SideBarLinks()

# Add a hero section
st.markdown(
    """
    <div class="hero">
        <h1>Welcome admin, Sam.</h1>
        <h3>What would you like to do today?</h3>
    </div>
    """,
    unsafe_allow_html=True
)

# Create columns for the card layout
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
        st.switch_page("pages/Job_Listings_Page.py")

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
        st.switch_page("pages/Job_Listings_Page.py")

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
