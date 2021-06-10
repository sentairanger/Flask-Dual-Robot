FROM python:3.8
LABEL maintainer="Edgardo Peregrino"

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

# command to run on container start
CMD [ "python", "dual_pwm_robot.py" ]
