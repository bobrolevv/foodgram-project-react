FROM python:3.8
WORKDIR /app

COPY requirements.txt .

RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

#CMD python manage.py runserver 0:8000
CMD gunicorn backend.wsgi -b 0:8000