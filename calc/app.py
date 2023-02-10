# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div
app = Flask(__name__)

OPERATIONS = {
	"add": add,
	"sub": sub,
	"mult": mult,
	"div": div
}

@app.route('/add')
def add_vars():
	a = int(request.args["a"])
	b = int(request.args["b"])
	return str(add(a,b))

@app.route('/sub')
def sub_vars():
	a = int(request.args["a"])
	b = int(request.args["b"])
	return str(sub(a,b))

@app.route('/mult')
def mult_vars():
	a = int(request.args["a"])
	b = int(request.args["b"])
	return str(mult(a,b))

@app.route('/div')
def div_vars():
	a = int(request.args["a"])
	b = int(request.args["b"])
	return str(div(a,b))

@app.route('/math/<operation>')
def all_math(operation):
	
	function = OPERATIONS[operation]
	a = int(request.args["a"])
	b = int(request.args["b"])
	return str(function(a,b))
