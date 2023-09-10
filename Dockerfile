FROM python:3.10

WORKDIR /api

COPY ./requirements.txt /tmp/requirements.txt

RUN python -m pip install --upgrade pip && \
    python -m pip install -r /tmp/requirements.txt

COPY ./app app/

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
