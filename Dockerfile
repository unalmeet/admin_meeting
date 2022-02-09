FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
ARG URL=0.0.0.0:4000

ENV DB_HOST     'adminmeeting_db'
ENV DB_PORT     '5432' 
ENV DB_USER     'unmeet' 
ENV DB_PASSWORD 'unmeet2021'
ENV DB_NAME     'unmeet_adminmeeting_db' 

CMD ["sh", "-c", "python manage.py makemigrations meetings && python manage.py migrate && python manage.py runserver $URL"]