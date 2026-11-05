
from flask import Flask, flash, redirect, render_template, request, session, url_for, send_from_directory

app = Flask(__name__) 

@app.route("/") 
def home(): 
    if "user_id" not in session:
        return redirect(url_for("home"))
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)

