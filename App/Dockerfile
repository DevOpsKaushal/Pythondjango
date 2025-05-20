FROM python:3.12
RUN apt -y update && apt -y install pkg-config python3-dev gcc default-libmysqlclient-dev
COPY . /opt
WORKDIR /opt
RUN pip install -r requirements.txt
RUN pip install mysqlclient
EXPOSE 9000
CMD ["python3","manage.py","runserver","0.0.0.0:9000"]
