FROM python:3.9-buster
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN python3.9 -m pip install -U pip setuptools
RUN pip install torch==1.7.1+cpu torchtext==0.8.1 -f https://download.pytorch.org/whl/torch_stable.html
RUN python3.9 -m pip install -r requirements.txt
RUN python3.9 -m spacy download en_core_web_sm
COPY . /app
CMD [ "python", "./run.py" ]
