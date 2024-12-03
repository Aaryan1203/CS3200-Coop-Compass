import streamlit as st
import logging
logger = logging.getLogger(__name__)
from modules.nav import SideBarLinks
from utils.frontend_routes import get_advisor_analytics
from utils.style_utils import load_css

# Set Streamlit page configuration for a modern, wide layout
st.set_page_config(
    layout="wide",
    page_title="Advisor Analytics",
    page_icon="📊"
)

# Retrieve Advisor ID
advisor_id = st.session_state.get('advisor_id', None)

try:
    analytics = get_advisor_analytics(advisor_id)
except Exception as e:
    st.write("**Important**: Could not connect to API.")
    st.error(f"Error: {e}")

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

# Page Content
st.title("Advisor Analytics")
if advisor_id:
    st.write(f"Analytics for Advisor ID: {advisor_id}")

    # Fetch Analytics Data
    try:
        if analytics:
            st.metric(label="Average Student Satisfaction", value=f"{analytics.get('averageStudentSatisfaction', 0):.2f}")
            st.metric(label="Number of Students Advised", value=analytics.get('numberOfStudents', 0))
            st.metric(label="Number of Reviews", value=analytics.get('numberOfReviews', 0))
        else:
            st.error("No analytics data found for this advisor.")
    except Exception as e:
        st.error(f"Error fetching analytics: {e}")
else:
    st.error("Error: Advisor ID not found in session state. Please return to the home page.")
