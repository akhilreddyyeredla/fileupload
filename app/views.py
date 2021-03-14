from app import app
from files_managment import upload,getfile,deletefile
from flask import request
@app.route("/")
def index():
    return "Hello world"

@app.route("/upload-file",methods=['POST'])
def upload_fun():
    data = request.get_json(force=True)
    file_path = data['file_path']
    file_name = data['file_name']
    upload_obj = upload.upload_class()
    response = upload_obj.upload_file(file_path,file_name)
    return response

@app.route("/get-file-data",methods=['GET'])
def get_fileinfo():
    search_string = request.args.get('file_name')
    getfile_obj = getfile.FileManagment()
    response = getfile_obj.getfilename(search_string)
    return response

@app.route("/delete-file",methods=['GET'])
def file_delete():
    file_id = request.args.get('file_id')
    deletefile_obj = deletefile.Filedestory()
    response = deletefile_obj.delete_file(file_id)
    return response

