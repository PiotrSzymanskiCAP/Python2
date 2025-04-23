## Check Code Formatting with Black

To ensure that your code is formatted according to Black's standards, you can run the following command:

```bash
black --check .
```

## Run Application using FastAPI

To ensure that your code is written using FastAPI and server correctly starts

```bash
uvicorn main:app --reload
```

## Application should be tested with coverage

Ensure that package name is correct (package_name = ETL2)

```bash
pytest --cov=ETL2
```

## Check if Application starts and provide Endpoints

http://localhost:8000/docs

