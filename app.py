import os
from flask import Flask, request,render_template, redirect
from extract_metadata import extract_content_metadata
from database import insert_and_index
import shutil

app=Flask(__name__)

# Get current path
path = os.getcwd()

# file Upload
UPLOAD = os.path.join(path, 'uploads')
UPLOAD_FOLDER = os.path.join(path, 'files')

# Make directory if files folder do not exists
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

app.config['UPLOAD'] = UPLOAD
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def upload_form():
    #creating uploads folder
    if not os.path.isdir(UPLOAD):
        os.mkdir(UPLOAD)
    return render_template('upload.html')


@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
  
        # Get the list of files from webpage
        files = request.files.getlist("file")
  
        # Iterate for each file in the files List, and Save them
        for file in files:
            file.save(os.path.join(app.config['UPLOAD'], file.filename))
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

        #extracting metadata
        folder='uploads'
        data=extract_content_metadata(folder)

        content=data[0]
        metadata=data[1]

        #inserting into MongoDB and indexing
        insert_and_index(content, metadata)

        #deleting uploads
        try:
            shutil.rmtree(folder)
        except OSError as e:
            print(f"Error: {e}")

        return redirect('/')

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5000,debug=False,threaded=True)
     



