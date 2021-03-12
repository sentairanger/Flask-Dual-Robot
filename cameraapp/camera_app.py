# Import the libraries
from picamera import PiCamera
from gpiozero import LED
from flask import Flask, render_template, request
from datetime import datetime

# Define the camera and the Eye
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 25
devastator_eye = LED(25)

# Define the flask app
app = Flask(__name__)

# Main function that displays the main html file
@app.route('/')
def index():
    return render_template('camera.html')

# Turns on the eye and starts recording 
@app.route('/record')
def record_camera():
    devastator_eye.on()
    camera.start_recording("/home/pi/Videos/video_%02d_%02d_%02d.mjpg" % (moment.hour, moment.minute, moment.second))
    return render_template('camera.html')

# Turns off the eye and stops recording
@app.route('/stop')
def stop_record():
    devastator_eye.off()
    camera.stop_recording()
    return render_template('camera.html')

# Runs the app. Port 5001 was used here to avoid conflict with the other code
if __name__ == "__main__":
	app.run(host='', port=5001)
