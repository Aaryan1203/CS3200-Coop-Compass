import streamlit as st
import logging
import pandas as pd
import matplotlib.pyplot as plt
from modules.nav import SideBarLinks
from utils.frontend_routes import (
    get_students_for_advisor,
    get_reviews_by_student,
    get_sent_job_listings_for_students,
)
from utils.style_utils import load_css

# Configure logging
logger = logging.getLogger(__name__)

# Set Streamlit page configuration for a modern, wide layout
st.set_page_config(
    layout="wide",
    page_title="Advisor Analytics",
    page_icon="📊"
)

# Apply custom CSS for consistent dark mode theme
load_css("./styles/advisor_analytics_styles.css")

# Retrieve Advisor ID from session state
advisor_id = st.session_state.get('advisor_id', None)

# Show appropriate sidebar links for the role of the currently logged-in user
SideBarLinks()

# Page Content
st.title("Advisor Analytics")
if advisor_id:
    try:
        # Fetch all students for the advisor
        students = get_students_for_advisor(advisor_id)

        if students:
            st.subheader("Student Analytics Overview")

            for student in students:
                try:
                    # Extract student details
                    student_id = student.get("StudentID", "Unknown")
                    student_name = student.get("StudentName", "Unknown")
                    student_email = student.get("StudentEmail", "Unknown")

                    st.markdown(f"""
                    <div class="student-info">
                        <strong>Student ID:</strong> {student_id} <br>
                        <strong>Name:</strong> {student_name} <br>
                        <strong>Email:</strong> {student_email} <br>
                    </div>
                    """, unsafe_allow_html=True)

                    # Fetch reviews for the student
                    reviews = get_reviews_by_student(student_id)
                    num_reviews = len(reviews)

                    # Calculate average job satisfaction
                    if reviews:
                        total_satisfaction = sum([review.get("Job Satisfaction", 0) for review in reviews])
                        avg_satisfaction = total_satisfaction / num_reviews
                    else:
                        avg_satisfaction = 0

                    # Fetch job listings sent to the student
                    sent_job_listings = get_sent_job_listings_for_students(student_id)
                    num_sent_job_listings = len(sent_job_listings)

                    # Display analytics
                    st.markdown(f"""
                    <div class="analytics">
                        <div><strong>Number of Reviews:</strong> {num_reviews}</div>
                        <div><strong>Average Job Satisfaction:</strong> {avg_satisfaction:.2f}</div>
                        <div><strong>Job Listings Sent:</strong> {num_sent_job_listings}</div>
                    </div>
                    """, unsafe_allow_html=True)

                except Exception as student_error:
                    st.markdown(f'<div class="error-message">Error processing student data: {student_error}</div>', unsafe_allow_html=True)

        else:
            st.markdown('<div class="error-message">No students found for this advisor.</div>', unsafe_allow_html=True)

    except Exception as e:
        st.markdown(f'<div class="error-message">Error fetching analytics: {e}</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="error-message">Advisor ID not found in session state.</div>', unsafe_allow_html=True)



# Prepare data for visualizations
student_names = [student.get("StudentName", "Unknown") for student in students]
num_reviews = [len(get_reviews_by_student(student.get("StudentID", 0))) for student in students]
avg_satisfaction = [
    sum(review.get("Job Satisfaction", 0) for review in get_reviews_by_student(student.get("StudentID", 0))) / max(len(get_reviews_by_student(student.get("StudentID", 0))), 1)
    for student in students
]
job_listings_sent = [len(get_sent_job_listings_for_students(student.get("StudentID", 0))) for student in students]

# Convert data to DataFrame for easier plotting
data = pd.DataFrame({
    "Student Name": student_names,
    "Number of Reviews": num_reviews,
    "Average Job Satisfaction": avg_satisfaction,
    "Job Listings Sent": job_listings_sent
})

# Visualize Number of Reviews
st.subheader("Number of Reviews by Student")
st.bar_chart(data.set_index("Student Name")["Number of Reviews"])

# Visualize Average Job Satisfaction
st.subheader("Average Job Satisfaction by Student")
st.bar_chart(data.set_index("Student Name")["Average Job Satisfaction"])

# Visualize Job Listings Sent
st.subheader("Job Listings Sent to Students")
fig, ax = plt.subplots()
ax.pie(
    job_listings_sent, 
    labels=student_names, 
    autopct='%1.1f%%', 
    startangle=90
)
ax.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
st.pyplot(fig)
