from flask import Flask, url_for, redirect

app = Flask(__name__)

@app.route("/")
def first():
	return redirect(url_for('test', name = 'swathi'))

@app.route("/<name>")
def test(name):
	return ("Hello " + name + "! Welcome to Flask.")

if __name__ == "__main__":
	app.run()