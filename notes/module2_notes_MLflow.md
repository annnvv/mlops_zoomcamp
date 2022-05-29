# In Python 
MLflow Python documentation, [here](https://www.mlflow.org/docs/latest/python_api/index.html).

## Logging Experiments
```
import mlflow
```

```
mlflow.set_tracking_uri('db_type:///path_to_db') 
mlflow.set_experiment('name_of_experiment')
```

```
mlflow.{model}.autolog() ##av.note: make sure this is before mlflow.start_run()

with mlflow.start_run() as run:
	# .... modeling....

	mlflow.set_tag('tag_name', 'tag_value')
	mlflow.log_param('param_name', param_obj) or mlflow.log_params(parm_obj)
	mlflow.log_model(moldel_obj, artifact_path = 'path')
	mlflow.log_metric('metric_name', metric_obj)
	mlflow.log_artifact(artifact_obj or local_artifact_path, artifact_path)
	
mlflow.stop_run() ##av.note: not necessary if using `with mlflow.start_run() as run:`
```

For more information on logging functions, see MLflow docs [here](https://www.mlflow.org/docs/latest/tracking.html#logging-functions).

## Reading information/results of experiments

```
client = mlflow.tracking.MlflowClient(tracking_uri = 'db_type:///path_to_db')
experiment = client.get_experiment_by_name('experiment_name')

runs = client.search_runs(1)
params = runs[0].data.params
```

For more information on tracking, see MLflow docs [here](https://www.mlflow.org/docs/latest/python_api/mlflow.tracking.html).

# Command line 

Installing MLflow

```
pip install mlflow # or 
conda install -c conda-forge mlflow
```

To view the MLflow UI:

```
mlflow ui --backend-store-uri 'db_type:///path_to_db'
```

