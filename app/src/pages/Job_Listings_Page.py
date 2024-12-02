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

st.markdown(
    """
    <style>
        /* Remove the persistent white header */
        [data-testid="stHeader"] {
            display: none !important;
        }

        /* General page and text styling */
        body {
            background-color: #000000 !important;
            color: #ffffff !important; /* Ensure all text is pure white */
        }
        .stApp {
            background-color: #000000 !important;
            margin-top: -50px !important; /* Remove unnecessary top margin */
        }

        /* Sidebar styling */
        .css-1d391kg {
            background-color: #1a1a1a !important;
        }

        /* Main header styling */
        h1.main-header {
            text-align: center;
            font-size: 3.5rem;
            font-weight: bold;
            color: #ffffff !important; /* Pure white text */
            margin-top: 20px;
            margin-bottom: 10px;
        }
        h1.main-header::after {
            content: "";
            display: block;
            width: 90%;
            height: 2px;
            background-color: #ffffff !important; /* White underline */
            margin: 10px auto;
        }

        /* Sub-header styling */
        h2.sub-header {
            text-align: center;
            font-size: 2rem;
            font-weight: bold;
            color: #ffffff !important; /* Pure white text */
            margin-top: 30px;
            margin-bottom: 10px;
        }
        h2.sub-header::after {
            content: "";
            display: block;
            width: 60%;
            height: 1.5px;
            background-color: #ffffff !important; /* White underline */
            margin: 5px auto;
        }

        /* Search bar styling */
        .css-1cpxqw2, .css-1n543e5, .css-2hb19z {
            color: #000000 !important; /* Black text inside input fields */
            background-color: #ffffff !important; /* White background */
            border: 1px solid #cccccc;
            border-radius: 5px;
        }

        /* Placeholder text inside the search bar */
        ::placeholder {
            color: #666666 !important; /* Grey placeholder */
            opacity: 1;
        }

        /* Label styling (e.g., "Search for Jobs?") */
        label {
            color: #ffffff !important; /* Pure white text for labels */
        }

        /* Job listing cards */
        [data-testid="stExpander"] {
            border: 1px solid #cccccc !important; /* Light grey border */
            border-radius: 10px !important;
            background-color: #1a1a1a !important; /* Dark grey background */
            margin-bottom: 10px !important;
        }

        /* Alternating background for cards */
        [data-testid="stExpander"]:nth-child(odd) {
            background-color: #252525 !important; /* Slightly lighter grey */
        }

        [data-testid="stExpander"]:nth-child(even) {
            background-color: #1a1a1a !important; /* Default dark grey */
        }

        /* Hover effect for cards */
        [data-testid="stExpander"]:hover {
            background-color: #333333 !important; /* Darker grey on hover */
        }

        /* Ensure card text remains white */
        [data-testid="stExpander"] div, 
        [data-testid="stExpander"] span {
            color: #ffffff !important; /* Ensure card text is pure white */
        }

        /* Button styling */
        div.stButton > button {
            background-color: #0047AB !important;
            color: #ffffff !important;
            border-radius: 5px !important;
            padding: 10px 20px !important;
            border: none;
            font-size: 1rem;
        }

        div.stButton > button:hover {
            background-color: #003366 !important;
        }

        /* Responsive adjustments */
        @media (max-width: 768px) {
            h1.main-header {
                font-size: 2.5rem !important; /* Adjust main header size */
            }
            h2.sub-header {
                font-size: 1.8rem !important; /* Adjust sub-header size */
            }
        }
    </style>
    """,
    unsafe_allow_html=True,
)


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


