from flask import Flask , render_template , request,redirect , url_for
app = Flask(__name__)

@app.route("/")
def ind():
    return render_template("index.html")
@app.route("/ninja/<color>")
def ninjac(color):
    return render_template("ninjac.html", color = color)
@app.route("/ninja")
def ninja():
    return render_template("ninja.html")
app.run(debug= True)
