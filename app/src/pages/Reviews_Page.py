import streamlit as st
import logging
logger = logging.getLogger(__name__)
from modules.nav import SideBarLinks
from components.review import review_component
from utils.review_modals import create_review_modal
from utils.frontend_routes import get_reviews_for_job_listing
from utils.frontend_routes import get_reviews_by_student
from utils.frontend_routes import get_deleted_reviews

# Initialize session state for modals
if "create_modal" not in st.session_state:
    st.session_state["create_modal"] = False

job_listing_id = st.session_state.get('job_listing_id', None)
student_id = st.session_state.get('student_id', None)
show_deleted = st.session_state.get('show_deleted', None)

reviews = []
if job_listing_id:
    try: 
        reviews = get_reviews_for_job_listing(job_listing_id)
    except:
        st.write("**Important**: Could not connect to API.")
elif show_deleted:
    try:
        reviews = get_deleted_reviews()
    except:
        st.write("**Important**: Could not connect to API.")
else:
    try:
        reviews = get_reviews_by_student(student_id)
    except:
        st.write("**Important**: Could not connect to API.")

SideBarLinks()

col1, col2 = st.columns(2)

with col1:
    if job_listing_id:
        st.write(f"## Reviews for {reviews[0]['Job Title']} at {reviews[0]['Company']}")
    elif show_deleted:
        st.write("## Deleted Reviews")
    else:
        st.write("## My Reviews")

with col2:
    if job_listing_id:
        if st.button("Write a review"):
            st.session_state["create_modal"] = True

# Modal for writing a review
if st.session_state["create_modal"]:
    create_review_modal(job_listing_id, student_id)

if reviews:
    my_reviews = not job_listing_id
    for review in reviews:
        review_component(review, my_reviews=my_reviews)
else:
    st.write("No reviews available.")
