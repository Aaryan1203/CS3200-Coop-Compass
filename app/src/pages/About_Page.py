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

st.title("About Co-op Compass")
st.markdown (
    """
The "Co-op Compass" platform is a unique, data-driven platform for Northeastern students
to gain valuable insights into co-op positions, going beyond what standard job postings offer.

 When applying for co-ops, students often lack transparency around work culture, compensation, and the true nature of job responsibilities.
 Our app fills these gaps by collecting and analyzing reviews on salary information and work experiences from previous co-op students, offering a 
 comprehensive picture that empowers applicants to make more informed decisions.

Our four main user personas—Applicants, Previous Co-ops, Employers, and Admin—each benefit from tailored features. 
Applicants can explore authentic peer reviews, Previous Co-ops can easily share their insights, and Employers can showcase their brand
through verified information as well as oversee trends regarding their company. Moreover, Admins can regulate content and users, to uphold the
functionality and guidelines within the app. With features like salary transparency, job satisfaction scores, and advanced filters, "Co-Op Compass" bridges the information gap,
providing students with a clearer path to co-op opportunities that match their aspirations and values.

Learn more about each user type and their app functionality below:
    """
)

st.header("Students: Empowering Informed Decisions")
st.markdown (
    '''

Students searching for co-op opportunities gain access to robust tools and data to enhance their application and decision-making process:

### Comprehensive Job Search:

Browse and filter job postings based on key attributes such as title, skills required, location, hourly wage, and more.
Advanced search functionality to target roles aligned with individual career aspirations.

### Peer Reviews:

View detailed reviews of job postings, including work culture, job satisfaction, salary information, and more, written by previous co-op students.
Access aggregated data such as average job satisfaction and review counts for each position.

### Favorites Management:

Save and manage a list of favorite job postings for easy reference.
Review and refine applications based on curated lists.

### Learning Resources:

Explore curated resources to help improve professional development, including links and materials shared by peers and administrators.

### Review Creation:

Write reviews for job postings to provide transparency for future applicants.
Share details anonymously to protect personal identity when desired.

### Review Management:

Edit or delete reviews as needed to ensure accuracy or retract contributions.
View and manage all personal reviews in one centralized interface.
'''
)
st.header("Recruiters: Data-Driven Talent Acquisition")
st.markdown(
    '''

Recruiters can leverage insights to enhance job postings and company branding:

### Analytics Dashboard:

Access metrics such as average job satisfaction and the number of reviews specific to their postings.
Use analytics to evaluate the effectiveness of co-op programs and improve job postings.

### Job Listing Management:

Create, edit, and delete job postings to keep opportunities up-to-date and relevant.
Ensure accurate representation of roles to attract top talent.

### Review Moderation:

Flag misleading or inaccurate reviews for administrative review.
Gain insights into feedback trends to refine recruitment strategies.
'''
)

st.header("Co-op Advisors: Enhanced Student Support")
st.markdown(
    '''
Co-op advisors have tools to oversee and guide students effectively:

### Student Analytics:

View aggregated and individual analytics for students under their guidance, including job satisfaction scores and review summaries.

### Job Recommendations:

Send personalized job listings to students based on their interests and past experiences.

### Student Engagement Overview:

Access a complete history of students' reviews and job applications to provide tailored advice.

### Recommendation Management:

Monitor and update sent job recommendations to ensure relevance.
'''
)

st.header("App Admin")
st.markdown(
    '''
Platform admins are critical to maintaining the integrity and professionalism of the community:

### Content Moderation:

Review, edit, or delete inappropriate or inaccurate reviews and job postings.
Oversee flagged reviews and job listings to ensure compliance with platform policies.

### Audit and Restore:

Access and restore previously deleted reviews or postings if necessary based on policy updates.

### Community Oversight:

Monitor overall activity, ensuring a respectful and resourceful environment for all users.
'''
)
