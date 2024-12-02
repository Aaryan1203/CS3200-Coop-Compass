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

# Main Header
st.markdown('<h1 class="main-header">All Job Postings</h1>', unsafe_allow_html=True)

if isinstance(job_listings, list):
    if student_id:
        favorite_jobs = [
            job
            for job in job_listings
            if job["Job Listing ID"]
            in [fav["Job Listing ID"] for fav in favorite_job_listings]
        ]
        other_jobs = [
            job
            for job in job_listings
            if job["Job Listing ID"]
            not in [fav["Job Listing ID"] for fav in favorite_job_listings]
        ]

        # Favorite Job Listings Header
        if favorite_jobs:
            st.markdown(
                '<h2 class="sub-header">Favorite Job Postings</h2>',
                unsafe_allow_html=True,
            )
            for job in favorite_jobs:
                num_reviews = len(
                    [
                        review
                        for review in reviews
                        if review["Job Listing ID"] == job["Job Listing ID"]
                    ]
                )
                job_listing_component(job, num_reviews, student_id, advisor_id, is_favorite=True)

        # Other Job Listings Header
        st.markdown(
            '<h2 class="sub-header">Other Job Listings</h2>', unsafe_allow_html=True
        )
        text_input = search_bar("Jobs")  # Search bar below "Other Job Listings"
        filtered_jobs = filter_job_listings(other_jobs, text_input)
        for job in filtered_jobs:
            num_reviews = len(
                [
                    review
                    for review in reviews
                    if review["Job Listing ID"] == job["Job Listing ID"]
                ]
            )
            job_listing_component(job, num_reviews, student_id, advisor_id)
    if advisor_id:
        for job in job_listings:
            num_reviews = len(
                [
                    review
                    for review in reviews
                    if review["Job Listing ID"] == job["Job Listing ID"]
                ]
            )
            job_listing_component(job, num_reviews, student_id, advisor_id, isAdvisor=True)
else:
    st.write("No job postings available.")


