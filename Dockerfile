FROM python:3.9-buster
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN python3.9 -m pip install -U pip setuptools
RUN python3.9 -m pip install -r requirements.txt
COPY . /app
RUN python3.9 -m spacy download en_core_web_sm
CMD [ "python", "./run.py" ]