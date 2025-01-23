from batchTranslate import translate
from flask import Flask,request,session,render_template
from os import getenv

def formatStr(text):
        return text.replace('\n','<br>')

app=Flask(__name__)
app.config['SECRET_KEY'] = 'hello'



@app.route("/theportaltotheotherworld")
def theportaltotheotherworld():
    return "In the portal to the other world, you can get rick rolled when you find the seacret"

@app.route("/", methods=["GET", "POST"])
def select():
    if request.method == 'POST':
        session["text"] = request.form['text']
        session["times"] = request.form["times"]
        try:
            session["times"]=int(session["times"])
        except:
            return "Please enter a number"
        if session["times"]<=0:
            return "Please enter a number greater than 0"
        session["resualt"]=translate(session["times"],session["text"])
        return render_template("done.html", resault=formatStr(session["resualt"]))
    return render_template("index.html")

                    
@app.route("/done",methods=["GET"])
def done():
    return render_template("done.html",done=session["resualt"])

if __name__ == "__main__":
    app.run(debug=False,port=int(getenv('PORT', 8080)),host="0.0.0.0")