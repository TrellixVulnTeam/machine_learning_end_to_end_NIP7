from flask import Flask, app

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    return "Machine Learning End to End project"

if __name__ == "__main__":
    app.run(debug=True)