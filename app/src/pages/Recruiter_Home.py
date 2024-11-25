import streamlit as st
import logging
logger = logging.getLogger(__name__)
from modules.nav import SideBarLinks


st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome recruiter, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('View all Companies', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/Companies.py')

if st.button('View all Job Postings', 
             type='primary',
             use_container_width=True):
  st.session_state['company_id'] = False
  st.switch_page('pages/Job_Listings.py')

if st.button('View my Job Postings', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/02_Map_Demo.py')