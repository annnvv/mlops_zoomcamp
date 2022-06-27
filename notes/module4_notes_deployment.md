# Deployment


## pipenv - virtual environment

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