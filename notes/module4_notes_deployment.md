# Deployment

Webservice Deployment steps (used in this module):
1. Create virtual environment using pipenv
2. Create flask app
3. Create docker container to run flask app using info specified in pipenv and trained model

## pipenv - virtual environment
Docs for pipenv, see [here](https://pipenv-fork.readthedocs.io/en/latest/basics.html)

### Command Line
```
pip install pipenv
```

```
pipenv install [package_name(s)]==1.0.2  ##install packages
```

```
pipenv install --dev [package_name(s)] ##install packages only needed for development purposes
```

```
pipenv uninstall [package_name(s)] ##uninstall packages
```

```
pipenv shell #launch virtual env
```

## Webservice - using flask
Purpose: Having already built a machine learning model, use a web app (in this case Flask) to make predictions on new data. 

This means that we have to have: 
1) the trained model saved somewhere 
2) new data from which to make predictions (this new data must be formatted in exactly the same way as the training data!) 
    2b) a process to transform new raw data using the same steps that were performed on the training data. 

To use flask, it is preferrable to transform the data into JSON format. Also, the prediction (using requests) similarly returns a json format. 

See notes on Flask, [here](https://github.com/annnvv/mlops_zoomcamp/blob/main/notes/module4_notes_Flask.md).


## Docker
Always make sure that docker is running! (You won't be able to build or run docker containers if it isnt')

av.note: to self: have all things that need to be copied in the same directory! 

Once you have the docker container running, you can run scripts (like test.py) or commands using that container. 

### Command Line
Build a docker container and give it a tag
```
docker build -t [image_name]:[tag] . 
```

Run a docker container
```
docker run -it --rm -p [local_machine_port]:[container_por] [image_name]:[tag]
```


## Argparse
From [Real Python](https://realpython.com/command-line-interfaces-python-argparse/#how-to-use-the-python-argparse-library-to-create-a-command-line-interface)
Using the Python argparse library has four steps:
1. Import the Python argparse library
2. Create the parser
3. Add optional and positional arguments to the parser
4. Execute .parse_args()