FROM python:3.9

RUN adduser --disabled-password --gecos '' ml-api-user

WORKDIR  /opt/class_api

ARG PIP_EXTRA_INDEX_URL 
ENV FLASK_APP run.py

ADD ./package/class_api /opt/class_api/

RUN pip install --upgrade pip 
# COPY requirements.txt /opt/class_api/
RUN pip install -r /opt/class_api_api/requirements.txt

RUN chmod +x /opt/class_api/run.sh
RUN chown -R ml-api-user:ml-api-user ./

USER  ml-api-user

EXPOSE 5000

CMD ["bash", "./run.sh"]