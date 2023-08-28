FROM python:3.10.6

WORKDIR /app

COPY cat_api_ok/app.py .
COPY cat_api_ok/get_features.py .
COPY cat_api_ok/dataset ./dataset
COPY requirements.txt .
COPY trained_model.h5 .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD uvicorn app:app --host 0.0.0.0 --port $PORT
