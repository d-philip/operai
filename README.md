# OperAI

## About The Project
By generating alluring images to accompany a vast selection of operas, OperAI allows anyone to experience opera regardless of their location. 

## Getting Started
To run OperAI locally, follow the instructions below:
### Prerequisites
* Install [Python](https://www.python.org/downloads/)
* Install [npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)
   * MacOS (Homebrew): `brew install node`

### Installation
1. Clone and navigate to the repo 
   ```sh
   git clone https://github.com/d-philip/operai.git
   cd operai
   ```
2. Install Python dependencies
   ```sh
   pip3 install -r requirements.txt
   ```
3. Run the Flask app
    ```sh
    export FLASK_APP=app.py
    flask run
    ```
4. Run the React app
    ```sh
    cd frontend
    npm i
    npm start
    ```