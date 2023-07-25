import os
from tika import parser as p

def extract_content_metadata(folder_path):

    file_list = []
    metadata=[]
    content=[]

    #getting list of file paths in /upload
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_list.append(file_path)

    #extractiong metadata
    for i in file_list:
        parsed = p.from_file(i)
        content.append(parsed['content'])
        metadata.append(parsed['metadata'])

    return content ,metadata
