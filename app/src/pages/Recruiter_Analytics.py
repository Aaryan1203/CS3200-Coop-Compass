import streamlit as st
import logging
logger = logging.getLogger(__name__)
from modules.nav import SideBarLinks
from modules.filter_functions import filter_job_listings
from utils.frontend_routes import (
get_recruiter_analytics,
get_all_reviews,
get_job_listings_by_recruiter,
)
from utils.style_utils import load_css
from components.job_listing import job_listing_component
from components.search import search_bar

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

    try: 
        listings = get_job_listings_by_recruiter(recruiter_id)
        reviews = get_all_reviews()

        st.subheader("Analytics Shown For Your Job Postings:")
        text_input = search_bar("Jobs")

        if listings:
                for listing in listings:
                     filtered_job_listings = filter_job_listings(listings, text_input)
                     num_reviews = len([review for review in reviews if review['Job Listing ID'] == listing['Job Listing ID']])

                     job_listing_component(listing, num_reviews, student_id=None, advisor_id=None, my_job_postings=True)
        else:
            st.markdown('<div class="error-message">No job listings found for this recruiter.</div>', unsafe_allow_html=True)
    except Exception as e:
        st.markdown(f'<div class="error-message">Error fetching analytics: {e}</div>', unsafe_allow_html=True)






