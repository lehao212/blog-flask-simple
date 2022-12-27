from .services import add_tow_number
from . import app
from flask import render_template, request, redirect, url_for, session

#Dieu huong
@app.route('/')
def main():
    return render_template("index.html")



@app.route('/login',methods=["POST", "GET"] )
def login():
    if request.method=="POST":
        user_name = request.form["email"]
        password = request.form["password"]
        if user_name and password:
           # return redirect(url_for("about", name = user_name))
           session["user"] = user_name
           session["pass"] = password
           #return home()    
           return redirect(url_for("home", name = user_name, password = password))
    return render_template("login.html")

@app.route('/home')
def home():
    if "user" in session:
        return render_template("home.html")
    else:
        return redirect(url_for("login"))

# @app.route('/logout')
# def logout():
#     session.pop["user", None]
#     session.pop["pass", None]
#     return redirect(url_for("login"))

@app.route('/about/<name>')
def about(name):
    return f"<h1>Hello {name}</h1>"

@app.route('/math/<int:num_a>/<int:num_b>')
def math(num_a: int, num_b: int):
    ans = add_tow_number(num_a, num_b)
    params = dict(num_a = num_a, num_b = num_b, ans = ans)
    return render_template('math.html', **params)