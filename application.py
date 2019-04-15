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

@app.route('/')
def css():
    return render_template('mangrove_Index.html')


