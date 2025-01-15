FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py ./
ENV DOCKER_HOST="tcp://host.docker.internal:2375"
CMD ["python", "./main.py"]
