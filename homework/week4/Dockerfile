FROM agrigorev/zoomcamp-model:mlops-3.9.7-slim

# do stuff here
RUN pip install -U pip
RUN pip install pipenv

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy 

COPY ["starter_parameterized.py", "./starter_parameterized_docker.py"]

ENTRYPOINT ["python", "starter_parameterized_docker.py", "--model_path=model.bin", "--year=2021", "--month=4"]