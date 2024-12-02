import streamlit as st
import logging
logger = logging.getLogger(__name__)
from utils.frontend_routes import create_review
from utils.frontend_routes import edit_review
from utils.frontend_routes import toggle_delete_review
from utils.frontend_routes import flag_review

def create_review_modal(job_listing_id, student_id):
    st.write("### Write a Review")
    description = st.text_area("Description")
    jobSatisfaction = st.slider("Job Satisfaction", 0, 5)
    hourlyWage = st.text_input("Hourly Wage")
    anonymous = st.checkbox("Anonymous")
    col1, col2 = st.columns(2)
    with col1:
        submit = st.button("Submit Review")
    with col2:
        if st.button("Cancel"):
            st.session_state["create_modal"] = False

    if submit:
        payload = {
            "description": description,
            "jobSatisfaction": jobSatisfaction,
            "hourlyWage": hourlyWage,
            "anonymous": anonymous,
            "jobListingId": job_listing_id,
            "studentId": student_id,
        }
        logger.info(f"Payload: {payload}")
        create_review(payload)
        st.success("Review submitted.")
        st.session_state["create_modal"] = False

def edit_review_modal(review, edit_modal_key):
    st.write("### Edit Review")
    new_description = st.text_area("Description", value=review['Description'])
    new_job_satisfaction = st.slider("Job Satisfaction", 1, 5, value=review['Job Satisfaction'])
    new_hourly_wage = st.number_input("Hourly Wage", value=review['Hourly Wage'])
    
    if st.button("Save Changes", key=f"save_edit_{review['Review ID']}"):
        payload = {
            "reviewId": review['Review ID'],
            "description": new_description,
            "jobSatisfaction": new_job_satisfaction,
            "hourlyWage": new_hourly_wage,
        }
        edit_review(payload)
        st.success(f"Review for {review['Job Title']} updated successfully!")
        st.session_state[edit_modal_key] = False
    if st.button("Cancel Edit", key=f"cancel_edit_{review['Review ID']}"):
        st.session_state[edit_modal_key] = False
    
def delete_review_modal(review, delete_modal_key):
    st.write("### Are you sure you want to delete this review?")
    if st.button("Confirm", key=f"confirm_delete_{review['Review ID']}"):
        toggle_delete_review(review['Review ID'])
        st.success(f"Review for {review['Job Title']} updated successfully!")
        st.session_state[delete_modal_key] = False
    if st.button("Cancel", key=f"cancel_delete_{review['Review ID']}"):
        st.session_state[delete_modal_key] = False

def flag_review_modal(review, flag_modal_key):
    st.write("### Flag Review")
    st.write("Please provide a reason for flagging this review.")
    reason = st.text_area("Reason")
    if st.button("Submit Flag", key=f"submit_flag_{review['Review ID']}"):
        payload = {
            "reviewId": review['Review ID'],
            "flaggedById": review['Recruiter ID'],
            "reason": reason,
        }
        flag_review(payload)
        st.success(f"Review for {review['Job Title']} flagged successfully!")
        st.session_state[flag_modal_key] = False
    if st.button("Cancel Flag", key=f"cancel_flag_{review['Review ID']}"):
        st.session_state[flag_modal_key] = False