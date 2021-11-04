FROM python:3.9

COPY . /api
WORKDIR /api
RUN pip install --upgrade pip
RUN pip install --upgrade -r requirements.txt
CMD [ "python", "run.py" ]