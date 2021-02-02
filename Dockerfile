FROM python:3.9-buster
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN python3.9 -m pip install -U pip setuptools
RUN pip install torch==1.7.1+cpu torchvision==0.8.2+cpu torchaudio==0.7.2 -f https://download.pytorch.org/whl/torch_stable.html
RUN python3.9 -m pip install -r requirements.txt
COPY . /app
RUN python3.9 -m spacy download en_core_web_sm
CMD [ "python", "./run.py" ]
