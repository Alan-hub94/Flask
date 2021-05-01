from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('list.html')

@app.route("/lenguajes")
def lenguajes():
    return render_template('lenguajes.html')

@app.route("/about")
def about():
    return "<h1> hola </h1>"

if __name__== "__main__":
    app.run(debug=True)


