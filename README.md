# Welcome to Geocodes-Fetcher-App

###### Python based geo cordinates fetching application


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

### ADD ENV VARIABLE API_KEY with your google cloud credentials

```
export API_KEY="<YOUR-GOOGLE-API-KEY-HERE>"
```

or

```
* vi ~/.bash_profile 
* export API_KEY="<YOUR-GOOGLE-API-KEY-HERE>"
* save ~/.bash_profile
* bash -l [To make available the environment variables]
* re-activate your virtualenv and proceed to the next step

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

2. Upload endpoints

2.1 Upload Endpoint Request Snapshot

![Application Landing Banner](https://github.com/TQUED/geocodes-fetcher-app/blob/master/imgs/upload_request.png)


2.2 Upload Endpoint Response Snapshot

![Application Landing Banner](https://github.com/TQUED/geocodes-fetcher-app/blob/master/imgs/upload_request-response.png)


2.3 Upload Endpoint Input Excel Format

![Application Landing Banner](https://github.com/TQUED/geocodes-fetcher-app/blob/master/imgs/input-excel-format.png)


2.4 Upload Endpoint Output Excel Format

![Application Landing Banner](https://github.com/TQUED/geocodes-fetcher-app/blob/master/imgs/output-excel-format.png)


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
