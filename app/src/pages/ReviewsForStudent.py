import streamlit as st
import logging
logger = logging.getLogger(__name__)
from modules.nav import SideBarLinks
from components.review import review_component
from utils.review_modals import create_review_modal
from utils.frontend_routes import get_job_listing_by_id
from utils.frontend_routes import get_reviews_for_job_listing
from utils.frontend_routes import get_reviews_by_student

# Set page layout
st.set_page_config(layout='wide')

student_id = st.session_state.get('studentId', None)

try:
    reviews = get_reviews_by_student(student_id)
except:
    st.write("**Important**: Could not connect to API.")

SideBarLinks()

if reviews:
    student_name = reviews[0]['Student Name']  # Get the student's name from the first review
    st.title(f"{student_name}'s Reviews:")
    st.write('')
    
    for review in reviews:
        review_component(review, my_reviews=False)
else:
    st.write("No reviews available.")


