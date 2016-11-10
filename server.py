from flask import *

app = Flask(__name__)
messages = []

@app.route("/")
def root():
    return render_template("home.html", messages=messages)

@app.route("/_receiveMessage", methods=["POST"])
def receiveMessage():
    message = request.form['chatText']
    name = request.form['username']
    if message.strip() != '':
        messages.append((name, message))
    return ('', 204)

@app.route("/_sendMessages")
def sendMessagesList():
    rendered = getHtml()
    return rendered

def getHtml():
    text = '''{% for name, msg in messages %}
                {{ name }}: {{ msg }}<br>
              {% endfor %}'''
    return render_template_string(text, messages=messages)


if __name__ == '__main__':
    app.run(debug=True)

