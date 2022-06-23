import os
from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename
import glob
import os

DOWNLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/Songs/'
UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/Uploads/'
ZIP_FOLDER = os.path.dirname(os.path.abspath(__file__))
ALLOWED_EXTENSIONS = {'txt'}

app = Flask(__name__,template_folder='./Template' , static_url_path="/static")
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
app.config['ZIP_FOLDER'] = ZIP_FOLDER
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        song = request.form['name']
        file = request.files['file']
        if request.form['name'].isspace() == False and song != '':
            os.system(f'C:/Users/Administrator/AppData/Local/Programs/Python/Python310/python.exe "f:/My Python Projects/Yt To Mp3/repeater.py" "{song}"')
            list_of_files = glob.glob('./Songs/*.mp3')
            latest_file = max(list_of_files, key=os.path.getctime)
            list_of_files = glob.glob('./Songs/*.mp3')
            latest_file = max(list_of_files, key=os.path.getctime)
            file = latest_file.replace(r"./Songs", '')
            filename = file.replace('\\', '')
            return redirect(url_for('req_file', filename=filename))
        if 'file' and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            os.system(f'C:/Users/Administrator/AppData/Local/Programs/Python/Python310/python.exe "f:/My Python Projects/Yt To Mp3/file_rep.py" "f:\\My Python Projects\\Yt To Mp3\\Uploads\\{filename}"')
            return redirect(url_for('req_zip', filename='songs.zip'))
        if song.isspace() == True or song == '':
            print('Blank')
    return render_template('index.html')

@app.route('/downloads/<filename>')
def req_file(filename):
    return send_from_directory(app.config['DOWNLOAD_FOLDER'], filename, as_attachment=True)

@app.route('/zips/<filename>')
def req_zip(filename):
    return send_from_directory(app.config['ZIP_FOLDER'], filename, as_attachment=True)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 80))
    app.run(host='0.0.0.0', port=port)