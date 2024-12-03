import streamlit as st
import logging
logger = logging.getLogger(__name__)
from modules.nav import SideBarLinks
from utils.frontend_routes import get_recruiter_analytics
from utils.style_utils import load_css

# Set Streamlit page configuration for a modern, wide layout
st.set_page_config(
    layout="wide",
    page_title="Recruiter Analytics",
    page_icon="📊"
)

# Apply custom CSS for consistent dark mode theme
load_css("./styles/recruiter_analytics_styles.css")

# Retrieve Recruiter ID
recruiter_id = st.session_state.get('recruiter_id', None)

try:
    reviews = get_recruiter_analytics(recruiter_id)
except:
    st.write("**Important**: Could not connect to API.")

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

# Page Content
st.title("Here are your Job Posting Analytics!")
if recruiter_id:

        # Fetch Analytics Data
    try:
        analytics = get_recruiter_analytics(recruiter_id)

        if analytics:
            st.markdown(f"""
            <div class="container">
                <div class="metric-container">
                    <div class="metric-label">Average Job Satisfaction</div>
                    <div class="metric-value">{analytics[0].get('averageJobSatisfaction', 0)}</div>
                </div>
                <div class="metric-container">
                    <div class="metric-label">Number of Reviews</div>
                    <div class="metric-value">{analytics[0].get('numberOfReviews', 0)}</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        else:
            st.markdown('<div class="error-message">No analytics data found for this recruiter.</div>', unsafe_allow_html=True)
    except Exception as e:
        st.markdown(f'<div class="error-message">Error fetching analytics: {e}</div>', unsafe_allow_html=True)

