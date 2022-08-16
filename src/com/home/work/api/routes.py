from flask import request, jsonify
from src.com.home.work import app, client, cross_origin, db
from src.com.home.work.database.model.earthheal.Project import Project


@app.route('/')
def home():
    return 'Welcome to earth heal Config Service'


@app.route('/Healthcheck', methods=['Get'])
def service_available():
    return "service ok"


@app.route('/project', methods=['POST'])
def create():
    """
        create() : Add document to Firestore collection with request body
        Ensure you pass a custom ID as part of json body in post request
        e.g. json={'id': '1', 'title': 'Write a blog post'}
    """
    # uploaded_file = request.files.get('image_file')
    persist_object = Project(request)
    project_image = request.files.get('image_file')

    return persist_object.add_record(project_image)


@app.route('/project/<project_id>', methods=['GET'])
def get_project(project_id):
    """
        read() : Fetches documents from Firestore collection as JSON
        todo : Return document that matches query ID
        all_todos : Return all documents
    """
    return Project().get_record(project_id)


@app.route('/project/<project_id>', methods=['PUT'])
def update(project_id):
    """
        update() : Update document in Firestore collection with request body
        Ensure you pass a custom ID as part of json body in post request
        e.g. json={'id': '1', 'title': 'Write a blog post today'}
    """
    return Project(request.json).update_record()


@app.route('/project/<project_id>', methods=['DELETE'])
def delete(project_id):
    """
        delete() : Delete a document from Firestore collection
    """
    return Project().delete_record(project_id)
