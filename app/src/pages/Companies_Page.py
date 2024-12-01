import streamlit as st
import logging
logger = logging.getLogger(__name__)
import requests
from modules.nav import SideBarLinks
from components.search import search_bar
from components.company import company_component
from modules.filter_functions import filter_companies
from utils.frontend_routes import get_all_companies
from utils.frontend_routes import get_all_job_listings

try: 
    companies = get_all_companies()
    job_listings = get_all_job_listings()
except:
    st.write("**Important**: Could not connect to API.")


st.markdown(
    """
    <style>
        /* Remove the white header at the top */
        [data-testid="stHeader"] {
            margin: 0 !important;
            padding: 0 !important;
            background: none !important;
        }

        /* Set background color for the entire page */
        body {
            background-color: #000000 !important;
            color: #e0e0e0 !important; /* Default text color to white */
        }

        /* Main app background */
        .stApp {
            background-color: #000000 !important;
        }

        /* Sidebar styling */
        .css-1d391kg {
            background-color: #1a1a1a !important;
        }

        /* Global text override to force white */
        * {
            color: #e0e0e0 !important; /* Universal text color to white */
            text-shadow: none !important;
        }

        /* Refined Header Styling */
        h1 {
            text-align: center !important; /* Center-align the header */
            font-weight: 600 !important; /* Slightly lighter font weight */
            padding: 5px 0 !important; /* Adjusted padding */
            margin-top: -10px !important; /* Keep header in its current position */
            margin-bottom: 50px !important; /* Add space below the header */
            background-color: #1a1a1a !important; /* Subtle dark background */
            border-radius: 10px !important; /* Rounded edges */
        }

        /* Thinner and centered divider line */
        h1::after {
            content: "";
            display: block;
            width: 50%; /* Make the line shorter */
            height: 1px !important; /* Reduce thickness */
            background-color: #ffffff !important; /* Line color changed to white */
            margin: 10px auto 20px; /* Add extra spacing below the divider */
        }

        /* Add light grey outline for ALL container sections */
        [data-testid="stExpander"] {
            border: 1px solid #cccccc !important; /* Light grey outline */
            border-radius: 10px !important;
            padding: 15px !important;
            background-color: #1a1a1a !important;
            margin-bottom: 10px !important; /* Reduced spacing between cards */
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3) !important; /* Sharper shadow */
        }

        /* Add alternating background colors for boxes */
        [data-testid="stExpander"]:nth-child(odd) {
            background-color: #252525 !important; /* Slightly lighter background for odd boxes */
        }

        [data-testid="stExpander"]:nth-child(even) {
            background-color: #1a1a1a !important; /* Default for even boxes */
        }

        /* Add hover effect to entire card */
        [data-testid="stExpander"]:hover {
            background-color: #333333 !important; /* Change background on hover */
        }

        /* Make the company name blue on hover */
        [data-testid="stExpander"]:hover div,
        [data-testid="stExpander"]:hover span,
        [data-testid="stExpander"]:hover * {
            color: #0047AB !important; /* Change company name to blue */
        }

        /* Smooth transition for hover effect */
        [data-testid="stExpander"] div,
        [data-testid="stExpander"] span,
        [data-testid="stExpander"] * {
            transition: color 0.3s ease-in-out !important; /* Smooth transition */
        }

        /* Links and buttons */
        a, div.stButton > button {
            color: #bb86fc !important;
        }
        div.stButton > button {
            background-color: #0047AB !important;
            border: none !important;
            padding: 10px 20px !important;
            border-radius: 5px !important;
            transition: all 0.3s ease-in-out !important; /* Smooth hover transition */
        }
        div.stButton > button:hover {
            transform: scale(1.05) !important; /* Slightly enlarge button on hover */
            background-color: #003366 !important; /* Darker blue hover effect */
        }

        /* Dropdowns and other input fields */
        .css-1cpxqw2, .css-1n543e5, .css-2hb19z {
            color: #000000 !important; /* Make input text black */
            background-color: #ffffff !important; /* Background color */
        }

        /* General input styling (including the search bar) */
        input {
            color: #000000 !important; /* Make text black */
            background-color: #ffffff !important; /* Ensure white background */
        }

        /* Placeholder text */
        ::placeholder {
            color: #000000 !important; /* Placeholder text color */
            opacity: 1 !important;
        }

        /* Smooth animations for expanding sections */
        [data-testid="stExpander"] > div {
            transition: all 0.3s ease-in-out !important; /* Smooth expand/collapse */
        }

        /* Ensure white text for Markdown-rendered content */
        .stMarkdown, .stMarkdown div, .stMarkdown span {
            color: #e0e0e0 !important;
        }

        /* Make the page responsive */
        @media (max-width: 768px) {
            h1 {
                font-size: 1.8rem !important; /* Smaller header font size for mobile */
            }

            [data-testid="stExpander"] {
                padding: 10px !important; /* Reduce padding */
                margin-bottom: 5px !important; /* Even less margin between boxes for mobile */
            }
        }
    </style>
    """,
    unsafe_allow_html=True,
)






SideBarLinks()

st.write("# Companies")

text_input = search_bar("Companies")

# Check if companies is valid
if isinstance(companies, list):
    
    filtered_companies = filter_companies(companies, text_input)

    for company in filtered_companies:
        # number of job listings per company
        num_job_listings = len([job for job in job_listings if job['Company ID'] == company['Company ID']])
        company_component(company, num_job_listings)

else:
    st.write("No companies available.")
