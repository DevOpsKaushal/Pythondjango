FROM Python:3.12
COPY . /opt
RUN pip install -r requirements.txt
EXPOSE 9000
CMD ["python3","app/manage.py","runserver","0.0.0.0:9000"]
