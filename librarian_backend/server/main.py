import shutil
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
import os
import engine

app = Flask(__name__)
cors = CORS(app, origins=["*"])
app.config['CORS_HEADERS'] = 'Content-Type'


UPLOAD_FOLDER = '/Users/sfkunal/Code/librarian/librarian_backend/library'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def ensure_upload_folder():
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

@app.route('/clear', methods=['POST'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def clear():
    if os.path.exists(UPLOAD_FOLDER):
        print('cleared')
        shutil.rmtree(UPLOAD_FOLDER)
        ensure_upload_folder()

    return jsonify({'success': True})

@app.route('/upload', methods=['POST'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def upload_file():
    # engine.clear_library()
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    ensure_upload_folder()  # Ensure that the upload folder exists

    if file:
        filename = file.filename.split('/')[-1]
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print(filename)
        return jsonify({'success': True, 'filename': filename})
    
@app.route('/sendquery', methods=['POST'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def send_query():
    text = request.json.get('text', '')
    response = engine.execute_query(UPLOAD_FOLDER, text)
    print(response)
    return jsonify({'success': True, 'text': text, 'response': response})

if __name__ == '__main__':
    app.run(debug=True)
