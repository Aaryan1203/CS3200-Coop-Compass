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
            st.metric(label="Average Job Satisfaction", value=analytics[0].get('averageJobSatisfaction', 0))
            st.metric(label="Number of Reviews", value=analytics[0].get('numberOfReviews', 0))
        else:
            st.error("No analytics data found for this recruiter.")
    except Exception as e:
        st.error(f"Error fetching analytics: {e}")
else:
    st.error("Error: Recruiter ID not found in session state. Please return to the home page.")