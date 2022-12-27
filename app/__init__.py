from flask import Flask, render_template

 #dinh nghia
app = Flask(__name__)
app.config["SECRET_KEY"] = "lehao212.tn@gmail.com"
from .route import*

