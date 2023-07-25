import os
from flask import Flask, request,render_template
from extract_metadata import extract_content_metadata
from database import insert_and_index
import shutil

app=Flask(__name__)

# Get current path
path = os.getcwd()
# file Upload
UPLOAD_FOLDER = os.path.join(path, 'uploads')

# Make directory if uploads does not exists
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
  
        # Get the list of files from webpage
        files = request.files.getlist("file")
  
        # Iterate for each file in the files List, and Save them
        for file in files:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

        folder='uploads'
        data=extract_content_metadata(folder)

        content=data[0]
        metadata=data[1]

        insert_and_index(content, metadata)

        #deleting upload
        try:
            shutil.rmtree(folder)
        except OSError as e:
            print(f"Error: {e}")

        return "<h1>Files Uploaded Successfully.!</h1>"

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5000,debug=False,threaded=True)
     



