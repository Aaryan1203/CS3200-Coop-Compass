import streamlit as st
import logging
logger = logging.getLogger(__name__)
from modules.nav import SideBarLinks
from utils.frontend_routes import get_recruiter_analytics
from utils.style_utils import load_css

# Set Streamlit page configuration for a modern, wide layout
st.set_page_config(
    layout="wide",
    page_title="Recruiter Analytics",
)

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()