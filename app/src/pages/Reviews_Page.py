import streamlit as st
import logging
from modules.nav import SideBarLinks
from components.review import review_component
from utils.review_modals import create_review_modal
from utils.frontend_routes import get_reviews_for_job_listing
from utils.frontend_routes import get_reviews_by_student
from utils.frontend_routes import get_deleted_reviews

# Initialize session state for modals
if "create_modal" not in st.session_state:
    st.session_state["create_modal"] = False

job_listing_id = st.session_state.get('job_listing_id', None)
student_id = st.session_state.get('student_id', None)
show_deleted = st.session_state.get('show_deleted', None)

reviews = []
if job_listing_id:
    try: 
        reviews = get_reviews_for_job_listing(job_listing_id)
    except:
        st.write("**Important**: Could not connect to API.")
elif show_deleted:
    try:
        reviews = get_deleted_reviews()
    except:
        st.write("**Important**: Could not connect to API.")
else:
    try:
        reviews = get_reviews_by_student(student_id)
    except:
        st.write("**Important**: Could not connect to API.")

st.markdown(
    """
    <style>
        /* Remove the persistent white header */
        [data-testid="stHeader"] {
            display: none !important;
        }

        /* General page styling */
        body {
            background-color: #000000 !important;
            color: #ffffff !important; /* Ensure all text is white */
        }
        .stApp {
            background-color: #000000 !important;
            margin-top: -50px !important; /* Adjust page content position */
        }

        /* Sidebar styling */
        .css-1d391kg {
            background-color: #1a1a1a !important;
        }

        /* Header styling */
        h2.main-header {
            text-align: center !important;
            font-size: 2.5rem !important; /* Slightly larger font size */
            font-weight: bold !important;
            color: #ffffff !important; /* Pure white text */
            margin-top: 20px !important; /* Adjust spacing above */
            margin-bottom: 15px !important; /* Adjust spacing below */
        }
        h2.main-header::after {
            content: "";
            display: block;
            width: 90%; /* Underline width */
            height: 2px; /* Underline thickness */
            background-color: #ffffff !important; /* White underline */
            margin: 10px auto; /* Center the underline */
        }

        /* Card styling for reviews */
        [data-testid="stExpander"] {
            border: 1px solid #cccccc !important; /* Light grey border */
            border-radius: 10px !important;
            background-color: #1a1a1a !important; /* Dark grey background */
            margin-bottom: 10px !important;
        }

        /* Ensure text inside cards remains white */
        [data-testid="stExpander"] div, 
        [data-testid="stExpander"] span,
        textarea, input {
            color: #ffffff !important; /* Ensure text is always white */
            background-color: #1a1a1a !important; /* Background dark for inputs */
        }

        /* Button styling */
        div.stButton > button {
            background-color: #0047AB !important; /* Solid blue background */
            color: #ffffff !important; /* White text */
            border-radius: 5px !important;
            padding: 10px 20px !important;
            border: none !important;
            font-size: 1rem !important;
        }

        div.stButton > button:hover {
            background-color: #003366 !important; /* Slightly darker blue on hover */
            color: #ffffff !important;
        }

        /* Slider styling */
        [data-testid="stSlider"] .css-1wy0on6 {
            color: #ffffff !important; /* White slider label text */
        }

        /* Placeholder and input styling */
        textarea, input {
            color: #ffffff !important; /* Ensure text in inputs is white */
            background-color: #1a1a1a !important;
            border: 1px solid #ffffff !important; /* White border for input fields */
        }

        ::placeholder {
            color: #cccccc !important; /* Light grey placeholder text */
        }

        /* Ensure all text remains white globally */
        * {
            color: #ffffff !important;
        }

        /* General responsive design */
        @media (max-width: 768px) {
            h2.main-header {
                font-size: 2rem !important; /* Adjust header size */
            }
            [data-testid="stExpander"] {
                padding: 10px !important; /* Smaller padding for cards */
            }
        }
    </style>
    """,
    unsafe_allow_html=True,
)


SideBarLinks()

# Center and style the header
if job_listing_id:
    st.markdown('<h2 class="main-header">Reviews for Job</h2>', unsafe_allow_html=True)
elif show_deleted:
    st.markdown('<h2 class="main-header">Deleted Reviews</h2>', unsafe_allow_html=True)
else:
    st.markdown('<h2 class="main-header">My Reviews</h2>', unsafe_allow_html=True)

if job_listing_id:
    if st.button("Write a review"):
        st.session_state["create_modal"] = True

# Modal for writing a review
if st.session_state["create_modal"]:
    create_review_modal(job_listing_id, student_id)

if reviews:
    my_reviews = not job_listing_id
    for review in reviews:
        review_component(review, my_reviews=my_reviews)
else:
    st.write("No reviews available.")
