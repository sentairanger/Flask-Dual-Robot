from flask import Flask, render_template, request
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import OutputDevice, AngularServo, LED, PWMOutputDevice

app = Flask(__name__)

#Define the factories
factory = PiGPIOFactory(host='192.168.0.21')
factory2 = PiGPIOFactory(host='192.168.0.18')

# Define both robots
en_1 = PWMOutputDevice(12, pin_factory=factory)
en_2 = PWMOutputDevice(26, pin_factory=factory)
motor_in1 = OutputDevice(13,  pin_factory = factory)
motor_in2 = OutputDevice(21,  pin_factory = factory)
motor_in3 = OutputDevice(17,  pin_factory = factory)
motor_in4 = OutputDevice(27,  pin_factory = factory)

pin1 = OutputDevice(7,  pin_factory = factory2)
pin2 = OutputDevice(8,  pin_factory = factory2)
pin3 = OutputDevice(9,  pin_factory = factory2)
pin4 = OutputDevice(10,  pin_factory = factory2)

#Define the eye
linus_eye = LED(16, pin_factory=factory)

# Define the servo
angular_servo = AngularServo(22, min_angle=-90, max_angle=90, pin_factory=factory)
angular_servo2 = AngularServo(23, min_angle=-90, max_angle=90, pin_factory=factory)

# Define the functions

# Main function where the main html file is displayed
@app.route('/')
def index():
    return render_template('dual_robot_pwm.html')

@app.route('/forward')
def direction_one():
    motor_in1.on()
    motor_in2.off()
    motor_in3.on()
    motor_in4.off()
    return render_template('dual_robot_pwm.html')

# backwards
@app.route('/backward')
def direction_two():
    motor_in1.off()
    motor_in2.on()
    motor_in3.off()
    motor_in4.on()
    return render_template('dual_robot_pwm.html')

#right
@app.route('/right')
def direction_three():
    motor_in1.on()
    motor_in2.off()
    motor_in3.off()
    motor_in4.on()
    return render_template('dual_robot_pwm.html')

#left
@app.route('/left')
def direction_four():
    motor_in1.off()
    motor_in2.on()
    motor_in3.on()
    motor_in4.off()
    return render_template('dual_robot_pwm.html')

@app.route('/stop')
def stop():
    motor_in1.off()
    motor_in2.off()
    motor_in3.off()
    motor_in4.off()
    return render_template('dual_robot_pwm.html')

@app.route('/eyeon')
def eye_on():
    linus_eye.on()
    return render_template('dual_robot_pwm.html')

@app.route('/eyeoff')
def eye_off():
    linus_eye.off()
    return render_template('dual_robot_pwm.html')

# Forwards
@app.route('/up')
def north():
    pin1.on()
    pin2.off()
    pin3.on()
    pin4.off()
    return render_template('dual_robot_pwm.html')

# backwards
@app.route('/down')
def south():
    pin1.off()
    pin2.on()
    pin3.off()
    pin4.on()
    return render_template('dual_robot_pwm.html')

#right
@app.route('/east')
def east():
    pin1.on()
    pin2.off()
    pin3.off()
    pin4.on()
    return render_template('dual_robot_pwm.html')

#left
@app.route('/west')
def west():
    pin1.off()
    pin2.on()
    pin3.on()
    pin4.off()
    return render_template('dual_robot_pwm.html')

@app.route('/stop2')
def stop_two():
    pin1.off()
    pin2.off()
    pin3.off()
    pin4.off()
    return render_template('dual_robot_pwm.html')

@app.route('/test', methods=['POST'])
def test():
    slider1 = request.form["slider1"]
    slider2 = request.form["slider2"]
    angular_servo.angle = int(slider1)
    angular_servo2.angle = int(slider2)
    return render_template('dual_robot_pwm.html')

@app.route('/test2', methods=['POST'])
def test_two():
    slider3 = request.form["slider3"]
    slider4 = request.form["slider4"]
    en_1.value = int(slider3) / 10
    en_2.value = int(slider4) / 10
    return render_template('dual_robot_pwm.html')

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0')


