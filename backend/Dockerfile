FROM python:3.10.6

EXPOSE 80

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN python -m pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r /code/requirements.txt

COPY ./ml /code/ml
COPY ./app /code/app

RUN pip install /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]