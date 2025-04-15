# pull official base image
FROM python:3.13-slim-bookworm

# set work directory
WORKDIR /bot

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# update system
RUN apt update && apt upgrade -y

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

# run
CMD ["python3", "/bot/main.py"]
