FROM python:3.12
COPY . /opt
WORKDIR /opt
RUN pip install -r requirements.txt
EXPOSE 9000
CMD ["python3","app/manage.py","runserver","0.0.0.0:9000"]
