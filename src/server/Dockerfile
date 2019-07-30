FROM python:3.7

# copy files
COPY . /var/app/backend

# set dir to run commands
WORKDIR /var/app/backend

# Expose python port
EXPOSE 5000

# Install Python dependencies
RUN pip install -r ./requirements.txt

# Run WSGI to host endpoints
#CMD [ "uwsgi", "--ini", "app.ini" ]
CMD [ "python", "./src/app.py" ]