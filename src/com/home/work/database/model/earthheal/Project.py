import logging

from flask import jsonify
from datetime import date
from src.com.home.work import app, client, bucket


class Project:
    logger = logging.getLogger("Project")

    def __init__(self, request=None):

        if request is None:
            return
        request_data = request.form
        self.id = request_data.get('project_id')
        self.title = request_data.get('title')
        self.organization = request_data.get('organization')
        self.created_by = request_data.get('created_by')
        self.created_on = str(date.today())
        self.file_url = None

    def add_record(self, project_image):

        self.upload_file_to_blob(project_image)
        client.document(self.id).set(self.__dict__)
        return jsonify(self.__dict__), 200

        # db.projects.insert_one({'title': self.title, 'created_by': self.created_by, 'created_on': self.created_on,
        #                         'organization': self.organization})

    def upload_file_to_blob(self,project_image):

        blob = bucket.blob(project_image.filename)
        blob.upload_from_string(
            project_image.read(),
            content_type=project_image.content_type
        )
        self.file_url = blob.public_url

    def get_record(self, project_id):
        try:
            if project_id:
                project = client.document(project_id).get()
                return jsonify(project.to_dict()), 200
            else:
                all_todos = [doc.to_dict() for doc in client.stream()]
                return jsonify(all_todos), 200
        except Exception as e:
            return f"An Error Occured: {e}"

    def update_record(self, project_id):
        try:
            client.document(project_id).update(self.__dict__)
            return jsonify({"success": True}), 200
        except Exception as e:
            return f"An Error Occured: {e}"

    def delete_record(self, project_id):
        try:
            client.document(project_id).delete()
            return jsonify({"success": True}), 200
        except Exception as e:
            return f"An Error Occured: {e}"
