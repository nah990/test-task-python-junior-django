FROM python:3.10.0-alpine
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /django

RUN apk update \
    apk add --update --no-cache g++ gcc libxslt-dev && \
    apk add --no-cache openssl-dev libffi-dev && \
    apk add postgresql-dev gcc python3-dev musl-dev && \
    rm -rf /var/lib/apt/lists/*

COPY pyproject.toml .
ENV PYTHONPATH=${PYTHONPATH}:${PWD} 
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --only main

COPY . .
EXPOSE 8000  
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# docker build . -t only-backend
# docker run -p 8000:8000 only-backend