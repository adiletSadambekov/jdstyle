FROM python:3.9

WORKDIR /app
ADD ./req.txt /app/
RUN pip install -r req.txt
ADD . /app/
CMD python manage.py migrate