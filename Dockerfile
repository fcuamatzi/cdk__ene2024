FROM python:3.10-alpine

ADD ./src /code

WORKDIR /code

RUN pip install -r dependencies.txt

EXPOSE 3000

CMD ["python", "webservice.py"]


