from flask import Flask, jsonify
import os
from flask import Flask, render_template, flash, redirect, url_for, make_response,session, request, logging,send_file
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, SelectField, IntegerField,FileField, SubmitField
import daredevil
from passlib.hash import sha256_crypt
from functools import wraps
from flask_wtf import FlaskForm
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired,DataRequired
import deadpool
import Ironman
import bcrypt
import zipping
import matplotlib.pyplot as plt
import os
from Ghost import gimme_string
import shutil
#from dotenv import load_dotenv
from gpt_vetha import answer
import plotly.graph_objs as go
#load_dotenv()
import os
from supabase import create_client

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
