from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

reviews = Blueprint('reviews', __name__)

#------------------------------------------------------------
# Get all the reviews
#------------------------------------------------------------
@reviews.route('/reviews', methods=['GET'])
def get_all_reviews():
    query = '''
        SELECT R.jobListingId as 'Job Listing ID', R.anonymous as Anonymous, R.description as Descriotion, R.jobSatisfaction as 'Job Satisfaction', R.hourlyWage as 'Hourly Wage', R.deleted as Deleted, J.jobTitle as 'Job Title', C.name as Company, J.recruiterId as 'Recruiter ID'
        FROM review R
        JOIN jobListing J ON R.jobListingId = J.jobListingId
        JOIN company C ON J.companyId = C.companyId
        LEFT JOIN flaggedReview FR ON R.reviewId = FR.reviewId
        WHERE R.deleted = false AND FR.reviewId IS NULL
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

#------------------------------------------------------------
# Get all reviews for a job listing
#------------------------------------------------------------
@reviews.route('/reviews/<job_listing_id>', methods=['GET'])
def get_reviews_by_job_listing(job_listing_id):
    query = f'''
        SELECT R.reviewId as 'Review ID', R.jobListingId as 'Job Listing ID', anonymous as Anonymous, R.description as Description, jobSatisfaction as 'Job Satisfaction', R.hourlyWage as 'Hourly Wage', S.name as 'Student Name', J.jobTitle as 'Job Title', C.name as Company, R.deleted as Deleted, J.recruiterId as 'Recruiter ID'
        FROM review R
        JOIN student S ON R.studentId = S.studentId
        JOIN jobListing J ON R.jobListingId = J.jobListingId
        JOIN company C ON J.companyId = C.companyId
        LEFT JOIN flaggedReview FR ON R.reviewId = FR.reviewId
        WHERE R.jobListingId = '{str(job_listing_id)}' AND R.deleted = false AND FR.reviewId IS NULL
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response


#------------------------------------------------------------
# Get all reviews by a student
#------------------------------------------------------------
@reviews.route('/reviews/student/<student_id>', methods=['GET'])
def get_reviews_by_student(student_id):
    query = f'''
        SELECT R.reviewId as 'Review ID', R.jobListingId as 'Job Listing ID', anonymous as Anonymous, R.description as Description, jobSatisfaction as 'Job Satisfaction', R.hourlyWage as 'Hourly Wage', S.name as 'Student Name', J.jobTitle as 'Job Title', C.name as Company, R.deleted as Deleted, J.recruiterId as 'Recruiter ID'
        FROM review R
        JOIN student S ON R.studentId = S.studentId
        JOIN jobListing J ON R.jobListingId = J.jobListingId
        JOIN company C ON J.companyId = C.companyId
        LEFT JOIN flaggedReview FR ON R.reviewId = FR.reviewId
        WHERE R.studentId = '{str(student_id)}' AND R.deleted = false AND FR.reviewId IS NULL
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

#------------------------------------------------------------
# Get all deleted reviews
#------------------------------------------------------------
@reviews.route('/reviews/deleted', methods=['GET'])
def get_deleted_reviews():
    query = '''
        SELECT R.reviewId as 'Review ID', R.jobListingId as 'Job Listing ID', anonymous as Anonymous, R.description as Description, jobSatisfaction as 'Job Satisfaction', R.hourlyWage as 'Hourly Wage', S.name as 'Student Name', J.jobTitle as 'Job Title', C.name as Company, R.deleted as Deleted, J.recruiterId as 'Recruiter ID'
        FROM review R
        JOIN student S ON R.studentId = S.studentId
        JOIN jobListing J ON R.jobListingId = J.jobListingId
        JOIN company C ON J.companyId = C.companyId
        WHERE R.deleted = true
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

#------------------------------------------------------------
# Get all flagged reviews
#------------------------------------------------------------
@reviews.route('/reviews/flagged', methods=['GET'])
def get_flagged_reviews():
    query = '''
        SELECT FR.reviewId as 'Review ID', FR.flaggedById as 'Flagged By ID', FR.reason as Reason, R.jobListingId as 'Job Listing ID', R.anonymous as Anonymous, R.description as Description, R.jobSatisfaction as 'Job Satisfaction', R.hourlyWage as 'Hourly Wage', S.name as 'Student Name', J.jobTitle as 'Job Title', C.name as Company, R.deleted as Deleted, J.recruiterId as 'Recruiter ID'
        FROM flaggedReview FR
        JOIN review R ON FR.reviewId = R.reviewId
        JOIN student S ON R.studentId = S.studentId
        JOIN jobListing J ON R.jobListingId = J.jobListingId
        JOIN company C ON J.companyId = C.companyId
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

#------------------------------------------------------------
# Add a review
#------------------------------------------------------------
@reviews.route('/review', methods=['POST'])
def add_review():
    data = request.json
    description = data['description']
    jobSatisfaction = data['jobSatisfaction']
    hourlyWage = data['hourlyWage']
    anonymous = data['anonymous']
    jobListingId = data['jobListingId']
    studentId = data['studentId']
    
    query = f'''
        INSERT INTO review (description, jobSatisfaction, hourlyWage, anonymous, jobListingId, studentId)
        VALUES ('{description}', {jobSatisfaction}, '{hourlyWage}', {anonymous}, '{jobListingId}', '{studentId}')
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    response = make_response(jsonify({"message": "Review added."}))
    response.status_code = 200
    return response

#------------------------------------------------------------
# Toggle flagging a review
#------------------------------------------------------------
@reviews.route('/review/flag', methods=['POST'])
def flag_review():
    data = request.json
    reviewId = data['reviewId']
    flaggedById = data['flaggedById']
    reason = data['reason']
    
    query = f'''
        INSERT INTO flaggedReview (reviewId, flaggedById, reason)
        VALUES ('{reviewId}', '{flaggedById}', '{reason}')
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    response = make_response(jsonify({"message": "Review flagged."}))
    response.status_code = 200
    return response

#------------------------------------------------------------
# Unflag a review
#------------------------------------------------------------
@reviews.route('/review/unflag/<reviewId>', methods=['PUT'])
def unflag_review(reviewId):
    query = f'''
        DELETE FROM flaggedReview
        WHERE reviewId = '{reviewId}'
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    response = make_response(jsonify({"message": "Review unflagged."}))
    response.status_code = 200
    return response

#------------------------------------------------------------
# Update a review
#------------------------------------------------------------
@reviews.route('/review', methods=['PUT'])
def update_review():
    data = request.json
    reviewId = data['reviewId']
    description = data['description']
    jobSatisfaction = data['jobSatisfaction']
    hourlyWage = data['hourlyWage']
    
    query = f'''
        UPDATE review
        SET description = '{description}', jobSatisfaction = {jobSatisfaction}, hourlyWage = '{hourlyWage}'
        WHERE reviewId = '{reviewId}'
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    response = make_response(jsonify({"message": "Review updated."}))
    response.status_code = 200
    return response

#------------------------------------------------------------
# Toggle delete a review
#------------------------------------------------------------
@reviews.route('/review/<review_id>', methods=['PUT'])
def toggle_delete_review(review_id):
    query = f'''
        UPDATE review
        SET deleted = NOT deleted
        WHERE reviewId = '{review_id}'
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    response = make_response(jsonify({"message": "Review updated."}))
    response.status_code = 200
    return response