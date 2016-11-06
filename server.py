from flask import *

app = Flask(__name__)

@app.route("/")
def root():
    return "Initial commit"

if __name__ == '__main__':
    app.run(debug=True)

