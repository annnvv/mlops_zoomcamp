# Flask

## Python
```
import flask from Flask

app = Flask('app_name')

@app.route('/predict', methods = ["POST"])
def make_prediction():
    ##some code/function to make a prediction
    return 'prediciton'
    
if __name__ == "__main__": #for debugging
    app.run(debug = True, host = '0.0.0.0', port = 9696)
```

Use app to make predictions
```
new_data = {
  'customerid': 'tbd,
  'var1': 'val1',
}

import requests
url = 'http://localhost:9696/predict' ## this is the route we made for prediction

response = requests.post(url, json=new_data) ## post the newdata information in json format
result = response.json() ## get the server response

print(result)
```

## Command Line
```
#for unix based OSs:
gunicorn --bind 0.0.0.0:9696 app_name:app
#or 
#for windows OS:
waitress-serve --listen=0.0.0.0:9696 app_name:app
```
