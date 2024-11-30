import streamlit as st
from utils.review_modals import edit_review_modal
from utils.review_modals import delete_review_modal

def review_component(review, my_reviews=False):
    delete_modal_key = f"delete_modal_{review['Review ID']}"
    edit_modal_key = f"edit_modal_{review['Review ID']}"

    if delete_modal_key not in st.session_state:
        st.session_state[delete_modal_key] = False
    if edit_modal_key not in st.session_state:
        st.session_state[edit_modal_key] = False

    student_name = review['Student Name'] if not review['Anonymous'] else 'Anonymous'
    job_title = f"{review['Job Title']} at {review['Company']}"

    with st.expander(job_title if my_reviews else student_name):
        col1, col2 = st.columns(2)
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

    # Delete modal
    if st.session_state[delete_modal_key]:
        delete_review_modal(review, delete_modal_key)

    # Edit modal
    if st.session_state[edit_modal_key]:
        edit_review_modal(review, edit_modal_key)

