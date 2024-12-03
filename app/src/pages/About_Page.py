import streamlit as st
from modules.nav import SideBarLinks
from utils.style_utils import load_css

st.set_page_config(
    layout="wide",
    page_title="About Co-Op Compass",
    page_icon="🧠"
)

SideBarLinks()

# Apply custom CSS
load_css("./styles/about_page_styles.css")

st.title("About Co-Op Compass")
st.markdown (
    """
    This is a demo app for CS 3200 Course Project.  

    The goal of this demo is to provide information on the tech stack 
    being used as well as demo some of the features of the various platforms. 

    Stay tuned for more information and features to come!
    """
)
