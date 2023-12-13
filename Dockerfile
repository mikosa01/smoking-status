FROM python:3.9.4

# Create the user that will run the app
RUN adduser --disabled-password --gecos '' ml-api-user

WORKDIR /opt/ml_api

ARG PIP_EXTRA_INDEX_URL
ENV FLASK_APP run.py

# Print system information
RUN echo "System Information:"
RUN uname -a
RUN cat /etc/os-release

# Install requirements, including from Gemfury
ADD ./package/class_api /opt/ml_api/
RUN echo "Installing Python dependencies..."
RUN pip install --upgrade pip
RUN pip install -r /opt/ml_api/requirements.txt || { echo "ERROR: Pip install failed"; exit 1; }
RUN echo "Finished installing dependencies."

RUN chmod +x /opt/ml_api/run.sh
RUN chown -R ml-api-user:ml-api-user ./

USER ml-api-user

EXPOSE 5000

CMD ["bash", "./run.sh"]
