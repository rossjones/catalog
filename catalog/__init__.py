from flask import Flask, render_template
from flask.ext.pymongo import PyMongo

from catalog.api import APIView

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'ckan'
mongo = PyMongo(app, config_prefix='MONGO')

#app.config.from_object('config')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.route('/')
def homepage():
    return render_template("index.html")

APIView.register(app, route_base='/api')
