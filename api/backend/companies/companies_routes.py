from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

companies = Blueprint('companies', __name__)

#------------------------------------------------------------
# Get all companies
#------------------------------------------------------------
@companies.route('/companies', methods=['GET'])
def get_all_companies():
    query = '''
        SELECT name as Name, headline as Headline, description as Description, websiteLink as 'Website Link', companyId as 'Company ID'
        FROM company
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
@companies.route('/companies/job_listings/<company_id>', methods=['GET'])
def get_job_listings_by_company(company_id):
    query = f'''
        SELECT jobTitle as 'Job Title', jobDescription as 'Job Description', jobType as 'Job Type', jobLocation as 'Job Location', jobListingId as 'Job Listing ID', companyId as 'Company ID'
        FROM job_listing
        WHERE companyId = {str(company_id)}
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

#------------------------------------------------------------
# Delete a company
#------------------------------------------------------------
@companies.route('/companies/<company_id>', methods=['DELETE'])
def delete_company(company_id):
    query = f'''
        DELETE FROM company
        WHERE companyId = {str(company_id)}
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    response = make_response(jsonify('Company deleted successfully'))
    response.status_code = 200
    return response

#------------------------------------------------------------
# Update a company
#------------------------------------------------------------
@companies.route('/companies', methods=['PUT'])
def update_company():
    data = request.json
    query = f'''
        UPDATE company
        SET name = '{data['Name']}', headline = '{data['Headline']}', description = '{data['Description']}', websiteLink = '{data['Website Link']}'
        WHERE companyId = {str(data['Company ID'])}
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    response = make_response(jsonify('Company updated successfully'))
    response.status_code = 200
    return response

#------------------------------------------------------------
# Create a company
#------------------------------------------------------------
@companies.route('/companies', methods=['POST'])
def create_company():
    data = request.json
    query = f'''
        INSERT INTO company (name, headline, description, websiteLink)
        VALUES ('{data['Name']}', '{data['Headline']}', '{data['Description']}', '{data['Website Link']}')
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    response = make_response(jsonify('Company created successfully'))
    response.status_code = 201
    return response


