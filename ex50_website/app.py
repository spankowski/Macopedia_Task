from flask import Flask
from flask import render_template
from flask import request
from werkzeug.utils import secure_filename
from flask import Flask, flash, redirect, url_for
import os
from flask import send_from_directory

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))                              
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

@app.route("/s")
def index_back():
    greeting = "Hello"
    return render_template("index.html", greeting=greeting)

@app.route("/upload")
def upload():
    return render_template("upload.html")


@app.route("/z")
def fo():
    person_1 = ['a','b','c']
    person_2 = ['a','b','c']
    person_3 = ['a','b','c']
    dane = [person_1,person_2,person_3]
    return render_template("list.html", greeting=dane)

@app.route("/hel")
def index_hel():
    name = request.args.get('name', 'Nobody')
    greet = request.args.get('greet', 'Hello')
    greeting = f"{greet}, {name}"

    if name and greet:
        greeting = f"{greet}, {name}"
    else:
        greeting = "Hello World"

    return render_template("index.html", greeting=greeting)    

@app.route("/hello", methods=['POST', 'GET'])
def index():
    greeting = "Hello World"

    if request.method == "POST":
        name = request.form['name']
        greet = request.form['greet']
        greeting = f"{greet}, {name}"
        return render_template("index.html", greeting=greeting)
    else:
        return render_template("hello_form.html")


if __name__ == "__main__":
    app.run()

