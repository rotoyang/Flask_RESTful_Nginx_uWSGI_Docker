FROM python:3.7.11-slim-buster

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  && apt-get install -y build-essential \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

RUN addgroup --system flask \
  && adduser --system --ingroup flask flask

COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r requirements.txt \
  && rm /requirements.txt

COPY --chown=flask:flask ./compose/dev/flask/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY --chown=flask:flask ./compose/dev/flask/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY --chown=flask:flask . /app

USER flask

WORKDIR /app

ENTRYPOINT ["/entrypoint"]

