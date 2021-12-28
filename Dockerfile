FROM python:3.9-alpine3.15
RUN apk add build-base jpeg-dev zlib-dev
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY gitplot.py gitplot.py
CMD python gitplot.py