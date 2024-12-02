import streamlit as st
import logging
logger = logging.getLogger(__name__)
from utils.frontend_routes import create_review, edit_review, toggle_delete_review, flag_review

st.markdown(
    """
    <style>
    .modal-overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background-color: rgba(0, 0, 0, 0.7);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 1000;
    }
    .modal {
        background-color: #1e1e1e;
        border-radius: 10px;
        padding: 20px;
        color: white;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        font-family: 'Arial', sans-serif;
        width: 400px;
    }
    .modal h3 {
        text-align: center;
        font-weight: bold;
        color: #00aaff;
    }
    .modal button {
        background-color: #007bff;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        font-size: 16px;
        cursor: pointer;
    }
    .modal button:hover {
        background-color: #0056b3;
    }
    .input-box input {
        width: 120px; /* Adjust the width of the input box */
        font-size: 16px; /* Keep the font size consistent */
        padding: 5px;
        border: 1px solid #ccc;
        border-radius: 5px;
        color: black; /* Ensure input text is black for readability */
        background-color: white; /* Set a white background for contrast */
    }
    .input-box input::placeholder {
        color: black; /* Make placeholder text black */
        opacity: 0.6; /* Adjust opacity for subtlety */
    }
    </style>
    """,
    unsafe_allow_html=True,
)
# Create Review Modal
def create_review_modal(job_listing_id, student_id):
    st.markdown('<div class="modal-overlay"><div class="modal">', unsafe_allow_html=True)
    st.write("### Write a Review")
    description = st.text_area("Description", placeholder="Describe your experience...")
    jobSatisfaction = st.slider("Job Satisfaction", 0, 5)
    hourlyWage = st.text_input("Hourly Wage", placeholder="Enter your hourly wage")
    anonymous = st.checkbox("Post anonymously")
    col1, col2 = st.columns(2)
    with col1:
        submit = st.button("Submit Review ✅")
    with col2:
        if st.button("Cancel ❌"):
            st.session_state["create_modal"] = False

    if submit:
        if not description.strip():
            st.error("Description cannot be empty!")
            return
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
        st.success("Review submitted successfully!")
        st.session_state["create_modal"] = False
    st.markdown('</div></div>', unsafe_allow_html=True)

# Edit Review Modal
def edit_review_modal(review, edit_modal_key):
    st.markdown('<div class="modal-overlay"><div class="modal">', unsafe_allow_html=True)
    st.write("### Edit Review")
    new_description = st.text_area("Description", value=review['Description'], placeholder="Update your description...")
    new_job_satisfaction = st.slider("Job Satisfaction", 1, 5, value=review['Job Satisfaction'])
    new_hourly_wage = st.number_input("Hourly Wage", value=review['Hourly Wage'], format="%.2f")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Save Changes ✅", key=f"save_edit_{review['Review ID']}"):
            payload = {
                "reviewId": review['Review ID'],
                "description": new_description,
                "jobSatisfaction": new_job_satisfaction,
                "hourlyWage": new_hourly_wage,
            }
            edit_review(payload)
            st.success(f"Review for {review['Job Title']} updated successfully!")
            st.session_state[edit_modal_key] = False
    with col2:
        if st.button("Cancel Edit ❌", key=f"cancel_edit_{review['Review ID']}"):
            st.session_state[edit_modal_key] = False
    st.markdown('</div></div>', unsafe_allow_html=True)

# Delete Review Modal
def delete_review_modal(review, delete_modal_key):
    st.markdown('<div class="modal-overlay"><div class="modal">', unsafe_allow_html=True)
    st.write("### Are you sure you want to delete this review?")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Confirm ✅", key=f"confirm_delete_{review['Review ID']}"):
            toggle_delete_review(review['Review ID'])
            st.success(f"Review for {review['Job Title']} deleted successfully!")
            st.session_state[delete_modal_key] = False
    with col2:
        if st.button("Cancel ❌", key=f"cancel_delete_{review['Review ID']}"):
            st.session_state[delete_modal_key] = False
    st.markdown('</div></div>', unsafe_allow_html=True)

# Flag Review Modal
def flag_review_modal(review, flag_modal_key):
    st.markdown('<div class="modal-overlay"><div class="modal">', unsafe_allow_html=True)
    st.write("### Flag Review")
    reason = st.text_area("Reason", placeholder="Provide a reason for flagging this review...")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Submit Flag ✅", key=f"submit_flag_{review['Review ID']}"):
            if not reason.strip():
                st.error("Reason cannot be empty!")
                return
            payload = {
                "reviewId": review['Review ID'],
                "flaggedById": review['Recruiter ID'],
                "reason": reason,
            }
            flag_review(payload)
            st.success(f"Review for {review['Job Title']} flagged successfully!")
            st.session_state[flag_modal_key] = False
    with col2:
        if st.button("Cancel Flag ❌", key=f"cancel_flag_{review['Review ID']}"):
            st.session_state[flag_modal_key] = False
    st.markdown('</div></div>', unsafe_allow_html=True)
