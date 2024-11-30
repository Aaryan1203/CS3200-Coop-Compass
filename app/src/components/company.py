import streamlit as st

def company_component(company, num_job_listings):
    with st.expander(f"{company['Name']}"):
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Headline**")
            st.write(company['Headline'])
            st.write("**Description**")
            st.write(company['Description'])
        with col2:
            st.write("**Website Link**")
            st.write(company['Website Link'])
            st.write("**Job Listings**")
            if st.button(f"{num_job_listings} {'Listing' if num_job_listings == 1 else 'Listings'}",
                    key=f"listings_button_{company['Company ID']}",
                    type='secondary'):
                st.session_state['company_id'] = company['Company ID']
                st.session_state['show_deleted'] = False
                st.switch_page('pages/Job_Listings_Page.py')
