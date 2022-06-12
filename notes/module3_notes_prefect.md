# Prefect
For more information on Prefect Orion (version 2.0), see [here](https://orion-docs.prefect.io/).

## Prefect Orchestration Steps

1. Create a script with @task and @flow decorators around functions or classes. 

2. Create a deployment specification (will need to specify flow function or script, schedule, and flow runner) 
    [Docs for deployment](https://orion-docs.prefect.io/concepts/deployments/) 
    [Docs for schedule](https://orion-docs.prefect.io/concepts/schedules/)
    [Docs for flow runner](https://orion-docs.prefect.io/concepts/flow-runners/)

3. Specify the orchestration engine (Prefect Cloud or a local Prefect API server started with `prefect orion start`)

4. Specify storage for flow deployments and results 
    [Docs for storage](https://orion-docs.prefect.io/concepts/storage/)

5. Specify a workqueue and an agent 
    [Docs for work-queue](https://orion-docs.prefect.io/concepts/work-queues/)


## Python
Toy Example
```
from prefect import flow, task, get_run_logger
from prefect.task_runners import SequentialTaskRunner

@task
def sometask(a: int, b:int): ##av.note: prefect supports type hinting via pydantic
    logger = get_run_logger()
    log.info('Some Info from a task')
    return a + b

def somefunction():
    pass

@flow(task_runner = SequentialTaskRunner()) ##av.note: if not specified, the default is ConcurrentTaskRunner
def main():
    sum = sometask(1, 2).results() ##av.note: need the results methods because futures...
    somefunction()

main()
```

Deployment and schedule

```
from datetime import timedelta
from prefect.deployments import Deployment Spec
from prefect.flow_runners import SuprocessFlowRunner
from prefect.blocks.storage import LocalFileSystem
from prefect.orion.schemas.schedules import IntervalSchedule

DeploymentSpec(
    name = 'model_training',
    flow = main, #or flow_location = "flow_script.py",
    flow_runner = SuprocessFlowRunner(), ##run this locally (Also can run in Docker or Kubernetes)
    flow_storage = LocalFileSystem('dir_path'),
    parameters = {},
    schedule = IntervalSchedule(interval=timedelta(days=1)),
    tags = ['ml']
)
```


## Command Line

Install prefect
```
pip install prefect
#or
conda install -c conda-forge prefect
```

Execute a prefect flow one time
```
python flow_script.py
```

**Launch prefect ui**
```
prefect orion start
```

**Create deployment**
```
prefect deployment create <filename>
```

Other deployment commands
```
prefect deployment create | run | execute | inspect | ls
```

Prefect storage on cloud
```
prefect storage ls
prefect storage create
```

**Create workqueue**
```
prefect work-queue create [OPTIONS] NAME
```

Workqueue
```
prefect work-queue preview 'work-queue-id-string' #view scheduled flow runs
prefect work-queue ls #view all available work queues
```

Agent
```
prefect agent start 'agent'
```

Clear Prefect database - will delete all data in `orion.db`
```
prefect orion database reset
```