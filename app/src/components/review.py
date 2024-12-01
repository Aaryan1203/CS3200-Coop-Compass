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
                <div class="review-actions">
            """,
            unsafe_allow_html=True,
        )

        if my_reviews:
            if st.button("Edit Review", key=f"edit_review_{review['Review ID']}"):
                st.session_state[edit_modal_key] = True
            if st.button(
                "Delete Review" if not review['Deleted'] else "Restore Review",
                key=f"delete_review_{review['Review ID']}",
            ):
                st.session_state[delete_modal_key] = True

        if recruiter_id == review['Recruiter ID'] or admin_id:
            if is_flagged:
                if st.button("UnFlag Review", key=f"unflag_review_{review['Review ID']}"):
                    unflag_review(review['Review ID'])
                    st.success("Review unflagged successfully!")
            else:
                if st.button("Flag Review", key=f"flag_review_{review['Review ID']}"):
                    st.session_state[flag_modal_key] = True

        if is_flagged:
            st.markdown(
                f"<p class='flagged-review'><strong>Flagged:</strong> {review['Reason']}</p>",
                unsafe_allow_html=True,
            )

        # Closing the div
        st.markdown("</div></div>", unsafe_allow_html=True)

    if st.session_state[delete_modal_key]:
        delete_review_modal(review, delete_modal_key)
    if st.session_state[edit_modal_key]:
        edit_review_modal(review, edit_modal_key)
    if st.session_state[flag_modal_key]:
        flag_review_modal(review, flag_modal_key)
