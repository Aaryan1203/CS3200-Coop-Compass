from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

management = Blueprint('management', __name__)

#------------------------------------------------------------
# Get student by ID
#------------------------------------------------------------
@management.route('/student/<student_id>', methods=['GET'])
def get_user_by_id(student_id):
    query = f'''
        SELECT name, email, phoneNumber
        FROM student
        WHERE studentId = {str(student_id)}
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# Get all students that are associated with the advisor
@management.route('/students/advisor/<advisor_id>', methods=['GET'])
def get_students_for_advisor(advisor_id):
    
    # SQL query
    query = f"""
        SELECT s.studentId as 'StudentID', s.name as 'StudentName', s.email as 'StudentEmail', s.phoneNumber as 'StudentPhoneNumber'
        FROM student s
        INNER JOIN advisor ON s.advisorId = advisor.advisorId
        WHERE advisor.advisorId = {str(advisor_id)};
    """
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

#------------------------------------------------------------
# Get all flagged reviews
#------------------------------------------------------------
@management.route('/reviews/flagged', methods=['GET'])
def get_flagged_reviews():
    query = '''
        SELECT FR.reviewId as 'Review ID', FR.flaggedById as 'Flagged By ID', FR.reason as Reason, R.jobListingId as 'Job Listing ID', R.anonymous as Anonymous, R.description as Description, R.jobSatisfaction as 'Job Satisfaction', R.hourlyWage as 'Hourly Wage', S.name as 'Student Name', J.jobTitle as 'Job Title', C.name as Company, R.deleted as Deleted, J.recruiterId as 'Recruiter ID', S.email as 'Student Email', S.phoneNumber as 'Student Phone Number', RC.name as 'Recruiter Name'
        FROM flaggedReview FR
        JOIN review R ON FR.reviewId = R.reviewId
        JOIN student S ON R.studentId = S.studentId
        JOIN jobListing J ON R.jobListingId = J.jobListingId
        JOIN company C ON J.companyId = C.companyId
        JOIN recruiter RC ON J.recruiterId = RC.recruiterId
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

#------------------------------------------------------------
# Toggle favorite job listing
#------------------------------------------------------------
@management.route('/job_listing/favorite', methods=['POST'])
def toggle_favorite_job_listing():
    data = request.json
    job_listing_id = data['jobListingId']
    student_id = data['studentId']
    
    query = f'''
        SELECT *
        FROM favoriteJobListings
        WHERE jobListingId = '{str(job_listing_id)}' AND studentId = '{str(student_id)}'
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchone()
    
    if theData:
        query = f'''
            DELETE FROM favoriteJobListings
            WHERE jobListingId = '{str(job_listing_id)}' AND studentId = '{str(student_id)}'
        '''
    else:
        query = f'''
            INSERT INTO favoriteJobListings (jobListingId, studentId)
            VALUES ('{str(job_listing_id)}', '{str(student_id)}')
        '''
    
    cursor.execute(query)
    db.get_db().commit()
    response = make_response(jsonify({"message": "Favorite job listing updated"}))
    response.status_code = 200
    return response

#------------------------------------------------------------
# Toggle sent job listing
#------------------------------------------------------------
@management.route('/job_listing/sent', methods=['POST'])
def toggle_sent_job_listing():
    data = request.json
    job_listing_id = data['jobListingId']
    student_id = data['studentId']
    advisor_id = data['advisorId']
    
    query = f'''
        SELECT *
        FROM sentJobListings
        WHERE jobListingId = '{str(job_listing_id)}' AND studentId = '{str(student_id)}' AND advisorId = '{str(advisor_id)}'
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchone()
    
    if theData:
        query = f'''
            DELETE FROM sentJobListings
            WHERE jobListingId = '{str(job_listing_id)}' AND studentId = '{str(student_id)}' AND advisorId = '{str(advisor_id)}'
        '''
    else:
        query = f'''
            INSERT INTO sentJobListings (jobListingId, studentId, advisorId)
            VALUES ('{str(job_listing_id)}', '{str(student_id)}', '{str(advisor_id)}')
        '''
    
    cursor.execute(query)
    db.get_db().commit()
    response = make_response(jsonify({"message": "Sent job listing updated"}))
    response.status_code = 200
    return response

#------------------------------------------------------------
# Toggle flagging a review
#------------------------------------------------------------
@management.route('/review/flag', methods=['POST'])
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
@management.route('/review/unflag/<reviewId>', methods=['PUT'])
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

