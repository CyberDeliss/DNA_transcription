FROM python:3.8

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install -U setuptools

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY main.py /code/main.py

COPY data /code/data/

COPY utilities.py /code/utilities.py

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]