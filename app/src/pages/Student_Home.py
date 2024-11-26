import streamlit as st
import requests
from modules.nav import SideBarLinks
from utils.routes import get_reviews_by_student
  # Importing the function

# Base API URL
BASE_API_URL = "http://api:4000"  # Assuming this works based on the given reference

# Set page configuration
st.set_page_config(
    layout="wide",
    page_title="Student Home",
    page_icon="🎓"
)

# Custom CSS for styling
st.markdown(
    """
    <style>
        body {
            background-color: #000000 !important;
            color: #e0e0e0 !important;
        }

        .stApp {
            background-color: #000000 !important;
        }

        .hero {
            text-align: center;
            padding: 20px;
            background-color: #1a1a1a;
            border-radius: 10px;
            margin-bottom: 20px;
        }

        .hero h1 {
            color: #0047AB;
            font-size: 2.5rem;
        }

        .hero h3 {
            color: #e0e0e0;
            font-size: 1.2rem;
        }

        .card {
            background-color: #1a1a1a;
            border-radius: 10px;
            padding: 20px;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.5);
            margin-bottom: 15px;
        }

        .card h3 {
            color: #bb86fc;
            margin-bottom: 10px;
        }

        .card p {
            color: #e0e0e0;
            margin-bottom: 20px;
        }

        .card:hover {
            background-color: #333333;
        }

        div.stButton > button {
            background-color: #0047AB !important;
            color: #ffffff !important;
            border-radius: 5px;
            padding: 10px 20px;
            border: none;
            font-size: 1rem;
        }

        div.stButton > button:hover {
            background-color: #003366 !important;
        }

        .preview {
            text-align: left;
            color: #e0e0e0;
            font-size: 0.9rem;
            margin-top: 10px;
            background-color: #1a1a1a;
            padding: 10px;
            border-radius: 5px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.5);
        }

        .preview h4 {
            color: #bb86fc;
            font-size: 1rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar Links
SideBarLinks()

# Add a hero section
st.markdown(
    """
    <div class="hero">
        <h1>Welcome, Aaryan</h1>
        <h3>What would you like to do today?</h3>
    </div>
    """,
    unsafe_allow_html=True
)

# Function to fetch data from API
def fetch_data(endpoint):
    """Fetch data from API and handle errors."""
    try:
        response = requests.get(f"{BASE_API_URL}{endpoint}")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        st.error(f"Error fetching data from {endpoint}: {e}")
        return []

# Fetch all data
companies = fetch_data("/j/companies")[:10]  # Limit to 10 companies
job_postings = fetch_data("/j/job_listings")[:10]  # Limit to 10 job postings

# Fetch reviews using the custom function
student_id = st.session_state.get("student_id", "100")  # Ensure student ID is set
all_reviews = get_reviews_by_student(student_id)[:10]  # Fetch all reviews and limit to 10

# Create a grid layout for the actions
cols = st.columns(3, gap="large")

# Companies Section
with cols[0]:
    st.markdown(
        """
        <div class="card">
            <h3>View All Companies</h3>
            <p>Explore a list of all the companies offering co-op opportunities.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("View All Companies", use_container_width=True):
        st.switch_page("pages/Companies.py")

    st.markdown(
        "<div class='preview'><h4>Preview:</h4><ul>" +
        "".join([f"<li>{c.get('Name', 'N/A')} - {c.get('Headline', 'No Headline')}</li>" for c in companies]) +
        "</ul></div>",
        unsafe_allow_html=True,
    )

# Job Postings Section
with cols[1]:
    st.markdown(
        """
        <div class="card">
            <h3>View All Job Postings</h3>
            <p>Browse through the latest job postings and find your next opportunity.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("View All Job Postings", use_container_width=True):
        st.switch_page("pages/Job_Listings.py")

    st.markdown(
        "<div class='preview'><h4>Preview:</h4><ul>" +
        "".join([f"<li>{jp.get('Job Title', 'N/A')} - {jp.get('Company', 'N/A')}</li>" for jp in job_postings]) +
        "</ul></div>",
        unsafe_allow_html=True,
    )

# Reviews Section
with cols[2]:
    st.markdown(
        """
        <div class="card">
            <h3>View My Reviews</h3>
            <p>See all of my reviews.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Add "View My Reviews" button below
    if st.button("View My Reviews", use_container_width=True, key="my_reviews_button"):
        st.session_state['job_listing_id'] = False
        st.session_state['student_id'] = '100'
        st.switch_page("pages/Reviews.py")

    # Preview section for reviews
    st.markdown(
        "<div class='preview'><h4>Preview:</h4><ul>" +
        "".join([f"<li>{r.get('Description', 'N/A')} - Satisfaction: {r.get('Job Satisfaction', 'N/A')}</li>" for r in all_reviews]) +
        "</ul></div>",
        unsafe_allow_html=True,
    )
