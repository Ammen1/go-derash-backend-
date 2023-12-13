# FROM python:3.9-slim

# # Copy your local files to your Docker container
# COPY . /app

# # Update your environment to work within the folder you copied your files above into
# WORKDIR /app

# # Install python-dotenv
# RUN pip install python-dotenv

# # /opt: reserved for the installation of add-on application software packages.
# # We'll use this to create & store our virtual environment
# RUN mkdir -p /opt
# RUN python -m venv /opt/env
# ENV PATH="/opt/env/bin:$PATH"

# # Install requirements to the new virtual environment
# # requirements.txt must have gunicorn & django
# RUN /opt/env/bin/pip install --upgrade pip && \
#     /opt/env/bin/pip install -r requirements.txt

# # Copy entrypoint.sh and give execution permissions
# # COPY entrypoint.sh /app/entrypoint.sh
# # RUN chmod +x /app/entrypoint.sh

# # # Entrypoint script will be discussed later.
# # CMD [ "/app/entrypoint.sh"]


FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip uninstall django
RUN pip install -r requirements.txt