from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

students = Blueprint('students', __name__)

#------------------------------------------------------------
# Get student by ID
#------------------------------------------------------------
@students.route('/student/<student_id>', methods=['GET'])
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


#------------------------------------------------------------
# Resource Section
#------------------------------------------------------------

#------------------------------------------------------------
# Get all resources
#------------------------------------------------------------
@students.route('/resouces', methods=['GET'])
def get_all_resources():
    query = '''
        SELECT name, url, description
        FROM resource
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

#------------------------------------------------------------
# Get all resources created by a specific student
#------------------------------------------------------------
@students.route('/resource/<student_id>', methods=['GET'])
def get_resources_by_student(student_id):
    query = f'''
        SELECT name, url, description
        FROM resource
        WHERE studentId = {str(student_id)}
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# Get all students that are associated with the advisor
@students.route('/students/advisor/<advisor_id>', methods=['GET'])
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