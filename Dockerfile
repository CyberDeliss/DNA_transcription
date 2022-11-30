FROM python:3.8

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install -U setuptools

# install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends netcat
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY main.py /code/main.py

COPY entrypoint.sh /code/entrypoint.sh
RUN chmod 755 /code/entrypoint.sh

COPY data /code/data

COPY utilities.py /code/utilities.py

COPY command_line.py /code/command_line.py

ENTRYPOINT ["/code/entrypoint.sh"]

