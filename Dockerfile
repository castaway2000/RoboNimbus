FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /dockercode
WORKDIR /dockercode
COPY . /dockercode
RUN pip3 install -r requirements.txt
EXPOSE 8000