# Welcome to Geocodes-Fetcher-App (now on Heroku!)

###### Python based geo cordinates fetching application

[Visit](https://geofinder.herokuapp.com)

## Project Goal

Using google Geocode API this application exposes endpoint to fetch coordinates(Latitude and Longitude) of a given address line. App reads a given excel file line by line and provides a result excel file with coordinates of each address line.



## Getting Started


**Note:** You have Python 3.5 or above installed with pip and virtualenv in a UNIX like box

### Virtual environment setup

```
virtualenv venv 
```

### Activate venv

```
source venv/bin/activate 
```

### Clone the repo

```
https://github.com/TQUED/geocodes-fetcher-app.git
```

### Navigate to the project

```
cd geocodes-fetcher-app
```

### Install Pre-Requisites

```
pip install -r requirements.txt
```

### Run this command in local

```
(venv)$python main.py 
 * Serving Flask app "main" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

### Endpoints

* /       - home page 
* /upload - upload excel file and fecth coordinates as excel

1. Index endpoint

![Application Landing Banner](https://github.com/TQUED/geocodes-fetcher-app/blob/master/imgs/get-url.png)

2. Upload endpoint

![Application Landing Banner](https://github.com/TQUED/geocodes-fetcher-app/blob/master/imgs/upload_request.png)


### Deactivate the virtual environment

```
deactivate
```

### Built With:


* Python - Server
* Flask - Framework
* Git - Version control tool


#### Deployment Tools:

* GitHub Actions
* Heroku


### Contributor:

* **Niraj Panda** - *Initial work* - [nirajKpanda](https://github.com/nirajKpanda)


Thank you
