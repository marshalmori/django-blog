FROM python:3.12-bullseye
ENV PYTHONUNBUFFERED=1

RUN mkdir /code

WORKDIR /code

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry install

COPY . .

EXPOSE 8000

ENTRYPOINT [ "poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000" ]

# ===========================================
# Criando a imagem do projeto
# 1 - sudo docker build -t djangocourse .

# 2 - sudo docker run -p 8005:8000 --name djangocourse djangocourse

# Roda enquanto o container estiver rodando
# 3 - sudo docker exec djangocourse poetry run python manage.py migrate

# Run docker container with volumes
# 4 - sudo docker run -p 8005:8000 --name djangocourse -v "$(pwd):/code" djangocourse

# 5 - sudo docker rm djangocourse

# 6 - sudo docker run -dp 8005:8000 --name djangocourse -v "$(pwd):/code" djangocourse
