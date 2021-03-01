FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

RUN addgroup --system archiver \
    && adduser --system --ingroup archiver archiver

COPY ./requirements /requirements
RUN pip install --no-cache-dir -r /requirements/production.txt \
    && rm -rf /requirements

COPY --chown=archiver:archiver ./compose/production/archiver/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY --chown=archiver:archiver ./compose/production/archiver/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY --chown=archiver:archiver . /app

USER archiver

WORKDIR /app
ENTRYPOINT ["/entrypoint"]
