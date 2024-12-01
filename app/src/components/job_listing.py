import streamlit as st
from utils.job_listing_modals import delete_job_listing_modal
from utils.job_listing_modals import edit_job_listing_modal
from utils.frontend_routes import toggle_favorite_job_listing

def job_listing_component(job, num_reviews, student_id, my_job_postings=False, is_favorite=False, deleted=False):
    delete_modal_key = f"delete_modal_{job['Job Listing ID']}"
    edit_modal_key = f"edit_modal_{job['Job Listing ID']}"

    if delete_modal_key not in st.session_state:
        st.session_state[delete_modal_key] = False
    if edit_modal_key not in st.session_state:
        st.session_state[edit_modal_key] = False

    with st.expander(f"{job['Company']}: {job['Job Title']}"):
        col1, col2, col3 = st.columns([2, 2, 1])
        with col1:
            st.write("**Start Date**")
            st.write(job.get('Start Date', 'N/A'))
            st.write("**End Date**")
            st.write(job.get('End Date', 'N/A'))
            st.write("**Skills**")
            st.write(job.get('Skills', 'N/A'))
        with col2:
            st.write("**Hourly Wage**")
            st.write(f"${job.get('Hourly Wage', 'N/A')} per hour")
            st.write("**Location**")
            st.write(job.get('Location', 'N/A'))
            st.write("**All Reviews**")
            if st.button(f"{num_reviews} {'Review' if num_reviews == 1 else 'Reviews'}",
                    key=f"reviews_button_{job['Job Listing ID']}",
                    type='secondary'):
                st.query_params.job_listing_id = job['Job Listing ID']
                st.session_state['job_listing_id'] = job['Job Listing ID']
                st.switch_page('pages/Reviews_Page.py')
            if my_job_postings:
                if st.button("Edit Job Listing", key=f"edit_job_{job['Job Listing ID']}"):
                    st.session_state[edit_modal_key] = True
                if st.button("Delete Job Listing", key=f"delete_job_{job['Job Listing ID']}") if not deleted else st.button("Restore Job Listing", key=f"restore_job_{job['Job Listing ID']}"):
                    st.session_state[delete_modal_key] = True
        with col3:
            if student_id:
                if st.button("⭐" if is_favorite else "☆",
                            key=f"favorite_button_{job['Job Listing ID']}"):
                    payload = {
                        'jobListingId': job['Job Listing ID'],
                        'studentId': student_id
                    }
                    toggle_favorite_job_listing(payload)
        st.write("**Description**")
        st.write(job.get('Description', 'N/A'))

    # Delete modal
    if st.session_state[delete_modal_key]:
        delete_job_listing_modal(job['Job Listing ID'], delete_modal_key, deleted)

    # Edit modal
    if st.session_state[edit_modal_key]:
        edit_job_listing_modal(job, edit_modal_key)

