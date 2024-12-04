import streamlit as st
from utils.job_listing_modals import delete_job_listing_modal
from utils.job_listing_modals import edit_job_listing_modal
from utils.frontend_routes import toggle_favorite_job_listing
from utils.frontend_routes import get_students_for_advisor, toggle_sent_job_listing
import logging
logger = logging.getLogger(__name__)

def job_listing_component(job, num_reviews, student_id, advisor_id, my_job_postings=False, is_favorite=False, deleted=False, show_sent_jobs=False):
    delete_modal_key = f"delete_modal_{job['Job Listing ID']}"
    edit_modal_key = f"edit_modal_{job['Job Listing ID']}"

    if delete_modal_key not in st.session_state:
        st.session_state[delete_modal_key] = False
    if edit_modal_key not in st.session_state:
        st.session_state[edit_modal_key] = False

    with st.expander(f"{job['Company']}: {job['Job Title']}"):
        col1, col2, col3, col4 = st.columns([2, 2, 1, 1])
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
            if st.button(f"{num_reviews} {'Review' if num_reviews == 1 else 'Reviews'}",
                    key=f"reviews_button_{job['Job Listing ID']}",
                    type='secondary'):
                st.session_state['job_listing_id'] = job['Job Listing ID']
                st.session_state['job_title'] = f"{job['Job Title']} at {job['Company']}" 
                st.session_state['job_listing_id'] = job['Job Listing ID']
                st.session_state['show_my_flagged'] = False
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
        
        with col4:
            if advisor_id:
                st.write("**Send to Student**") if not show_sent_jobs else st.write("**Unsend to Student**")
                try:
                    # Fetch students associated with the advisor
                    students = get_students_for_advisor(advisor_id)
                    if students and isinstance(students, list):  # Check if students is a non-empty list
                        student_names = [student['StudentName'] for student in students]

                        # Display a dropdown with student names
                        selected_student = st.selectbox(
                            "Select a student to send this job:" if not show_sent_jobs else "Select a student to unsend this job:",
                            student_names,
                        key=f"student_select_{job['Job Listing ID']}"
                        )

                        # Button to "send" the job to the selected student
                        if st.button(f"Send Job to {selected_student}", key=f"send_button_{job['Job Listing ID']}") if not show_sent_jobs else st.button(f"Unsend Job to {selected_student}", key=f"unsend_button_{job['Job Listing ID']}"):
                            try:
                                payload = {
                                    'jobListingId': job['Job Listing ID'],
                                    'studentId': students[student_names.index(selected_student)]['StudentID'],
                                    'advisorId': advisor_id
                                }
                                # Send the payload and wait for the response
                                response = toggle_sent_job_listing(payload)

                                # Check the response status
                                st.success(f"Job {'sent' if not show_sent_jobs else 'unsent'} to {selected_student}!")
                            except Exception as e:
                                logger.error(f"Error toggling job listing: {e}")
                                st.error(f"An error occurred: {e}")
                    else:
                        st.error("No students found for this advisor.")
                except Exception as e:
                    st.error(f"Error fetching students: {e}")

        st.write("**Description**")
        st.write(job.get('Description', 'N/A'))

    # Delete modal
    if st.session_state[delete_modal_key]:
        delete_job_listing_modal(job['Job Listing ID'], delete_modal_key, deleted)

    # Edit modal
    if st.session_state[edit_modal_key]:
        edit_job_listing_modal(job, edit_modal_key)