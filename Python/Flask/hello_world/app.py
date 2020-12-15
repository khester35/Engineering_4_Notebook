from flask import Flask

app = Flask(__name__) # makes new Flask app called "app"

@app.route("/") # tells app that any requests to the root directory (hello_world) should fire off hello_world() function
def hello_world():
	return "hello world!"

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80) # host= tells the app to be visible to outside computers

