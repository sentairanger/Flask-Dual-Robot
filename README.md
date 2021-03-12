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
* `camera_app.py`: This app controls the Pi Camera remotely. To run this ssh into the robot and then run the app using a different port number like 5001 and run it in a different window. But you also can run it on a new tab if you want.
* `camera_app.html`: This builds the app and embeds the CSS and JavaScript files.
* `camera_app.css`: This designs the app.
* `camera_app.js`: This defines the two buttons using JavaScript. This avoids reloading the webpage. 


## Pictures
* `dual_robot.png`
