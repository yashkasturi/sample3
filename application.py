import cv2
import imutils
import numpy
import requests
from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from PIL import Image
from skimage.io import imread
from skimage.measure import compare_ssim

app = Flask(__name__)

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

@app.after_request
def add_header(response):
    response.cache_control.max_age = 0
    response.cache_control.public = True
    return response

@app.route('/')
def css():
    return render_template('mangrove_Index.html')


