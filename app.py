from batchTranslate import translate
from flask import Flask,request,session,render_template,redirect
from os import getenv

app=Flask(__name__)
app.config['SECRET_KEY'] = 'hello'

@app.route("/debug")
def debug():
    return "Suscsessfull"

@app.route("/", methods=["GET", "POST"])
def select():
    if request.method == 'POST':
        session["text"] = request.form['text'].upper()
        session["times"] = request.form["times"].upper()
        return redirect("/get")
    return render_template("index.html")

@app.route("/get",methods=["GET"])
def get():
    resualt=translate(int(session["times"]),session["text"])
    return resualt

if __name__ == "__main__":
    app.run(debug=False,port=int(getenv('PORT', 8080)),host="0.0.0.0")