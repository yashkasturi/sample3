from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def css():
    return render_template('mangrove_Index.html')


