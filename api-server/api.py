import mlflow 
import uvicorn
import json
import pandas as pd 
from pydantic import BaseModel
from typing import Literal, List, Union
from fastapi import FastAPI, File, UploadFile
print(mlflow.__version__)

description = """
API description
# Just try it 
"""

tags_metadata = [
    {
        "name": "tag_1",
        "description": "description"
    },
    {
        "name": "tag_2",
        "description": "description"
    }
]

# Input data types definition goes here
class Input(BaseModel):
    input: list

# FastAPI server creation
app = FastAPI(
    title="👽 Oxscan",
    description=description,
    version="0.1",
    contact={
        "name": "Aon",
        "url": "http://none.com",
    },
    openapi_tags=tags_metadata
)

# MLflow tracker configuration 
mlflow.set_tracking_uri("https://mlflow-s3-5c46c0d9d46b.herokuapp.com/")

# Loading all required models 
logged_model_name_1 = 'runs:/2d469d9db04b4bb7b63c8ec9c8aae5c2/xgboost'
logged_model_name_2 = 'runs:/2d469d9db04b4bb7b63c8ec9c8aae5c2/xgboost'
print('loading models...')
loaded_model_name_1 = mlflow.pyfunc.load_model(logged_model_name_1)
loaded_model_name_2 = mlflow.pyfunc.load_model(logged_model_name_2)
print('...models loaded')

# API endpoint creation
@app.post("/predict", tags=["tag_1"])
async def index(input:Input):

    # Read data 
    print(input)
    columns = ['col_1', 'col_2']
    features = pd.DataFrame([input.input], columns=columns)
    print(features)

    # Run prediction
    prediction = loaded_model_name_1.predict(features)
    print('prediction',prediction)

    # Format response
    response = {"prediction": prediction.tolist()[0]}
    return response
    
# Command to load the server 
if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=4000) # Here you define your web server to run the `app` variable (which contains FastAPI instance), with a specific host IP (0.0.0.0) and port (4000)