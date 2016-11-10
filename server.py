from flask import *

app = Flask(__name__)
messages = []

@app.route("/")
def root():
    return render_template("home.html", messages=messages)

@app.route("/_receiveMessage", methods=["POST"])
def receiveMessage():
    message = request.form['chatText']
    if message.strip() != '':
        messages.append(message)
    return ('', 204)

@app.route("/_sendMessages")
def sendMessagesList():
    rendered = getHtml()
    return rendered

def getHtml():
    text = '''{% for msg in messages %}
                {{ msg }}<br>
              {% endfor %}'''
    return render_template_string(text, messages=messages)


if __name__ == '__main__':
    app.run(debug=True)

