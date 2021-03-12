# Import the libraries
from flask import Flask, render_template, request
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import Robot, LED, CamJamKitRobot, AngularServo

# Define the flask app
app = Flask(__name__)

# Define the pin factories, the robots and the servos
factory = PiGPIOFactory(host='192.168.0.25')
factory2 = PiGPIOFactory(host='192.168.0.10')
linus_eye = LED(16, pin_factory=factory)
linus = Robot(left=(13, 21), right=(17, 27), pin_factory=factory)
torvalds = CamJamKitRobot(pin_factory=factory2)
angular_servo = AngularServo(22, min_angle=-90, max_angle=90, pin_factory=factory)
angular_servo2 = AngularServo(23, min_angle=-90, max_angle=90, pin_factory=factory)

# Main function where the main html file is displayed
@app.route('/')
def index():
    return render_template('dual_robot.html')

# Turns the eye on
@app.route('/eyeon')
def eye_on():
    linus_eye.on()
    return render_template('dual_robot.html')

# Turns the eye off
@app.route('/eyeoff')
def eye_off():
    linus_eye.off()
    return render_template('dual_robot.html')
# These functions move Linus by the given direction
@app.route('/forward')
def north():
    linus.forward()
    return render_template('dual_robot.html')

@app.route('/backward')
def south():
    linus.backward()
    return render_template('dual_robot.html')

@app.route('/left')
def west():
    linus.left()
    return render_template('dual_robot.html')

@app.route('/right')
def east():
    linus.right()
    return render_template('dual_robot.html')

@app.route('/stop')
def stop_movement():
    linus.stop()
    return render_template('dual_robot.html')

# These functions move torvalds based on the given direction
@app.route('/up')
def go_up():
    torvalds.forward()
    return render_template('dual_robot.html')

@app.route('/down')
def go_down():
    torvalds.backward()
    return render_template('dual_robot.html')

@app.route('/west')
def go_left():
    torvalds.left()
    return render_template('dual_robot.html')

@app.route('/east')
def go_right():
    torvalds.right()
    return render_template('dual_robot.html')

@app.route('/stop2')
def stop_robot():
    torvalds.stop()
    return render_template('dual_robot.html')

# This function controls the servo arm of Linus based on the value of the sliders
@app.route('/test', methods=['POST'])
def test():
    slider1 = request.form["slider1"]
    slider2 = request.form["slider2"]
    angular_servo.angle = int(slider1)
    angular_servo2.angle = int(slider2)
    return render_template('dual_robot.html')

# Runs the app at the host IP. Default port is 5000.
if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0')
