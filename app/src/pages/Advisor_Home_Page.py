import streamlit as st
import logging
logger = logging.getLogger(__name__)
from modules.nav import SideBarLinks
from utils.style_utils import load_css

# Set Streamlit page configuration for a modern, wide layout
st.set_page_config(
    layout="wide",
    page_title="Advisor Home",
    page_icon="🧑‍🏫"
)

load_css("./styles/advisor_home_page_styles.css")

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome advisor, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('View my Students Reviews', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/My_Students.py')

if st.button('View my Students Analytics', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/Advisor_Analytics.py')

if st.button('View my Sent Job Listings', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/Job_Listings_Page.py')

if st.button('View all Job Postings', 
             type='primary',
             use_container_width=True):
  st.session_state['company_id'] = False
  st.session_state['my_job_postings'] = False
  st.session_state['show_deleted'] = False
  st.switch_page('pages/Job_Listings_Page.py')