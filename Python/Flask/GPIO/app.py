from flask import Flask, render_template, request
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])

def index():
     global msg
     if request.method == "POST":
         request.form.get("formA")
         GPIO.output(17,GPIO.HIGH)
         GPIO.output(22,GPIO.LOW)
         msg = "Button A Clicked"
     else:
         GPIO.output(17,GPIO.LOW)
         GPIO.output(22,GPIO.LOW)
         msg = "No click yet."
     return render_template("index.html", msg=msg)

if __name__ == "__main__":
     app.run(host="0.0.0.0", port=8080)
