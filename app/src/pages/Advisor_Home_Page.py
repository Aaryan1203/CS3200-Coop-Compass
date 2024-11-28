import streamlit as st
import logging
logger = logging.getLogger(__name__)
from modules.nav import SideBarLinks

# Set Streamlit page configuration for a modern, wide layout
st.set_page_config(
    layout="wide",
    page_title="Advisor Home",
    page_icon="🧑‍🏫"
)

# Apply custom CSS for consistent dark mode theme
st.markdown(
    """
    <style>
        /* Set the entire page background to black */
        body {
            background-color: #000000 !important;
            color: #e0e0e0 !important;
        }

        /* Main container background */
        .stApp {
            background-color: #000000 !important;
        }

        /* Title Styling */
        h1 {
            color: #0047AB !important; /* Darker blue for main title */
        }
        h3 {
            color: #0047AB !important; /* Darker blue for section headers */
        }

        /* Button Styling */
        div.stButton > button {
            background-color: #bb86fc !important; /* Blue-purple background */
            color: #000000 !important; /* Black text */
            border-radius: 5px !important;
            padding: 10px 20px !important;
            font-size: 1rem !important;
            border: none !important;
        }
        div.stButton > button:hover {
            background-color: #3700b3 !important; /* Darker purple-blue on hover */
            color: #ffffff !important; /* White text on hover */
        }

        /* General Text */
        p, div {
            color: #e0e0e0 !important; /* Light gray text for readability */
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome advisor, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('View my Students Reviews', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/02_Map_Demo.py')

if st.button('View my Students Analytics', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/01_World_Bank_Viz.py')

if st.button('View my Sent Job Listings', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/02_Map_Demo.py')