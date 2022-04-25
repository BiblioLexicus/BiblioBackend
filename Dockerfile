FROM python:3.9

WORKDIR /app

COPY pyproject.toml ./

RUN pip install poetry

RUN poetry install

COPY . .

RUN poetry run python setup.py --auto --deploy --DB_PASSWORD placeholder --default_rep

ENV PORT=8000

EXPOSE 8000

CMD ["poetry", "run", "python", "Backend/manage.py", "runserver"]