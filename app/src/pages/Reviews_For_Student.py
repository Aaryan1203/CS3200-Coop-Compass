import streamlit as st
import logging
logger = logging.getLogger(__name__)
from modules.nav import SideBarLinks
from components.review import review_component
from utils.frontend_routes import get_reviews_by_student
from utils.style_utils import load_css

student_id = st.session_state.get('studentId', None)
recruiter_id = st.session_state.get('recruiterId', None)

try:
    reviews = get_reviews_by_student(student_id)
except:
    st.write("**Important**: Could not connect to API.")

load_css("./styles/reviews_page_styles.css")

SideBarLinks()

if reviews:
    student_name = reviews[0]['Student Name']
    st.title(f"{student_name}'s Reviews:")
    st.write('')
    
    for review in reviews:
        review_component(review, my_reviews=False, student_id=student_id)
else:
    st.write("No reviews available.")


