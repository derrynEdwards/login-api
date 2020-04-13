# Simple Flask based Microservice
This is a simple users microservice made with Flask for user creation and user authentication.
Running the API will automatically create an sqlite database to store and read users from.

## Requirements
- Python3
- .env file based on the `.env-sample`

## Installation

### Using the Makefile for complete installation
- Clone the repo `git clone https://github.com/derrynEdwards/login-api.git`
- `make all` to setup the venv, install required packages and run the api

### Using the Makefile step by step
- Clone the repo `git clone https://github.com/derrynEdwards/login-api.git`
- `make setup` to setup the venv
- `make install` to install the required packages in the venv
- `make start-api` to run the api

### Step by Step without Makefile
- Clone the repo `git clone https://github.com/derrynEdwards/login-api.git`
- *RECOMMENDED* Create a virtual environment `python3 -m venv ~/.login-api`
- Activate the virtual environment `source ~/.login-api/bin/activate`
- Install the required packages `pip install --upgrade pip` `pip install -r requirements.txt`
- Start the api `python web.py`

## Testing
The API will be running in port `5000`. 

### Endpoints
- /api/createuser
  - **Expects JSON**:
  
  ```
  {
      "username": "<username>",
      "password": "<password>",
      "email": "<email>"
  }
  ```

- /api/auth
  - **Expects JSON**:
  
  ```
  {
      "username": "<username>",
      "password": "<password>"
  }
  ```
## More to come...!