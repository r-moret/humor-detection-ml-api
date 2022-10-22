FROM python:3.10.7

EXPOSE 80

WORKDIR /code

COPY ./requirements.txt ./requirements.txt

RUN python -m pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r ./requirements.txt

COPY ./app ./app
COPY ./.streamlit ./.streamlit

CMD streamlit run ./app/main.py --server.address=0.0.0.0