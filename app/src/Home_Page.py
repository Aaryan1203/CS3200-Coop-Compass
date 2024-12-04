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
from utils.style_utils import load_css

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

load_css("./styles/home_page_styles.css")

# Hero Section
st.markdown(
    """
    <div class="hero">
        <h1>Welcome to Co-op Compass 🎓</h1>
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
        st.session_state['advisor_id'] = False
        st.session_state['recruiter_id'] = False
        st.session_state['admin_id'] = False
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
        st.session_state['student_id'] = False
        st.session_state['advisor_id'] = False
        st.session_state['admin_id'] = False
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
        st.session_state['student_id'] = False
        st.session_state['recruiter_id'] = False
        st.session_state['admin_id'] = False
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
        st.session_state['advisor_id'] = False
        st.session_state['student_id'] = False
        st.session_state['recruiter_id'] = False
        st.session_state['admin_id'] = '1'

        st.switch_page("pages/Admin_Home_Page.py")
