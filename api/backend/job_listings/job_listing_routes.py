from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

job_listings = Blueprint('job_listings', __name__)

#------------------------------------------------------------
# Get all the job_listings
#------------------------------------------------------------
@job_listings.route('/job_listings', methods=['GET'])
def get_all_job_listings():
    query = '''
        SELECT J.jobListingId as 'Job Listing ID', J.jobTitle as 'Job Title', J.description as Description, J.startDate as 'Start Date', J.endDate as 'End Date', J.hourlyWage as 'Hourly Wage', J.skills as 'Skills', J.location as 'Location', C.name as Company, C.companyId as 'Company ID'
        FROM jobListing J
        JOIN company C ON J.companyId = C.companyId
        WHERE deleted = false
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

#------------------------------------------------------------
# Get all deleted job listings
#------------------------------------------------------------
@job_listings.route('/job_listings/deleted', methods=['GET'])
def get_deleted_job_listings():
    query = '''
        SELECT J.jobListingId as 'Job Listing ID', J.jobTitle as 'Job Title', J.description as Description, J.startDate as 'Start Date', J.endDate as 'End Date', J.hourlyWage as 'Hourly Wage', J.skills as 'Skills', J.location as 'Location', C.name as Company, C.companyId as 'Company ID'
        FROM jobListing J
        JOIN company C ON J.companyId = C.companyId
        WHERE deleted = true
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

#------------------------------------------------------------
# Get a single job listing
#------------------------------------------------------------
@job_listings.route('/job_listing/<job_listing_id>', methods=['GET'])
def get_job_listing_by_company(job_listing_id):
    query = f'''
        SELECT J.jobListingId as 'Job Listing ID', J.jobTitle as 'Job Title', J.description as Description, J.startDate as 'Start Date', J.endDate as 'End Date', J.hourlyWage as 'Hourly Wage', J.skills as 'Skills', J.location as 'Location', C.name as Company, C.companyId as 'Company ID'
        FROM jobListing J
        JOIN company C ON J.companyId = C.companyId
        WHERE J.jobListingId = '{str(job_listing_id)}' AND deleted = false
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchone()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

#------------------------------------------------------------
# Get all job listings for a recruiter
#------------------------------------------------------------
@job_listings.route('/job_listings/recruiter/<recruiter_id>', methods=['GET'])
def get_job_listings_by_recruiter(recruiter_id):
    query = f'''
        SELECT J.jobListingId as 'Job Listing ID', J.jobTitle as 'Job Title', J.description as Description, J.startDate as 'Start Date', J.endDate as 'End Date', J.hourlyWage as 'Hourly Wage', J.skills as 'Skills', J.location as 'Location', C.name as Company, C.companyId as 'Company ID'
        FROM jobListing J
        JOIN company C ON J.companyId = C.companyId
        WHERE J.recruiterId = '{str(recruiter_id)}' AND deleted = false
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response


#------------------------------------------------------------
# Get all job listings for a company
#------------------------------------------------------------
@job_listings.route('/job_listings/company/<company_id>', methods=['GET'])
def get_job_listings_by_company(company_id):
    query = f'''
        SELECT J.jobListingId as 'Job Listing ID', J.jobTitle as 'Job Title', J.description as Description, J.startDate as 'Start Date', J.endDate as 'End Date', J.hourlyWage as 'Hourly Wage', J.skills as 'Skills', J.location as 'Location', C.name as Company, C.companyId as 'Company ID'
        FROM jobListing J
        JOIN company C ON J.companyId = C.companyId
        WHERE J.companyId = '{str(company_id)}' AND deleted = false
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

#------------------------------------------------------------
# Create a job listing
#------------------------------------------------------------
@job_listings.route('/job_listing', methods=['POST'])
def create_job_listing():
    data = request.json
    job_title = data['jobTitle']
    description = data['description']
    startDate = data['startDate']
    endDate = data['endDate']
    wage = data['wage']
    skills = data['skills']
    location = data['location']
    company_id = data['companyId']
    recruiter_id = data['recruiterId']
    
    query = f'''
        INSERT INTO jobListing (jobTitle, description, startDate, endDate, hourlyWage, skills, location, companyId, recruiterId)
        VALUES ('{job_title}', '{description}', '{startDate}', '{endDate}', '{wage}', '{skills}', '{location}', '{company_id}', '{recruiter_id}')
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    response = make_response(jsonify({"message": "Job Listing created"}))
    response.status_code = 201
    return response

#------------------------------------------------------------
# Update a job listing
#------------------------------------------------------------
@job_listings.route('/job_listing', methods=['PUT'])
def update_job_listing():
    data = request.json
    job_listing_id = data['jobListingId']
    job_title = data['jobTitle']
    description = data['description']
    startDate = data['startDate']
    endDate = data['endDate']
    hourlyWage = data['hourlyWage']
    skills = data['skills']
    location = data['location']
    
    query = f'''
        UPDATE jobListing
        SET jobTitle = '{job_title}', description = '{description}', hourlyWage = '{hourlyWage}', startDate = '{startDate}', endDate = '{endDate}', skills = '{skills}', location = '{location}'
        WHERE jobListingId = '{str(job_listing_id)}'
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    response = make_response(jsonify({"message": "Job Listing updated"}))
    response.status_code = 200
    return response

#------------------------------------------------------------
# toggle delete a job listing
#------------------------------------------------------------
@job_listings.route('/job_listing/<job_listing_id>', methods=['PUT'])
def toggle_delete_job_listing(job_listing_id):
    query = f'''
        SELECT deleted
        FROM jobListing
        WHERE jobListingId = '{str(job_listing_id)}'
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchone()
    
    if theData['deleted']:
        query = f'''
            UPDATE jobListing
            SET deleted = false
            WHERE jobListingId = '{str(job_listing_id)}'
        '''
    else:
        query = f'''
            UPDATE jobListing
            SET deleted = true
            WHERE jobListingId = '{str(job_listing_id)}'
        '''
    
    cursor.execute(query)
    db.get_db().commit()
    response = make_response(jsonify({"message": "Job Listing deleted"}))
    response.status_code = 200
    return response

#------------------------------------------------------------
# Get all favorite job listings
#------------------------------------------------------------
@job_listings.route('/job_listings/favorite/<student_id>', methods=['GET'])
def get_favorite_job_listings(student_id):
    query = f'''
        SELECT jobListingId as 'Job Listing ID', studentId as 'Student ID'
        FROM favoriteJobListings
        WHERE studentId = '{str(student_id)}'
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

#------------------------------------------------------------
# Get all sent job listings for students
#------------------------------------------------------------
@job_listings.route('/job_listings/received/<student_id>', methods=['GET'])
def get_sent_job_listings_for_students(student_id):
    query = f'''
        SELECT JL.jobListingId as 'Job Listing ID', JL.jobTitle as 'Job Title', JL.description as Description, JL.startDate as 'Start Date', JL.endDate as 'End Date', JL.hourlyWage as 'Hourly Wage', JL.skills as Skills, JL.location as Location, C.name as Company, C.companyId as 'Company ID'
        FROM sentJobListings SJL
        JOIN jobListing JL ON SJL.jobListingId = JL.jobListingId
        JOIN company C ON JL.companyId = C.companyId
        WHERE studentId = '{str(student_id)}'
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response


#------------------------------------------------------------
# Get all sent job listings for advisors
#------------------------------------------------------------
@job_listings.route('/job_listings/sent/<advisor_id>', methods=['GET'])
def get_sent_job_listings_for_advisors(advisor_id):
    query = f'''
        SELECT JL.jobListingId as 'Job Listing ID', JL.jobTitle as 'Job Title', JL.description as Description, JL.startDate as 'Start Date', JL.endDate as 'End Date', JL.hourlyWage as 'Hourly Wage', JL.skills as Skills, JL.location as Location, C.name as Company, C.companyId as 'Company ID', S.studentId as 'Student ID'
        FROM sentJobListings SJL
        JOIN jobListing JL ON SJL.jobListingId = JL.jobListingId
        JOIN company C ON JL.companyId = C.companyId
        JOIN student S ON SJL.studentId = S.studentId
        WHERE SJL.advisorId = '{str(advisor_id)}'
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response
