import streamlit as st
import logging
from modules.nav import SideBarLinks
from utils.frontend_routes import get_students_for_advisor
from utils.frontend_routes import get_reviews_by_student
from components.student import student_component
from utils.style_utils import load_css

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Set page layout
st.set_page_config(layout='wide')


load_css("./styles/my_students_styles.css")


# Sidebar navigation
SideBarLinks()

advisor_id = st.session_state["advisor_id"]

students = []
try:
    response = get_students_for_advisor(advisor_id)
except:
    st.write("**Important**: Could not connect to API.")

# Page Title
st.title(f"Here are your Students' Reviews!")
st.write('')
st.write('### Students assigned to you:')

# Search bar for filtering students
search_input = st.text_input("Search Students", placeholder="Enter student name or email")

def filter_students(students, query):
    query = query.lower()
    return [
        student for student in students
        if query in student["name"].lower() or query in student["Email"].lower()
    ]

filtered_students = filter_students(students, search_input) if search_input else students

if response:
    for student in response:
        student_component(student)
else:
    st.write("## My Reviews")
