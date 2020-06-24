FROM python:3.8.3-slim-buster
RUN apt-get update && \
    apt-get install -y gcc && \
    apt-get autoremove -y && \
    apt-get autoclean -y
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
EXPOSE 8000