import streamlit as st
from utils.style_utils import load_css


#### ------------------------ General ------------------------
def HomeNav():
    st.sidebar.page_link("Home_Page.py", label="Home", icon="🏠")


def AboutPageNav():
    st.sidebar.page_link("pages/About_Page.py", label="About", icon="🧠")


#### ------------------------ Role of Student ------------------------
def StudentHomeNav():
    st.sidebar.page_link(
        "pages/Student_Home_Page.py", label="Student Home", icon="👤"
    )

#### ------------------------ Role of Recruiter ------------------------
def RecruiterHomeNav():
    st.sidebar.page_link(
        "pages/Recruiter_Home_Page.py", label="Recruiter Home", icon="👤"
    )

#### ------------------------ Role of Advisor ------------------------
def AdvisorHomeNav():
    st.sidebar.page_link(
        "pages/Advisor_Home_Page.py", label="Advisor Home", icon="👤"
    )

#### ------------------------ Role of Admin ------------------------
def AdminHomeNav():
    st.sidebar.page_link(
        "pages/Admin_Home_Page.py", label="Admin Home", icon="👤"
    )

# --------------------------------Links Function -----------------------------------------------
def SideBarLinks():
    """
    This function handles adding links to the sidebar of the app based upon the logged-in user's role,
    which was put in the streamlit session_state object when logging in.
    """

    # Add CSS for dark sidebar theme with forced white text for all elements

    load_css("./styles/nav_styles.css")

    st.sidebar.image("assets/Coop Compass Logo.png", width=300)

    # If there is no logged-in user, redirect to the Home (Landing) page
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        st.switch_page("Home_Page.py")

    if not st.session_state["authenticated"]:
        HomeNav()

    # Show the other page navigators depending on the user's role
    if st.session_state["authenticated"]:

        if st.session_state["role"] == "student":
            StudentHomeNav()

        if st.session_state["role"] == "recruiter":
            RecruiterHomeNav()

        # If the user is an advisor, give them access to the advisor pages
        if st.session_state["role"] == "advisor":
            AdvisorHomeNav()

        # If the user is an admin, give them access to the admin pages
        if st.session_state["role"] == "admin":
            AdminHomeNav()

    # Always show the About page at the bottom of the list of links
    AboutPageNav()

    if st.session_state["authenticated"]:
        # Always show a logout button if there is a logged-in user
        if st.sidebar.button("Logout"):
            del st.session_state["role"]
            del st.session_state["authenticated"]
            st.switch_page("Home_Page.py")
