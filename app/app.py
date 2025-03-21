from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
	return "Hello SECURE World!"

@app.route('/meow')
def cat():
	return "Safe kitty cat!"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)
