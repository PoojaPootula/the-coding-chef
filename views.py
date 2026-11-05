from flask import Blueprint, render_template

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

@views.route("/contactus")
def contactus():
    return render_template("contactus.html")

@views.route("/breakfast")
def breakfast():
    return render_template("breakfast.html")

@views.route("/rice")
def rice():
    return render_template("rice.html")

@views.route("/vegrecipes")
def veg():
    return render_template("vegrecipes.html")

@views.route("/nonvegrecipes")
def nonveg():
    return render_template("nonvegrecipes.html")