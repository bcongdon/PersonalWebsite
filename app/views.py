from app import app
from flask import render_template
from fitbit import step_getter
from wunderlist import wunderlist_downloader
import stats

@app.route('/')
@app.route('/index')
def index():
	return render_template("index.html")

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/projects')
def projects():
	return render_template("projects.html")