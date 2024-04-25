FROM python:3.10-bullseye

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2 \
    && apt-get install -y netcat \
    && apt install gettext -y

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN pip install flake8
RUN pip install pymemcache

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh # Delete unnecessery characters [\r$]
RUN chmod +x /usr/src/app/entrypoint.sh

COPY . .
#RUN flake8 --ignore=E501,F401 .

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]