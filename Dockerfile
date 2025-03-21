FROM python:3.7-slim

RUN mkdir /main
COPY main.py /main/
CMD ["python", "/main/main.py"]

WORKDIR /main

