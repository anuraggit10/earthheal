FROM python:3.10.2

RUN apt update

RUN mkdir /earthheal-be
WORKDIR /earthheal-be
COPY . /earthheal-be/

RUN pip install -r requirements.txt
RUN pip install gunicorn[gevent]

CMD gunicorn --worker-class gevent --workers 5 --bind 0.0.0.0:5000 --timeout 300 --graceful-timeout 300 wsgi:app


#CMD python main.py