# Flask-Dual-Robot

## Introduction

As much as I enjoy web development it becomes more fun when using it to control devices such as LEDs, servo motors and robots. Here I decided to build a web application to control my robots Linus and Torvalds. I will show the process I followed to build the web application and how I got it to run.

## Getting Started

Here are the following things I used to build the web application.

### Hardware
* My robots Linus and Torvalds
* Raspberry Pi 4 For testing both robots
* Optional: A smartphone to run the app remotely

### Software

* Flask module: installed using `pip3 install flask`
* Raspbian Stretch on Torvalds
* Raspberry Pi OS Lite on Linus
* Raspberry Pi OS on the Pi 4
* Python modules `gpiozero` and `pigpio` 

## Code Explanation

* `dual_robot.py`: This controls both Linus, Torvalds and also controls the servo arm on Linus. 
* `dual_robot.html`: This builds the app for the robots using HTML and embeds the CSS and JavaScript files. 
* `dual_robot.css`: This is used to design the app.
* `dual_robot.js`: This is used to define the buttons using JavaScript. It uses the 'mouseup' and 'mousedown' arguements to define an action when the mouse is clicked and unclicked. I also add a section in the slider where you can see the value of the slider in degrees.
* `dual_pwm_robot.py`: This code is similar to `dual_robot.py` only this time it is altered to allow the code to run on multiple platforms outside of a Raspberry Pi. PWM is introduced for Linus but can be used with another robot as long as PWM is supported with the motor controller.
* `dual_robot_pwm.js`: Similar to `dual_robot.js` but this time it includes the functionality for the PWM sliders.
* `dual_robot_pwm.html`: Similar to `dual_robot.html` but this time includes the PWM sliders.
* `camera_app.py`: This app controls the Pi Camera remotely. To run this ssh into the robot and then run the app using a different port number like 5001 and run it in a different window. But you also can run it on a new tab if you want.
* `camera_app.html`: This builds the app and embeds the CSS and JavaScript files.
* `camera_app.css`: This designs the app.
* `camera_app.js`: This defines the two buttons using JavaScript. This avoids reloading the webpage. 

## To run on different platforms

The dualrobotpwm app folder should be used to run the code outside of the Raspberry Pi 4. To run this on Linux, Mac and Windows, here are the following steps to take for each OS:

### Linux
Python is already installed so instead make sure to install `pigpio`, `gpiozero` and `flask` using the `pip3 install` command. If you are using a virtual environment like virtualenv just use `pip install`. Then make sure to ssh into each robot and enable `pigpio` with `sudo pigpiod`.

## Windows

To install python you can follow [this](https://www.howtogeek.com/197947/how-to-install-python-on-windows/) and then install `pigpio`, `gpiozero` and `flask` with `pip3 install`.

### Mac

To install python, use the `brew install python` command and then you can install `pigpio`, `gpiozero` and `flask` with `pip install`.

### Android and iOS

Here just point to the link for the app by typing the IP address of where the app is running and then the port. Like this `http://{ip_address_of_flask_app}:5000`.
If you want to run the code natively on Android use the Pydroid3 app in combination with an SSH client app like JuiceSSH. It should work as well.

For iOS you can use Pythonista but there is an issue because there will be an error. So changing the end code to this should help. This was found on ![this](https://forum.omz-software.com/topic/5758/pythonista-flask-error-errno-1) forum post. 

```
if __name__ == '__main__':
    app.run(use_reloader=False, debug=True)
```

## Pictures
* `dual_robot.png`
![dual_robot](https://github.com/sentairanger/Flask-Dual-Robot/blob/main/dual_robot.png)

* `Figure4.png`
![dual_robot](https://github.com/sentairanger/Flask-Dual-Robot/blob/main/Figure4.png)

* `dual_pwm_robot.py running on Ubuntu`:
![dual_pwm_robot](https://github.com/sentairanger/Flask-Dual-Robot/blob/main/Screenshot%20from%202021-04-20%2018-52-29.png)

* `dual_pwm_robot.py running on Windows`:
![Windows_pwm_robot](https://github.com/sentairanger/Flask-Dual-Robot/blob/main/2021-04-21.png)

* `dual_pwm_robot.py running on Android`:
![Android_pwm_robot](https://github.com/sentairanger/Flask-Dual-Robot/blob/main/Screenshot_2021-04-20-19-43-18-611%7E2.jpeg)
