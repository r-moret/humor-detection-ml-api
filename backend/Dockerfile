FROM python:3.10.7

EXPOSE 80

WORKDIR /code

COPY ./config.yaml ./config.yaml
COPY ./requirements.txt ./requirements.txt

RUN python -m pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r ./requirements.txt

COPY ./app ./app
COPY ./machine-learning ./machine-learning

RUN pip install ./app
RUN pip install ./machine-learning

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]