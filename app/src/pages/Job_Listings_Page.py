import streamlit as st
import logging

logger = logging.getLogger(__name__)
from components.search import search_bar
from modules.nav import SideBarLinks
from components.job_listing import job_listing_component
from modules.filter_functions import filter_job_listings
from utils.frontend_routes import (
    get_job_listings_by_company,
    get_all_job_listings,
    get_all_reviews,
    get_job_listings_by_recruiter,
    get_favorite_job_listings,
    get_deleted_job_listings,
    get_received_job_listings,
    get_sent_job_listings
)
from utils.job_listing_modals import create_job_listing_modal
from utils.style_utils import load_css

# Initialize session state for modals
if "create_modal" not in st.session_state:
    st.session_state["create_modal"] = False

advisor_id = st.session_state.get("advisor_id", None)
company_id = st.session_state.get("company_id", None)
recruiter_id = st.session_state.get("recruiter_id", None)
my_job_postings = st.session_state.get("my_job_postings", None)
student_id = st.session_state.get("student_id", None)
admin_id = st.session_state.get("admin_id", None)
deleted = st.session_state.get("show_deleted", None)
show_sent_jobs = st.session_state.get("show_sent_jobs", None)
show_recieved_jobs = st.session_state.get("show_recieved_jobs", None)

if my_job_postings:
    try:
        job_listings = get_job_listings_by_recruiter(recruiter_id)
    except:
        st.write("**Important**: Could not connect to API.")
elif company_id:
    try:
        job_listings = get_job_listings_by_company(company_id)
    except:
        st.write("**Important**: Could not connect to API.")
elif deleted:
    try:
        job_listings = get_deleted_job_listings()
    except:
        st.write("**Important**: Could not connect to API.")
elif show_sent_jobs:
    try:
        job_listings = get_sent_job_listings(advisor_id)
    except:
        st.write("**Important**: Could not connect to API.")
elif show_recieved_jobs:
    try:
        job_listings = get_received_job_listings(student_id)
    except:
        st.write("**Important**: Could not connect to API.")
else:
    try:
        job_listings = get_all_job_listings()
    except:
        st.write("**Important**: Could not connect to API.")

try:
    reviews = get_all_reviews()
    favorite_job_listings = (
        get_favorite_job_listings(student_id) if student_id else []
    )
    logger.info(f"Favorite jobs: {favorite_job_listings}")
except:
    st.write("**Important**: Could not connect to API.")

load_css("./styles/job_listings_page_styles.css")

SideBarLinks()

# Display
if my_job_postings:
    st.write("# My Job Postings")
elif company_id:
    st.write(f"# Job Postings for {job_listings[0]['Company']}")
elif deleted:
    st.write("# Deleted Job Postings")
elif show_sent_jobs:
    st.write("# Sent Job Postings")
elif show_recieved_jobs:
    st.write("# Recieved Job Postings")
elif admin_id:
    st.write(f"# All Job Postings")
else:
    st.write("# All Job Postings")

if recruiter_id:
    if st.button("Create a new job listing"):
        st.session_state["create_modal"] = True
        
# Modal for writing a review
if st.session_state["create_modal"]:
    create_job_listing_modal(recruiter_id)
text_input = search_bar("Jobs")
# Extract just the 'Job Listing ID' values from favorite_job_listings
favorite_job_ids = [fav['Job Listing ID'] for fav in favorite_job_listings]

if isinstance(job_listings, list):
    # Filter job listings based on search input
    filtered_job_listings = filter_job_listings(job_listings, text_input)
    logger.info(f"Student ID: {student_id}")
    if student_id:
        favorite_jobs = [job for job in filtered_job_listings if job['Job Listing ID'] in favorite_job_ids]
        other_jobs = [job for job in filtered_job_listings if job['Job Listing ID'] not in favorite_job_ids]
        # Display favorite job listings
        if favorite_jobs:
            st.write("## Favorite Job Listings")
            for job in favorite_jobs:
                num_reviews = len([review for review in reviews if review['Job Listing ID'] == job['Job Listing ID']])
                job_listing_component(job, num_reviews, student_id, advisor_id, my_job_postings=my_job_postings, is_favorite=True, show_sent_jobs=show_sent_jobs)
        
        # Display other job listings
        if other_jobs:
            st.write("## Other Job Listings")
            for job in other_jobs:
                num_reviews = len([review for review in reviews if review['Job Listing ID'] == job['Job Listing ID']])
                job_listing_component(job, num_reviews, student_id, advisor_id, my_job_postings=my_job_postings, is_favorite=False, show_sent_jobs=show_sent_jobs)
    else:
        allow_edit = my_job_postings or admin_id
        for job in filtered_job_listings:
            num_reviews = len([review for review in reviews if review['Job Listing ID'] == job['Job Listing ID']])
            job_listing_component(job, num_reviews, student_id, advisor_id, my_job_postings=allow_edit, deleted=deleted, show_sent_jobs=show_sent_jobs)
else:
    st.write("No job postings available.")
