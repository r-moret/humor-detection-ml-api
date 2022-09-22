FROM python:3.10.6

EXPOSE 80

WORKDIR /code

COPY ./requirements.txt ./requirements.txt

RUN python -m pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r ./requirements.txt

COPY ./ml ./ml
COPY ./app ./app

RUN pip install ./app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]