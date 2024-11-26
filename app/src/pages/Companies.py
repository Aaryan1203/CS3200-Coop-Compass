import streamlit as st
import logging
logger = logging.getLogger(__name__)
import requests
from modules.nav import SideBarLinks
from components.search import search_bar
from components.company import company_component
from modules.filter_functions import filter_companies
from utils.routes import get_all_companies
from utils.routes import get_all_job_listings

try: 
    companies = get_all_companies()
    job_listings = get_all_job_listings()
except:
    st.write("**Important**: Could not connect to API.")

SideBarLinks()

st.write("# Companies")

text_input = search_bar("Companies")

# Check if companies is valid
if isinstance(companies, list):
    
    filtered_companies = filter_companies(companies, text_input)

    for company in filtered_companies:
        # number of job listings per company
        num_job_listings = len([job for job in job_listings if job['Company ID'] == company['Company ID']])
        company_component(company, num_job_listings)

else:
    st.write("No companies available.")
