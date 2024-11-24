import streamlit as st
import logging
logger = logging.getLogger(__name__)
from components.search import search_bar
import requests
from modules.nav import SideBarLinks
from components.job_listing import job_listing_component
from modules.filter_functions import filter_job_listings

company_id = st.session_state.get('company_id', None)

if (company_id):
    try: 
        job_listings = requests.get(f'http://api:4000/j/job_listings/company/{company_id}').json()
        logger.info(f"Job Listings: {job_listings}")
        reviews = requests.get('http://api:4000/r/reviews').json()
    except:
        st.write("**Important**: Could not connect to API.")
else:
    try: 
        job_listings = requests.get('http://api:4000/j/job_listings').json()
        reviews = requests.get('http://api:4000/r/reviews').json()
    except:
        st.write("**Important**: Could not connect to API.")

SideBarLinks()

# Display
st.write(f"## Job Listings {' for ' + job_listings[0]['Company'] if company_id else ''}")

text_input = search_bar("Jobs")

if isinstance(job_listings, list):
    # Filtering the job_listings if the user has entered a search value
    filtered_job_listings = filter_job_listings(job_listings, text_input)

    for job in filtered_job_listings:
        # number of reviews per job
        num_reviews = len([review for review in reviews if review['Job Listing ID'] == job['Job Listing ID']])

        job_listing_component(job, num_reviews)
else:
    st.write("No job postings available.")
