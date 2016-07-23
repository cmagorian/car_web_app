from flask import Flask, render_template, request
import os, sys
from subprocess import call

app = Flask(__name__)

@app.route("/")
def home():
	return render_template('index.html')

@app.route("/navigation", methods=['GET'])
def navigation():
	x = call(["ls", "-l"])
	return x

@app.route("/bluetooth")
def bluetooth():
	x = call(["ls", "-l"])
	return x

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=3000)
