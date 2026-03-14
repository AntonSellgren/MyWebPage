from webserver import app
from flask import abort, render_template, redirect, render_template, request, url_for, flash, session, jsonify, send_file

@app.route('/')
@app.route('/home')
def start():
    return render_template('start.html')
