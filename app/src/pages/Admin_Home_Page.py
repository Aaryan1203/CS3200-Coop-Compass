import streamlit as st
import logging
logger = logging.getLogger(__name__)
from modules.nav import SideBarLinks
from utils.style_utils import load_css

st.set_page_config(
    layout="wide",
    page_title="Admin Home",
    page_icon="🛠️"
)

# Apply custom CSS for consistent dark mode theme

load_css("./styles/admin_home_page_styles.css")

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome admin, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('View all Companies', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/Companies_Page.py')

if st.button('View all Job Postings', 
             type='primary',
             use_container_width=True):
  st.session_state['my_job_postings'] = False
  st.session_state['show_deleted'] = False
  st.switch_page('pages/Job_Listings_Page.py')

if st.button('View all Deleted Job Postings', 
             type='primary',
             use_container_width=True):
  st.session_state['my_job_postings'] = False
  st.session_state['show_deleted'] = True
  st.switch_page('pages/Job_Listings_Page.py')

if st.button('View all Flagged Reviews', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/01_World_Bank_Viz.py')

if st.button('View all Deleted Reviews', 
             type='primary',
             use_container_width=True):
  st.session_state['show_deleted'] = True
  st.session_state['job_listing_id'] = False
  st.switch_page('pages/Reviews_Page.py')