##################################################
# Enhanced Streamlit Homepage for Coop Compass (Dark Mode)
##################################################

# Set up basic logging infrastructure
import logging
logging.basicConfig(format='%(filename)s:%(lineno)s:%(levelname)s -- %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Import Streamlit and the SideBarLinks function
import streamlit as st
from modules.nav import SideBarLinks

# Set Streamlit page configuration for a modern look
st.set_page_config(
    page_title="Coop Compass",
    page_icon="🎓",
    layout="wide"
)

# Initialize session state variables
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

# Use SideBarLinks to configure the navigation sidebar
SideBarLinks()

# ***************************************************
#    The Major Content of the Page (Dark Mode)
# ***************************************************

st.markdown(
    """
    <style>
        /* Remove white space at the top by targeting Streamlit header */
        [data-testid="stHeader"] {
            margin: 0 !important;
            padding: 0 !important;
            background: none !important; /* Remove unnecessary background */
        }

        /* Adjust block container for content */
        .block-container {
            padding-top: 2rem !important; /* Restore top padding for content */
            padding-left: 1rem !important;
            padding-right: 1rem !important;
        }

        /* Set the entire page background to black */
        body {
            background-color: #000000 !important;
            color: #e0e0e0;
        }

        /* Change the main app container background to black */
        .stApp {
            background-color: #000000 !important;
        }
        
        /* Hero Section Styling */
        .hero {
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px 20px;
            background-color: #1a1a1a; /* Lighter black/gray */
            border-radius: 15px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.5);
            margin-bottom: 2rem;
        }
        .hero h1 {
            color: #bb86fc;
            font-size: 3rem;
            margin-bottom: 20px;
        }
        .hero p {
            color: #e0e0e0;
            font-size: 1.2rem;
        }

        /* Markdown Styling */
        .stMarkdown h3 {
            color: #bb86fc !important; /* Light purple */
            font-size: 1.5rem !important;
            font-weight: bold !important;
            text-align: center;
        }

        /* Card Styling for User Personas */
        .card {
            background-color: #1a1a1a; /* Lighter black/gray */
            border-radius: 10px;
            padding: 20px;
            margin: 10px 0;
            text-align: center;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.5);
        }
        .card h3 {
            color: #bb86fc;
            margin-bottom: 10px;
        }
        .card p {
            color: #e0e0e0;
        }
        
        /* Footer Styling */
        .footer {
            text-align: center;
            font-size: 0.9rem;
            color: #7f8c8d;
            margin-top: 50px;
        }
        
        /* Button Styling */
        button {
            background-color: #bb86fc;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            color: #121212;
            font-size: 1rem;
            cursor: pointer;
        }
        button:hover {
            background-color: #3700b3;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Hero Section
st.markdown(
    """
    <div class="hero">
        <h1>Welcome to Coop Compass 🎓</h1>
        <p>Your one-stop platform for navigating co-op opportunities!</p>
    </div>
    """,
    unsafe_allow_html=True
)



# Add user persona cards for a better visual layout
st.write('\n\n')
st.markdown("### 👤 Select a User Persona:")
cols = st.columns(2, gap="large")

with cols[0]:
    st.markdown(
        """
        <div class="card">
            <h3>Aaryan</h3>
            <p>Student on a co-op search with one previous co-op</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("Login as Aaryan", type='primary', use_container_width=True):
        st.session_state['authenticated'] = True
        st.session_state['role'] = 'student'
        st.session_state['first_name'] = 'Aaryan'
        st.session_state['student_id'] = '100'
        st.switch_page("pages/Student_Home_Page.py")

with cols[1]:
    st.markdown(
        """
        <div class="card">
            <h3>Quandale</h3>
            <p>Recruiter at a company</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("Login as Quandale", type='primary', use_container_width=True):
        st.session_state['authenticated'] = True
        st.session_state['role'] = 'recruiter'
        st.session_state['first_name'] = 'Quandale'
        st.session_state['recruiter_id'] = '0'
        st.switch_page("pages/Recruiter_Home_Page.py")

cols = st.columns(2, gap="large")

with cols[0]:
    st.markdown(
        """
        <div class="card">
            <h3>Rachel</h3>
            <p>Co-op Advisor</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("Login as Rachel", type='primary', use_container_width=True):
        st.session_state['authenticated'] = True
        st.session_state['role'] = 'advisor'
        st.session_state['first_name'] = 'Rachel'
        st.session_state['advisor_id'] = '1'
        st.switch_page("pages/Advisor_Home_Page.py")

with cols[1]:
    st.markdown(
        """
        <div class="card">
            <h3>Sam</h3>
            <p>Admin of the app</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("Login as Sam", type='primary', use_container_width=True):
        st.session_state['authenticated'] = True
        st.session_state['role'] = 'admin'
        st.session_state['first_name'] = 'Sam'
        st.switch_page("pages/Admin_Home_Page.py")
