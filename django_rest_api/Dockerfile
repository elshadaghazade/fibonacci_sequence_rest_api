FROM ubuntu:latest
RUN apt update
RUN apt install -y python3
RUN apt install -y python3-pip
WORKDIR /app
ADD . /app
RUN pip3 install -r /app/requirements.txt
RUN python3 /app/manage.py makemigrations fibonacci_app
RUN python3 /app/manage.py migrate
CMD [ "python3", "/app/run.py" ]