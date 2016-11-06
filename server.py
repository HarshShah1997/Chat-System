from flask import *

app = Flask(__name__)
messages = []

@app.route("/")
def root():
    return render_template("home.html", messages=messages)

@app.route("/receiveMessage", methods=["POST"])
def receiveMessage():
    message = request.form['chatText']
    messages.append(message)
    return redirect(url_for('root'))

if __name__ == '__main__':
    app.run(debug=True)

