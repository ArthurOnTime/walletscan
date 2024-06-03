FROM continuumio/miniconda3

WORKDIR /home/app

COPY requirements.txt /dependencies/requirements.txt
RUN pip install -r /dependencies/requirements.txt

COPY . /home/app

# gunicorn required for Heroku
CMD gunicorn api:app  --bind 0.0.0.0:$PORT --worker-class uvicorn.workers.UvicornWorker 