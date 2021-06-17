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
* Docker to run the app inside a container
* Kubernetes, in this case k3s to run the app inside a virtual machine or locally
* Vagrant to facilitate Kubernetes

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
* `requirements.txt`: This is used when wanting to install the prerequisites
* `Dockerfile`: This is used to build the docker image.

## To run on different platforms

The dualrobotpwm app folder should be used to run the code outside of the Raspberry Pi 4. To run this on Linux, Mac and Windows, here are the following steps to take for each OS:

### Linux
Python is already installed so instead make sure to install `pigpio`, `gpiozero` and `flask` using the `pip3 install` command. If you are using a virtual environment like virtualenv just use `pip install`. Then make sure to ssh into each robot and enable `pigpio` with `sudo pigpiod`.

### Windows

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


## Update

I added a `dualpwmtouch` directory so that touch support is available for touch devices. This replaces the mouseup and mousedown commands with touchstart and touchend. 

I added a `dualpwmtouch_debug` and `dualpwm_docker` directory for debugging and for docker.


## Running the Project with Docker

To run this project with docker follow this [link](https://docs.docker.com/get-docker/). Follow the instructions for Windows, Mac or Linux. Then once you do that you want to go to the `dualpwm_docker` directory and prepare to build the docker image. Follow these instructions closely:

* First build with `docker build -t python-dualrobot .`. The dot is needed to build on that directory.
* Check to see if it's created with `docker images`. It should be listed there.
* Then run with `docker -d -p 5000:5000 python-dualrobot`. Check it's running with `docker ps`. Go to `127.0.0.1:5000` to check it runs correctly.

If you want to push and tag this docker image, you'll need a dockerhub account. Once you do then use the `docker login` command to log in. Then run the `docker tag python-dualrobot linuxrobotgeek/python-dualrobot:tag-version`. You can put any tag you want like v1.0.1. Then to push it type `docker push linuxrobotgeek/python-dualrobot:tag-version`. And that's it. Once you finish you can logout with `docker logout` and you can stop the container with `docker stop [container-id]`.

## Running the app in Kubernetes

Using the Docker image you created you can run this app locally or on a virtual machine. If you want to run this locally you can use kind or if you're running it virtually use k3s. Install k3s using this [link](https://k3s.io/). Also install vagrant following this [link](https://www.vagrantup.com/downloads). Also make sure to have VirtualBox installed as well. Once that's done you need to run the VM with the vagrant file I have provided. Run the `vagrant up` command and the VM should work. To ssh into it run `vagrant ssh`. Once inside the VM install k3s inside the VM. Then to create a new deployment with `kubectl create deploy python-dualrobot --image=linuxrobotgeek/python-dualrobot:tagnumber`. Then check it was created with `kubectl get deploy` or `kubectl get po`. Next, to run it you want to port forward it with `kubectl port-forward svc/python-dualrobot --address 0.0.0.0 5000:5000`. Svc means service so if you use po for example make sure you get the pod id of it by running `kubectl get po`. Then go to `192.168.50.4:5000` and the app should now be displayed.

## Deploying the App using ArgoCD and Helm

Using the `argocd-python-robot.yaml` file you can deploy the app using ArgoCD. Make sure this runs under the VM created by the `Vagrantfile` I provide. Follow this [link](https://argoproj.github.io/argo-cd/getting_started/) to get started. Then use either `192.168.50.4:30007` or `192.168.50.4:30008` to go to ArgoCD. Follow the link provided to log in. Username is admin and password is whatever password is generated by the command that is mentioned in the installation guide. Then you can deploy the app from the VM with the `kubectl apply -f argocd-python-robot.yaml` and the app should appear under ArgoCD. If you want to use helm instead use the `argocd-helm-robot.yaml` or the `argocd-helm-robot-prod.yaml` file and then run the `kubectl apply -f` to either of the files and they should appear in ArgoCD. Also be sure to click the sync button to get things synchronized. 

![ArgoCD Screenshot](https://github.com/sentairanger/Flask-Dual-Robot/blob/main/Screenshot%20from%202021-06-16%2013-20-44.png)
