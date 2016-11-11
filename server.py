from flask import *
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'static/uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
messages = []

@app.route("/")
def root():
    return render_template("home.html", messages=messages)

@app.route("/_receiveMessage", methods=["POST"])
def receiveMessage():
    message = request.form['chatText']
    name = request.form['username']
    if message.strip() != '':
        messages.append((name, message, ''))
    return ('', 204)

@app.route("/_sendMessages")
def sendMessagesList():
    rendered = getHtml()
    return rendered

@app.route("/_uploadFile", methods=["POST"])
def uploadFile():
    recvFile = request.files['file']
    if recvFile.filename == '':
        return 'No file selected'

    allowed_extensions = set(['txt', 'pdf', 'doc', 'docx', 'ppt', 'pptx'])

    if recvFile and allowed_file(recvFile.filename, allowed_extensions):
        filename = secure_filename(recvFile.filename)
        recvFile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        messages.append(('Anonymous', '', filename))
        return 'Uploaded successfully'
    return 'Invalid file'

@app.route('/uploads/<filename>')
def fileLink(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

def createLink(filename):
    link = url_for('fileLink', filename=filename) 
    return link

def getHtml():
    text = '''{% for name, msg, link in messages %}
                {{ name }}: {{ msg }} <a href="{{ url_for('fileLink', filename=link) }}">{{ link }}</a><br>
              {% endfor %}'''
    return render_template_string(text, messages=messages)

def allowed_file(filename, allowed_extensions):
    return '.' in filename and filename.rsplit('.', 1)[1] in allowed_extensions

if __name__ == '__main__':
    app.run(debug=True)

