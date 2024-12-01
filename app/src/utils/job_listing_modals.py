import streamlit as st
from utils.frontend_routes import get_all_companies
from utils.frontend_routes import create_job_listing
from utils.frontend_routes import edit_job_listing
from utils.frontend_routes import toggle_delete_job_listing
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

def create_job_listing_modal(recruiter_id):
    companies = get_all_companies()
    company_names = [company["Name"] for company in companies]

    st.write("### Create a Job Listing")
    job_title = st.text_input("Job Title")
    description = st.text_area("Description")
    start_date = st.date_input("Start Date", value=datetime.now())
    end_date = st.date_input("End Date", value=datetime.now())
    wage = st.number_input("Wage")
    skills = st.text_input("Skills")
    location = st.text_input("Location")
    company = st.selectbox("Company", options=company_names)
    company = next((item for item in companies if item["Name"] == company), None)
    col1, col2 = st.columns(2)
    with col1:
        submit = st.button("Create Job Listing")
    with col2:
        if st.button("Cancel"):
            st.session_state["create_modal"] = False

    if submit:
        formatted_start_date = start_date.strftime("%Y-%m-%d")
        formatted_end_date = end_date.strftime("%Y-%m-%d")
        payload = {
            "jobTitle": job_title,
            "description": description,
            "startDate": formatted_start_date,
            "endDate": formatted_end_date,
            "wage": wage,
            "skills": skills,
            "location": location,
            "companyId": company['Company ID'],
            "recruiterId": recruiter_id,
        }
        logger.info(f"Payload: {payload}")
        create_job_listing(payload)
        st.success("Job Listing created.")
        st.session_state["create_modal"] = False
    
def edit_job_listing_modal(job_listing, edit_modal_key):
    st.write("### Edit Job Listing")
    new_job_title = st.text_input("Job Title", value=job_listing['Job Title'])
    new_description = st.text_area("Description", value=job_listing['Description'])

    start_date = datetime.strptime(job_listing['Start Date'], "%a, %d %b %Y %H:%M:%S %Z").date()
    end_date = datetime.strptime(job_listing['End Date'], "%a, %d %b %Y %H:%M:%S %Z").date()

    new_start_date = st.date_input("Start Date", value=start_date)
    new_end_date = st.date_input("End Date", value=end_date)
    new_wage = st.number_input("Wage", value=job_listing['Hourly Wage'])
    new_skills = st.text_input("Skills", value=job_listing['Skills'])
    new_location = st.text_input("Location", value=job_listing['Location'])
    col1, col2 = st.columns(2)
    with col1:
        submit = st.button("Save Changes")
    with col2:
        if st.button("Cancel"):
            st.session_state[edit_modal_key] = False

    if submit:
        formatted_start_date = new_start_date.strftime("%Y-%m-%d")
        formatted_end_date = new_end_date.strftime("%Y-%m-%d")
        payload = {
            "jobListingId": job_listing['Job Listing ID'],
            "jobTitle": new_job_title,
            "description": new_description,
            "startDate": formatted_start_date,
            "endDate": formatted_end_date,
            "hourlyWage": new_wage,
            "skills": new_skills,
            "location": new_location,
        }
        logger.info(f"Payload: {payload}")
        edit_job_listing(payload)
        st.success("Job Listing updated successfully.")
        st.session_state[edit_modal_key] = False

def delete_job_listing_modal(job_listing_id, delete_modal_key, deleted):
    st.write("### Are you sure you want to delete this job listing?")
    if (st.button("Confirm Delete") if not deleted else st.button("Restore Job Listing")):
        toggle_delete_job_listing(job_listing_id)
        st.success("Job Listing deleted successfully.") if not deleted else st.success("Job Listing restored successfully.")
        st.session_state[delete_modal_key] = False
    if st.button("Cancel"):
        st.session_state[delete_modal_key] = False