import streamlit as st
import logging
logger = logging.getLogger(__name__)
from components.search import search_bar
import requests
from modules.nav import SideBarLinks
from components.job_listing import job_listing_component
from modules.filter_functions import filter_job_listings
from utils.frontend_routes import get_job_listings_by_company
from utils.frontend_routes import get_all_job_listings
from utils.frontend_routes import get_all_reviews
from utils.job_listing_modals import create_job_listing_modal
from utils.frontend_routes import get_job_listings_by_recruiter

# Initialize session state for modals
if "create_modal" not in st.session_state:
    st.session_state["create_modal"] = False

company_id = st.session_state.get('company_id', None)
recruiter_id = st.session_state.get('recruiter_id', None)
my_job_postings = st.session_state.get('my_job_postings', None)

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
else:
    try: 
        job_listings = get_all_job_listings()
    except:
        st.write("**Important**: Could not connect to API.")

try:
    reviews = get_all_reviews()
except:
    st.write("**Important**: Could not connect to API.")
SideBarLinks()

col1, col2 = st.columns(2)

# Display
with col1:
    if my_job_postings:
        st.write("## My Job Postings")
    elif company_id:
        st.write(f"## Job Postings for {job_listings[0]['Company']}")
    else:
        st.write("## All Job Postings")
with col2:
    if recruiter_id:
        if st.button("Create a new job listing"):
            st.session_state["create_modal"] = True

# Modal for writing a review
if st.session_state["create_modal"]:
    create_job_listing_modal(recruiter_id)

text_input = search_bar("Jobs")

if isinstance(job_listings, list):
    filtered_job_listings = filter_job_listings(job_listings, text_input)

    for job in filtered_job_listings:
        num_reviews = len([review for review in reviews if review['Job Listing ID'] == job['Job Listing ID']])

        job_listing_component(job, num_reviews, my_job_postings=my_job_postings)
else:
    st.write("No job postings available.")
