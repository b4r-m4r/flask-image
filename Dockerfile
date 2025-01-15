FROM python:3.12-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py ./
ENV DOCKER_HOST="tcp://host.docker.internal:2375"
CMD ["python", "./main.py"]
