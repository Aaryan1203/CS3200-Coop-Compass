import streamlit as st
from utils.review_modals import edit_review_modal, delete_review_modal, flag_review_modal
from utils.frontend_routes import unflag_review

def review_component(review, recruiter_id=False, student_id=False, my_reviews=False, is_flagged=False, admin_id=False):
    delete_modal_key = f"delete_modal_{review['Review ID']}"
    edit_modal_key = f"edit_modal_{review['Review ID']}"
    flag_modal_key = f"flag_modal_{review['Review ID']}"

    if delete_modal_key not in st.session_state:
        st.session_state[delete_modal_key] = False
    if edit_modal_key not in st.session_state:
        st.session_state[edit_modal_key] = False
    if flag_modal_key not in st.session_state:
        st.session_state[flag_modal_key] = False

    student_name = review['Student Name'] if not review['Anonymous'] else 'Anonymous'
    job_title = f"{review['Job Title']} at {review['Company']}"
    show_name = my_reviews or student_id

    with st.expander(f"{job_title} - {student_name}" if show_name else student_name):
        st.markdown(
            f"""
            <div class="review-card">
                <div class="review-header">
                    <h3 class="review-title">{job_title}</h3>
                    <p class="review-student">{student_name}</p>
                </div>
                <div class="review-body">
                    <p><strong>Job Satisfaction:</strong> {review['Job Satisfaction']}</p>
                    <p><strong>Hourly Wage:</strong> {review['Hourly Wage']}</p>
                    <p><strong>Description:</strong> {review['Description']}</p>
                </div>
            """,
            unsafe_allow_html=True,
        )

        if student_name not in ['Anonymous']:
            st.write(f"Student Email: {review['Student Email']}")
            st.write(f"Student Phone Number: {str(review['Student Phone Number'])}")

        # Buttons in Columns
        if my_reviews or recruiter_id == review['Recruiter ID'] or admin_id:
            col1, col2, col3 = st.columns([1, 1, 1])  # Adjust proportions as needed

            with col1:
                if my_reviews and st.button("Edit Review", key=f"edit_review_{review['Review ID']}"):
                    st.session_state[edit_modal_key] = True

            with col2:
                if my_reviews and st.button(
                    "Delete Review" if not review['Deleted'] else "Restore Review",
                    key=f"delete_review_{review['Review ID']}",
                ):
                    st.session_state[delete_modal_key] = True

            with col3:
                if recruiter_id == review['Recruiter ID'] or admin_id:
                    if is_flagged:
                        if st.button("UnFlag Review", key=f"unflag_review_{review['Review ID']}"):
                            unflag_review(review['Review ID'])
                            st.success("Review unflagged successfully!")
                    else:
                        if st.button("Flag Review", key=f"flag_review_{review['Review ID']}"):
                            st.session_state[flag_modal_key] = True

        # If flagged, show the reason
        if is_flagged:
            st.markdown(
                f"<p class='flagged-review'><strong>Flagged by {review['Recruiter Name']}:</strong> {review['Reason']}</p>",
                unsafe_allow_html=True,
            )

        # Closing the div
        st.markdown("</div>", unsafe_allow_html=True)

    # Modals
    if st.session_state[delete_modal_key]:
        delete_review_modal(review, delete_modal_key)
    if st.session_state[edit_modal_key]:
        edit_review_modal(review, edit_modal_key)
    if st.session_state[flag_modal_key]:
        flag_review_modal(review, flag_modal_key)
