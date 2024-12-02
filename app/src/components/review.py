import streamlit as st
from utils.review_modals import edit_review_modal
from utils.review_modals import delete_review_modal
from utils.review_modals import flag_review_modal
from utils.frontend_routes import unflag_review

def review_component(review, recruiter_id, my_reviews=False, is_flagged=False, admin_id=False):
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

    with st.expander(f"{job_title} - {student_name}" if my_reviews else student_name):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write("**Job Satisfaction**")
            st.write(review['Job Satisfaction'])
            st.write("**Hourly Wage**")
            st.write(review['Hourly Wage'])
            st.write("**Description**")
            st.write(review['Description'])

        if my_reviews:
            with col2:
                if st.button("Edit review", key=f"edit_review_{review['Review ID']}"):
                    st.session_state[edit_modal_key] = True
                if st.button("Delete review", key=f"delete_review_{review['Review ID']}") if not review['Deleted'] else st.button("Restore review", key=f"restore_review_{review['Review ID']}"):
                    st.session_state[delete_modal_key] = True
        
        if recruiter_id == review['Recruiter ID'] or admin_id:
            with col3:
                if is_flagged:
                    if st.button("UnFlag Review", key=f"unflag_review_{review['Review ID']}"):
                        unflag_review(review['Review ID'])
                        st.success("Review unflagged successfully!")
                else:
                    if st.button("Flag Review", key=f"flag_review_{review['Review ID']}"):
                        st.session_state[flag_modal_key] = True
        
        if is_flagged:
            st.write(f"**This review has been flagged**")
            st.write(f"Reason: {review['Reason']}")

    # Delete modal
    if st.session_state[delete_modal_key]:
        delete_review_modal(review, delete_modal_key)

    # Edit modal
    if st.session_state[edit_modal_key]:
        edit_review_modal(review, edit_modal_key)
    
    # Flag modal
    if st.session_state[flag_modal_key]:
        flag_review_modal(review, flag_modal_key)

