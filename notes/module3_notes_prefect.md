# Prefect
For more information on Prefect Orion (version 2.0), see [here](https://orion-docs.prefect.io/).

## Python
```
from prefect import flow, task, SequentialTaskRunner

@task
def sometask(a: int, b:int): ##av.note: prefect supports type hinting via pydantic
    return a + b

def somefunction():
    pass

@flow(task_runner = SequentialTaskRunner()) ##av.note: if not specified, the default is ConcurrentTaskRunner
def main():
    sum = sometask(1, 2).results() ##av.note: need the results methods if returning something from a task
    somefunction()

main()
```

## Command Line

Install prefect
```
pip install prefect
#or
conda install -c conda-forge prefect
```

Launch prefect ui
```
prefect orion start
```