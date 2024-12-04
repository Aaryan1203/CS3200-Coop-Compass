import streamlit as st
import requests
import logging
logger = logging.getLogger(__name__)


BASE_API_URL = "http://api:4000"

# Function to fetch data from API
def fetch_data(endpoint):
    """Fetch data from API and handle errors."""
    try:
        response = requests.get(f"{BASE_API_URL}{endpoint}")
        logging.info(f"Fetching data from {BASE_API_URL}/{endpoint}")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        st.error(f"Error fetching data from {endpoint}: {e}")
        return []

def create_data(endpoint, data):
    """Create data in the API and handle errors."""
    try:
        response = requests.post(f"{BASE_API_URL}{endpoint}", json=data)
        logging.info(f"Creating data in {BASE_API_URL}/{endpoint}")
        response.raise_for_status()
        logger.info(f"Responseeeeee: {response.json()}")
        return response.json()
    except requests.RequestException as e:
        st.error(f"Error creating data in {endpoint}: {e}")
        return []

def edit_data(endpoint, data):
    """Edit data in the API and handle errors."""
    try:
        response = requests.put(f"{BASE_API_URL}{endpoint}", json=data)
        logging.info(f"Editing data in {BASE_API_URL}/{endpoint}")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        st.error(f"Error editing data in {endpoint}: {e}")
        return []
    
def delete_data(endpoint):
    """Delete data in the API and handle errors."""
    try:
        response = requests.put(f"{BASE_API_URL}{endpoint}")
        logging.info(f"Deleting data in {BASE_API_URL}/{endpoint}")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        st.error(f"Error deleting data in {endpoint}: {e}")
        return []

#----------------- Companies -----------------#

def get_all_companies():
    return fetch_data('/c/companies')

#----------------- Job Listings -----------------#

def get_all_job_listings():
    return fetch_data('/j/job_listings')

def get_job_listing_by_id(job_listing_id):
    return fetch_data(f'/j/job_listing/{job_listing_id}')

def get_job_listings_by_recruiter(recruiter_id):
    return fetch_data(f'/j/job_listings/recruiter/{recruiter_id}')

def get_job_listings_by_company(company_id):
    return fetch_data(f'/j/job_listings/company/{company_id}')

def get_favorite_job_listings(student_id):
    return fetch_data(f'/j/job_listings/favorite/{student_id}')

def get_deleted_job_listings():
    return fetch_data('/j/job_listings/deleted')

def toggle_favorite_job_listing(data):
    return create_data('/m/job_listing/favorite', data)

def create_job_listing(data):
    return create_data('/j/job_listing', data)

def edit_job_listing(data):
    return edit_data('/j/job_listing', data)

def toggle_delete_job_listing(job_listing_id):
    return delete_data(f'/j/job_listing/{job_listing_id}')

def toggle_sent_job_listing(data):
    return create_data('/m/job_listing/sent', data)

def get_sent_job_listings(advisor_id):
    return fetch_data(f'/j/job_listings/sent/{advisor_id}')

def get_received_job_listings(student_id):
    return fetch_data(f'/j/job_listings/received/{student_id}')


#----------------- Reviews -----------------#

def get_all_reviews():
    return fetch_data('/r/reviews')
    
def get_reviews_for_job_listing(job_listing_id):
    return fetch_data(f'/r/reviews/{job_listing_id}')

def get_reviews_by_student(student_id):
    return fetch_data(f'/r/reviews/student/{student_id}')

def get_deleted_reviews():
    return fetch_data('/r/reviews/deleted')

def get_flagged_reviews():
    return fetch_data('/m/reviews/flagged')

def create_review(data):
    return create_data('/r/review', data)

def edit_review(data):
    return edit_data('/r/review', data)

def flag_review(data):
    return create_data('/r/review/flag', data)

def toggle_delete_review(review_id):
    return delete_data(f'/r/review/{review_id}')

def unflag_review(review_id):
    return delete_data(f'/m/review/unflag/{review_id}')

#----------------- Advisors -----------------#

def get_students_for_advisor(advisor_id):
    return fetch_data(f'/m/students/advisor/{advisor_id}')

def get_sent_job_listings_for_students(student_id):
    """Fetch all job listings sent to a specific student."""
    return fetch_data(f"/j/job_listings/received/{student_id}")


#----------------- Recruiter Analytics -----------------#

def get_recruiter_analytics(recruiter_id):
    return fetch_data(f'/r/recruiter/{recruiter_id}/analytics')